import csv
import unidecode
sqlfile = open("otherwords.sql", "a")
wordsfile = open("csvwords.txt", "a")

with open('words.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    wordList = []
    for row in csv_reader: 
        if len(row[0]) == 5:       
            decodedWord = unidecode.unidecode(row[0])
            if decodedWord not in wordList:
                wordList.append(decodedWord)
    for word in wordList:
        line_count += 1
        # insert = "insert into wordle.dictionary_word values (" + str(line_count) + ", '" + word + "');\n"
        insert = word + "\n"
        sqlfile.write(insert)
sqlfile.close()
