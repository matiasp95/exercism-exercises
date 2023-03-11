TO_TEXT = ["no", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
def recite(start, take=1):
    s = []
    for i in range(start,0,-1):
        if take == 0:
            break
        if i > 2:
            s.append(TO_TEXT[i] + " green bottles hanging on the wall,") 
            s.append(TO_TEXT[i] + " green bottles hanging on the wall,")
            s.append("And if one green bottle should accidentally fall,")
            s.append("There'll be " + TO_TEXT[i-1].lower() + " green bottles hanging on the wall.")
            s.append("")
        elif i == 2:
            s.append(TO_TEXT[i] + " green bottles hanging on the wall,") 
            s.append(TO_TEXT[i] + " green bottles hanging on the wall,")
            s.append("And if one green bottle should accidentally fall,")
            s.append("There'll be " + TO_TEXT[i-1].lower() + " green bottle hanging on the wall.")
            s.append("")
        else:
            s.append(TO_TEXT[i] + " green bottle hanging on the wall,") 
            s.append(TO_TEXT[i] + " green bottle hanging on the wall,")
            s.append("And if one green bottle should accidentally fall,")
            s.append("There'll be " + TO_TEXT[i-1].lower() + " green bottles hanging on the wall.")
            s.append("")
        take -= 1
    return s[:-1]
print(recite(2))
