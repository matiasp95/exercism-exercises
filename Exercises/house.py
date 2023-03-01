NURSERY = """This is the horse and the hound and the horn
that belonged to the farmer sowing his corn
that kept the rooster that crowed in the morn
that woke the priest all shaven and shorn
that married the man all tattered and torn
that kissed the maiden all forlorn
that milked the cow with the crumpled horn
that tossed the dog
that worried the cat
that killed the rat
that ate the malt
that lay in the house that Jack built."""
def recite(start_verse, end_verse):
    un = NURSERY.splitlines()
    ret = []
    for i in range(start_verse-1,end_verse):
        ret_str = "This is the "
        initial_str = un[11-i]
        ret_str += initial_str[initial_str.find("the")+3:] +" "+ " ".join(un[12-i:]) 
        ret.append(ret_str.rstrip())
    return ret
print(recite(12,12))