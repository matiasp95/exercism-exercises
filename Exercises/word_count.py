import re
def count_words(sentence):
    x = re.findall("\w+\'*\w", sentence.lower())
    my_dict = {}
    for i in x:
        my_dict[i] = my_dict.get(i,0)+1
    return my_dict
count_words("one fish two fish red fish blue fish")
