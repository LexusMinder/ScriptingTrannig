import pprint
message = "Yo estoy enamorado de una persona, pero al parecer no le intereso"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

#print(count)
pprint.pprint(count)
