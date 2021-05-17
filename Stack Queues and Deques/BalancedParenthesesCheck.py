def balance_check(s):
    # Check is even number of brackets
    if len(s) % 2 != 0:
        return False

    # Set of opening brackets
    opening = set('([{')

    # Matching Pairs
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    # Use a list as a "Stack"
    stack = []

    # Check every parenthesis in string
    for current in s:

        # If its an opening, append it to list
        if current in opening:
            stack.append(current)

        else:

            # Check that there are parentheses in Stack
            if len(stack) == 0:
                return False

            # Check the last open parenthesis
            last_open = stack.pop()

            # Check if it has a closing match
            if (last_open, current) not in matches:
                return False

    return len(stack) == 0

def check_balance_other_approach(s):
    opening = ['(','{','[']
    closing = [')','}',']']
    stack = []
    for i in s:
        if i in opening:
            stack.append(i)
        else:
            position=closing.index(i)
            if len(stack)>0 and opening[position] == stack[-1]:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

print(balance_check('()(){]}'))
print(check_balance_other_approach('()(){]}'))