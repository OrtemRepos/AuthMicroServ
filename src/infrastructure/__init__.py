def check_brackets(string: str) -> bool:
    stack: list[str] = []
    brackets: dict[str, str] = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in string:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
    return not stack


n = 6
alpha = "{][}"
char_values = {char: i for i, char in enumerate(alpha[::-1])}
input = "[]["
print(char_values)
