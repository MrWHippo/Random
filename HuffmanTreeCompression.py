
num = int(input("file 1 or 2? :"))
file = open(f"sentence{num}.txt", "r")
sentence = file.read().replace('\n', " ")

def letter_counter(sentence):
    counts = {}
    for i in sentence:
        counts[i] = sentence.count(i)
    return counts


def tree(s):
    done = False
    path = {}
    while done == False:
        a = 10**32
        b = 10**32
        for x in s:
            if s[x] < a:
                if s[x] < b:
                    try:
                        Temp = B
                        temp = b 
                        A = Temp
                        a = temp
                    except:
                        pass
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


total = 0
for keys in letter_counter(sentence):
    encoded = encode(keys, finalpath)
    print( keys,"=",encoded)
    total += len(encoded)


codedsentence = ""

for letter in sentence:
    codedsentence += encode(letter, finalpath)

meta = 24*len(sentencedict) + total /8
numbytes = (len(codedsentence) / 8) + meta 

print(codedsentence)
print(f"Total Size = {numbytes} bytes")
print(f"Size of meta = {meta} bytes")