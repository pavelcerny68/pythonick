mesta = [["Zlín", 76010], ["Jičín", 16792], ["Aš", 13093]]
mestoNad50tisObyvatel = [mesto[0] for mesto in mesta if mesto[1] > 50000]
mestoPocetObyvatel = [mesto[1] for mesto in mesta if mesto[1] > 50000]
print(str(mestoNad50tisObyvatel) + " má " + str(mestoPocetObyvatel) + " obyvatel")
