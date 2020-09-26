name = input()
new = name[0]
last = name[0]
for letter in name[1:]:
    if letter == last :
        continue
    new += letter
    last = letter
print(new)