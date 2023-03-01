OPERANDS = ["multiplied", "divided", "plus", "minus"]
def answer(question):
    if(question[-1] != "?"):
        raise ValueError("syntax error")
    question = question.replace("?", "")
    splitted = question.split()

    numbers = []
    operands = []
    
    for i in range(2, len(splitted)):
        if(i%2 != 0):
            if(splitted[i] not in OPERANDS):
                raise ValueError("unknown operation")
            operands.append(splitted[i])
        if(i%2 == 0):
            if(splitted[i].lstrip("-").isnumeric()):
                numbers.append(splitted[i])
            else:
                raise ValueError("syntax error")
    x = int(numbers[0])
    for i in range(len(operands)):
        if(operands[i] == OPERANDS[0]):
            x = x*int(numbers[i+1])
        if(operands[i] == OPERANDS[1]):
            x = x/int(numbers[i+1])
        if(operands[i] == OPERANDS[2]):
            x = x+int(numbers[i+1])
        if(operands[i] == OPERANDS[3]):
            x = x-int(numbers[i+1])
    return x

def xasdad(question):
    question = question.replace("?", "")
    question = question.replace("by", "")
    splitted = question.split()
    splitted = splitted[2:]
    if(len(splitted) == 1):
        return int(splitted[0])
    numbers = []
    operands = []
    for i in range(1,len(splitted),2):
        operands.append(splitted[i])
    for j in range(2,len(splitted),2):
        numbers.append(splitted[j])
    
    for i in operands:
        if(i not in OPERANDS and not i.lstrip("-").isnumeric()):
            raise ValueError("unknown operation")
        if(i.lstrip("-").isnumeric()):
            raise ValueError("syntax error")
    if(len(numbers) == 0):
        raise ValueError("syntax error")
    for j in numbers:
        if(not j.lstrip("-").isnumeric()):
            raise ValueError("syntax error")
    x = int(splitted[0])
    for i in range(len(operands)):
        if(operands[i] == OPERANDS[0]):
            x = x*int(numbers[i])
        if(operands[i] == OPERANDS[1]):
            x = x/int(numbers[i])
        if(operands[i] == OPERANDS[2]):
            x = x+int(numbers[i])
        if(operands[i] == OPERANDS[3]):
            x = x-int(numbers[i])
    return x



#print(xasdad("What is 52 cubed?"))
print(xasdad("What is 7 plus multiplied by -2?"))
#print(xasdad("What is 52 cubed?"))
