def proverb(*args, qualifier):
    if(qualifier == None):
        qualifier = ""
    else:
        qualifier = qualifier + " "

    ret = ["For want of a "+args[i]+" the "+args[i+1]+" was lost." for i in range(0, len(args)-1) if len(args) > 1]
    if(len(args) > 0):
        ret.append("And all for the want of a " + qualifier + args[0] +".")
    return ret

input_data = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
print(proverb(*input_data, qualifier=None))