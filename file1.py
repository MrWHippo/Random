file = open("readfile.txt","r")
newfile = open("writefile.txt","w")

text = file.read()
newfile.write(text)

file.close()
newfile.close()
