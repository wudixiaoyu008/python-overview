import re
import random

fhand = open('mbox.txt')
fhandanon = open('mbox-anon.txt', 'w')
fhandkey = open('mbox-anon-key.txt', 'w')

rhand = fhand.read()
file1 = rhand


email = re.findall(r'[\s<]([a-zA-Z]+\S+@\S+\.[a-zA-Z]+)', rhand)
newemail = list(set(email))

randomlist = random.sample(range(10000, 99999), len(newemail))

newrandom = []
for item in randomlist:
    a = "%%" + str(item) + "%%"
    newrandom.append(a)


i = 0
for item in newemail:
    file1 = file1.replace(item, newrandom[i])
    i = i + 1

# map
j = 0
for item in newemail:
    a = str(randomlist[j]) + "=" + newemail[j] + "\n"
    j = j + 1
    fhandkey.write(a)

fhandanon.write(file1)

fhand.close()
fhandanon.close()
fhandkey.close()
