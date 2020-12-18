lignesHappy = open("happynumbers.txt", "r").readlines()
lignesPrime = open("primenumbers.txt", "r").readlines()

for ligneH in lignesHappy :
    for ligneP in lignesPrime :
        if ligneH == ligneP :
            print (ligneH)

