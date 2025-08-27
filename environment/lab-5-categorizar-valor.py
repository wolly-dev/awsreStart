myMixedTypeList = [45, 290578, 1.02, True, "Meu cachorro tá na cama.", "45"]
for item in myMixedTypeList:
    #vou usar format atual.
    print(f"{item} é um dado do tipo {type(item)}!")