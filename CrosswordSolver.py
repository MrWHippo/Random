EnglishWords = open("AllEnglishWords.txt", "r")
allwords = EnglishWords.readlines()

word = input("Enter Crossword Problem: (in the format _,_,A,_,D)")
word.split(",")
word.remove(",")
        
def trim(allwords, length):
    search = ()
    for word in allwords:
        if length == len(word):
            search.append(word)

def searchfor(search,word):
    for x in range(len(word)):
        if word[x] != "_":
            for y in search:
                if y[x] != word[x]:
                    search.remove(y)
    return search


#searchlist = trim(allwords, len(word))
#print(searchfor(searchlist,word))
print(word)