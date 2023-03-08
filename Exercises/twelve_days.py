gifts = (
     "Drummers Drumming", 
            "Pipers Piping",
            "Lords-a-Leaping",
            "Ladies Dancing",
            "Maids-a-Milking",
            "Swans-a-Swimming",
            "Geese-a-Laying",
            "Gold Rings",
            "Calling Birds",
            "French Hens",
            "Turtle Doves",
            "Partridge in a Pear Tree"
)
nums = ("and a", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve")
days = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")
def recite(start_verse, end_verse):
    x = []
    while(end_verse+1 != start_verse):
        x.append(_gen_verse(start_verse))
        start_verse+=1
    return(x)
def _gen_verse(n):
    start = "On the " + days[n-1]+ " day of Christmas my true love gave to me:"
    for i in range(n):
        start = "{0} {1} {2}{3}".format(start,
                                   nums[n-i-1] if(n !=1) else "a",
                                   gifts[-n+i], "." if i==n-1 else ",")
    return start
print(recite(1,1))