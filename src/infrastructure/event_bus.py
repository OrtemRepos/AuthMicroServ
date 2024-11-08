from functools import singledispatchmethod
from typing import Any

from src.core.ports.event_bus import (
    CommandType,
    EventBusInterface,
    HandlerFuncCommandType,
    HandlerFuncQueryType,
    QueryType,
)

type EventType = CommandType | QueryType
type HandlerFunc = HandlerFuncCommandType | HandlerFuncQueryType


class EventBusAdapter(EventBusInterface):
    def __init__(
        self,
        command_bus: EventBusInterface[CommandType, HandlerFuncCommandType],
        query_bus: EventBusInterface[QueryType, HandlerFuncQueryType],
    ) -> None:
        self._command_bus = command_bus
        self._query_bus = query_bus

    async def publish(self, event: EventType) -> None:
        if isinstance(event, CommandType.__value__):
            await self._command_bus.publish(event=event)
        elif isinstance(event, QueryType.__value__):
            await self._query_bus.publish(event=event)
        else:
            raise TypeError(f"Expected {EventType}, but given {type(event)}")

    @singledispatchmethod
    def _override_subscribe(self, event_type: Any, handlers: list) -> bool:
        raise TypeError(
            f"Expected {EventType} and {list[HandlerFunc]},"
            f"but given {event_type} and {handlers}"
        )

    @_override_subscribe.register
    def _(
        self,
        event_type: type[CommandType],
        handlers: list[HandlerFuncCommandType],
    ) -> bool:
        return self._command_bus.subscribe(
            event_type=event_type, handlers=handlers
        )

    @_override_subscribe.register
    def _(
        self, event_type: type[QueryType], handlers: list[HandlerFuncQueryType]
    ) -> bool:
        return self._query_bus.subscribe(
            event_type=event_type, handlers=handlers
        )

    def subscribe(
        self, event_type: type[EventType], handlers: list[HandlerFunc]
    ) -> bool:
        return self._override_subscribe(event_type, handlers)
