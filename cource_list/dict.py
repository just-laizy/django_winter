words = {
    "hello":"salam",
    "thanks":"sagbol",
    "ok":"bolyar",
    "me":"men",
    "you":"sen",
    "who":"kim",
    "what":"name",
    "so":"onson",
}

# soz = input("Name gozleyaniz : ")

# print(tranTurkmen[soz])

eng_Words = []
tm_Words = []
eng_Words += words.keys()
tm_Words += words.values()

print ("Englsih words : ",eng_Words)
print ("Turkmen words : ",tm_Words)