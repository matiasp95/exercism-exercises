sentence = "abcdefghijklmnopqrstuvwxyz"
all_letters = "abcdefghijklmnopqrstuvwxyz"
for i in sentence:
    if i in all_letters:
        all_letters = all_letters.replace(i, "")
if len(all_letters) == 0:
    print("True")
print("False")