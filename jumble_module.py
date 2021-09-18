import random

def jumbleWord():
    file = open("Jumble Game\Jumble Words\words.txt",'r')
    words = file.read()
    word_list = words.split()
    word = random.choice(word_list)
    wordlist = list(word)
    length = len(wordlist)
    jumbledword = []
    mainstr = ""
    for i in range(length):
        rndmnum = random.randrange(length)
        jumbledword.append(wordlist.pop(rndmnum))
        length-=1
    for letter in jumbledword:
        mainstr = mainstr + letter # Jumbled Word
    f=open('__cache__.txt',"w")
    f.write(word)
    f.close()
    return mainstr