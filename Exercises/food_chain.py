import pprint


CONSTANTS_ANIMALS =("fly","spider", "bird","cat", "dog", "goat", "cow", "horse")
CONSTANT_PHRASES = ("","It wriggled and jiggled and tickled inside her.", "How absurd to swallow a bird!",
                     "Imagine that, to swallow a cat!", "What a hog, to swallow a dog!",
                       "Just opened her throat and swallowed a goat!", "I don't know how she swallowed a cow!",
                         "She's dead, of course!")
CONSTANT_COMPLETES = ("She swallowed the spider to catch the fly.", "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."
                      ,"She swallowed the cat to catch the bird.", "She swallowed the dog to catch the cat.", "She swallowed the goat to catch the dog.",
                      "She swallowed the cow to catch the goat.")
def recite(start_verse, end_verse):
    x = (end_verse - start_verse) + 1
    ret = []
    for i in range(x,0,-1):
        ret.append(single_recite(end_verse+1-i))
    l = [item for sublist in ret for item in sublist]
    return l[:-1]
def single_recite(end_verse):
    if end_verse == 8:
        return ["I know an old lady who swallowed a horse.","She's dead, of course!",""]
    s = ("I know an old lady who swallowed a {}.".format(CONSTANTS_ANIMALS[end_verse-1]) )
    s += ("\n" +CONSTANT_PHRASES[end_verse-1]) if end_verse != 1 else ""
    for i in range(end_verse,1,-1):
        s += ("\n" + CONSTANT_COMPLETES[i-2])
    s += ("\n" + "I don't know why she swallowed the fly. Perhaps she'll die.")
    s += "\n"
    return s.split("\n")
pprint.pprint(recite(1,8))