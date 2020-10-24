def stock_list(listOfArt, listOfCat):
    if len(listOfArt) == 0 or len(listOfCat) == 0:
        return ""
    else:
        dictOfArt = {}
        finalDict = {}
        for item in listOfArt:
            i = item.find(" ")
            dictOfArt[item[:i]] = int(item[i+1:])
        
        for item in listOfCat:
            if item not in dictOfArt.keys():
                dictOfArt[item] = 0

        keysToDel = []
        for key, value in dictOfArt.items():
            if key[0] in listOfCat:
                if finalDict.get(key[0]):
                    finalDict[key[0]] += value
                else:
                    finalDict[key[0]] = value
            else:
                keysToDel.append(key)

        for item in keysToDel:
            if item in finalDict.keys():
                del finalDict[item]

        finalStrings = []

        for item in listOfCat:
            key = item
            value = finalDict[key]
            finalStrings.append("({} : {})".format(key, value))

        finalString = " - ".join(finalStrings)

        return finalString