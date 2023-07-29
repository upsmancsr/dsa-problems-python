# Brackets are said to be balanced when every opening bracket has a corresponding closing bracket.
# Check if a given string has balanced brackets

def check_bracket_balance(str):
    stack = []
    for char in str:
        if char == '(' or char ==  '[' or char == '{':
            stack.append(char)
        if char == ')' or char == ']' or char == '}':
            if len(stack) == 0:
                return False
            matching_element = stack.pop()
            if not check_balance(matching_element, char):
                return False
    if len(stack) != 0:
        return False
    return True

def check_balance(opener, closer):
    if opener == '(' and closer == ')':
        return True
    if opener == '[' and closer == ']':
        return True
    if opener == '{' and closer == '}':
        return True
    return True

print(check_bracket_balance("{123(456[.768])}"))