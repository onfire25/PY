lignes = open("nameslist.txt", "r").readlines()
counter = 0

for ligne in lignes:
    counter += 1
print(counter)