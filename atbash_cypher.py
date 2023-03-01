PLAIN = "123456789abcdefghijklmnopqrstuvwxyz"
CIPHER = "123456789zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    s = ""
    plain_text = plain_text.replace(" ","").lower()
    plain_text = ''.join(e for e in plain_text if e.isalnum())
    for i in range(len(plain_text)):
        if(i % 5 == 0):
            s = s + " "
        ind = PLAIN.find(plain_text[i])
        s = s+CIPHER[ind]
    return s   

def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ","").lower()
    s = ""
    for i in range(len(ciphered_text)):
        ind = CIPHER.index(ciphered_text[i])
        s = s+PLAIN[ind]
    return s 

print(encode("O M G"))