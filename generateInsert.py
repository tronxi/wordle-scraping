file = open("words.txt", "r")
resultFile = open("result.sql", "a")
wordList = []
numWords = 0
for word in file:
    decodedWord = (word.lower().replace("\n", "")
        .replace("'", "")
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ç", "c")
        .replace("ä", "a")
        .replace("ë", "e")
        .replace("ï", "i")
        .replace("ö", "o")
        .replace("ü", "u")
        )
    if decodedWord not in wordList:
        wordList.append(decodedWord)
        insert = "insert into wordle.dictionary_word values (" + str(numWords) + ", '" + decodedWord + "');\n"
        resultFile.write(insert)
        numWords += 1
file.close()
resultFile.close()