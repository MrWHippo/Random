
#sentence = input("Enter Sentence: ").lower()
#sentence = "sentence ."

file = open("sentence.txt", "r")
sentence = file.read().replace('\n', " ")

def letter_counter(sentence):
    counts = {}
    for i in sentence:
        counts[i] = sentence.count(i)
    return counts


def tree(s):
    count = 0
    done = False
    path = {}
    while done == False:
        count += 1
        print(count)
        a = 10
        b = 10
        for x in s:
            if s[x] < a:
                if s[x] < b:
                    B = x
                    b = s[x]
                else:
                    A = x
                    a = s[x]
        del s[A]
        del s[B]
        s[A + B] = a+b
        path[A] = (A+B, "1")
        path[B] = (A+B, "0")
        if len(s) == 1:
            for k in s:
                finalpath = k
            done = True
    return path, finalpath


def encode(char, finalpath):
    temp = ""
    done = False
    while done == False:
        if char == finalpath:
            return temp
        else:
            if path[char][1][0] == "0":
                temp += "0"
            else:
                temp += "1"
            char = path[char][0]


sentencedict = letter_counter(sentence)
path, finalpath = tree(sentencedict)



for keys in letter_counter(sentence):
    print( keys ,encode(keys, finalpath))


codedsentence = ""

for letter in sentence:
    codedsentence += encode(letter, finalpath)

print(codedsentence)


