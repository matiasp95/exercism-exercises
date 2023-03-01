def is_paired(input_string):
    open_l = ["(", "{", "["]
    close_l = [")", "}", "]"]
    stack = []
    for i in input_string:
        if i in open_l:
            stack.append(i)
        elif((len(stack) == 0 and i in close_l) or (len(stack) > 0 and i in close_l and open_l[close_l.index(i)] != stack.pop())):
            return False
    return len(stack) == 0

print(is_paired("(((185 + 223.85) * 15) - 543)/2"))