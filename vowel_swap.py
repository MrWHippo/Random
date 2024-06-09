

entered_string = input("Enter some text: ")

entered_string = list(entered_string)

vowels = []
index = []
word = []

# break text into vowels and cons
for i in range(len(entered_string)):
    if entered_string[i] in "aeiou":
        vowels.append(entered_string[i])
        index.append(i)
    else:
        word.append(entered_string[i])

rebuilt_word = []
word.reverse()

# rebuild text
for i in range(len(entered_string)):
    if i in index:
        rebuilt_word.append(vowels.pop())
    else:
        rebuilt_word.append(word.pop())
        

altered_text = "".join(rebuilt_word)



print(altered_text)