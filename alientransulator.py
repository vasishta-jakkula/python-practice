aliendictionary = {"hello":"hlo","welcome":"wlcme","come":"cme","in":"n","can":"cn","you":"u","play": "ply", "with":"wth","me":"em"}
personenglishphrase = input("Please enter an english phrase or word and if its in the dictionary it will be transulated\n")
personenglishtoalientransulated = personenglishphrase.lower().split()

alienwords=[]
for word in personenglishtoalientransulated:
    if word in aliendictionary:
        alienwords.append(aliendictionary[word])
    else:
        alienwords.append(word)
print("In alien, say:","".join(alienwords))
