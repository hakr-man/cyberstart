import socket
import string


# load file name "backdoor.txt"
f = open("backdoor.txt", "r", encoding='utf-8')
# read file
# print(f.read())

#connect to a socket at localhost:10000 and send a random byte
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 10000))
s.send(b"Hello World")
key = s.recv(1024)
#convert key to string
key = key.decode("utf-8")
#split key into a list of strings
key = key.split("\n")

print(key)


#parse f into paragraphs
paragraphs = f.read().split("\n\n")
# parse paragraphs into lines
lines = [p.split("\n") for p in paragraphs]
# remove punctiation from each line
# lines = [[w.translate(str.maketrans('', '', string.punctuation)) for w in l] for l in lines]
# print(lines)
# parse array lines into words
words = [[l.split(" ") for l in p] for p in lines]

decoded = []

for i in key:
    if i == "":
        continue
    # print(i)
    #split i into 3 integers
    i = i.split(", ")
    # print(i)
    #print(i)
    paragraph = i[0]
    line = i[1]
    word = i[2]
    selectedParagraph = paragraphs[int(paragraph) - 1]
    #print(selectedParagraph)
    selectedLines = selectedParagraph.split("\n")
    selectedLine = selectedLines[int(i[1]) - 1]
    #print(selectedLine)
    #strip punctuation from selctedLines
    selectedLine = selectedLine.translate(str.maketrans('', '', string.punctuation))
    selectedWords = selectedLine.split(" ")
    selectedWord = selectedWords[int(i[2]) - 1]
    #print(selectedWord)
    decoded.append(selectedWord)
print(decoded)
# concat all words in decoded, separated by \n
decoded = "\n".join(decoded)
#send decoded to socket

s.send(decoded.encode("utf-8"))
data = s.recv(1024)
data = data.decode('utf-8')
s.close()
print(data)
