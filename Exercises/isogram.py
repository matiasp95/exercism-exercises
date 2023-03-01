string = "isogram"

list_of_chars = []
for i in string.lower():
    if(i.isalpha()):
        if(i not in list_of_chars):
            list_of_chars.append(i)
        else:
            print("False")
print("True")