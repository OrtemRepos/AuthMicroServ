from abc import ABC
from src.core.domain.entities.value_objects import ID


class Entity(ABC[ID]):
    id: ID
