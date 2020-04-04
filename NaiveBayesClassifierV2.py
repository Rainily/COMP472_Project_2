import math

# Function to print sum 
def checkKey(dict, key): 
    if key in dict.keys(): 
        return True
    return False

def createUnigramDictionary(vocabularyList):
    temporaryDictionary = {}

    for x in range(len(vocabularyList)):
        keyName = vocabularyList[x]
        temporaryDictionary[keyName] = 0

    return temporaryDictionary

def createBigramDictionary(vocabularyList):

    temporaryDictionary = {}

    for x in range(len(vocabularyList)):
        temporaryDictionary[vocabularyList[x]] = {}
        for y in range(len(vocabularyList)):
            temporaryDictionary[vocabularyList[x]][vocabularyList[y]] = 0


    return temporaryDictionary

def createTrigramDictionary(vocabularyList):
    
    temporaryDictionary = {}

    for x in range(len(vocabularyList)):
        temporaryDictionary[vocabularyList[x]] = {}
        for y in range(len(vocabularyList)):
            temporaryDictionary[vocabularyList[x]][vocabularyList[y]] = {}
            for z in range(len(vocabularyList)):
                temporaryDictionary[vocabularyList[x]][vocabularyList[y]][vocabularyList[z]] = 0

    return temporaryDictionary

# create class

class AI:
    def __init__(self):
        self.eu_table = {}
        self.ca_table = {}
        self.gl_table = {}
        self.es_table = {}
        self.en_table = {}
        self.pt_table = {}


    def score(self, tweet, nGramInt, smoothingValue):
        if nGramInt == 1:
            digitIndex = 0

            # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
            eu_score = 0
            ca_score = 0
            gl_score = 0
            es_score = 0
            en_score = 0
            pt_score = 0
            
            for k in self.eu_table.keys():
                self.eu_table[k] += smoothingValue
                self.ca_table[k] += smoothingValue
                self.gl_table[k] += smoothingValue
                self.es_table[k] += smoothingValue
                self.en_table[k] += smoothingValue
                self.pt_table[k] += smoothingValue

            eu_totalCharacters = 0
            ca_totalCharacters = 0
            gl_totalCharacters = 0
            es_totalCharacters = 0
            en_totalCharacters = 0
            pt_totalCharacters = 0


            for x in self.eu_table.keys():
                eu_totalCharacters += self.eu_table[x]
                ca_totalCharacters += self.ca_table[x]
                gl_totalCharacters += self.gl_table[x]
                es_totalCharacters += self.es_table[x]
                en_totalCharacters += self.en_table[x]
                pt_totalCharacters += self.pt_table[x]



            for y in range(len(tweet)):
                if checkKey(self.eu_table, tweet[digitIndex]):
                    eu_score += math.log(self.eu_table[tweet[digitIndex]] / eu_totalCharacters) # multiply by P(character | eu)
                    ca_score += math.log(self.ca_table[tweet[digitIndex]] / ca_totalCharacters) # multiply by P(character | eu)
                    gl_score += math.log(self.gl_table[tweet[digitIndex]] / gl_totalCharacters) # multiply by P(character | eu)
                    es_score += math.log(self.es_table[tweet[digitIndex]] / es_totalCharacters) # multiply by P(character | eu)
                    en_score += math.log(self.en_table[tweet[digitIndex]] / en_totalCharacters) # multiply by P(character | eu)
                    pt_score += math.log(self.pt_table[tweet[digitIndex]] / pt_totalCharacters) # multiply by P(character | eu)
                digitIndex += 1

            biggestValue = eu_score
            answer = 'eu'

            if ca_score > biggestValue:
                biggestValue = ca_score
                answer = 'ca'
            if gl_score > biggestValue:
                biggestValue = gl_score
                answer = 'gl'
            if es_score > biggestValue:
                biggestValue = es_score
                answer = 'es'
            if en_score > biggestValue:
                biggestValue = en_score
                answer = 'en'
            if pt_score > biggestValue:
                biggestValue = pt_score
                answer = 'pt'

            #print("ANSWER: " + answer)

            return answer, biggestValue, smoothingValue




        elif nGramInt == 2:
            # for vocInt = 0 and nGramInt = 1

            # index of the character we're scanning in the tweet
            firstDigitIndex = 0
            secondDigitIndex = 1


            for k in self.eu_table.keys():
                for l in self.eu_table.keys():
                    self.eu_table[k][l] += smoothingValue
                    self.ca_table[k][l] += smoothingValue
                    self.gl_table[k][l] += smoothingValue
                    self.es_table[k][l] += smoothingValue
                    self.en_table[k][l] += smoothingValue
                    self.pt_table[k][l] += smoothingValue

            # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
            eu_score = 0
            ca_score = 0
            gl_score = 0
            es_score = 0
            en_score = 0
            pt_score = 0

            for y in range(len(tweet) - 1):
                if checkKey(self.eu_table, tweet[firstDigitIndex]):
                    if checkKey(self.eu_table, tweet[secondDigitIndex]):

                        firstCharacterTotal = 0
                        for x in self.eu_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.eu_table[tweet[firstDigitIndex]][x]
                        eu_score += math.log(self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)
                        
                        firstCharacterTotal = 0
                        for x in self.ca_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.ca_table[tweet[firstDigitIndex]][x]
                        ca_score += math.log(self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.gl_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.gl_table[tweet[firstDigitIndex]][x]
                        gl_score += math.log(self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.es_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.es_table[tweet[firstDigitIndex]][x]
                        es_score += math.log(self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.en_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.en_table[tweet[firstDigitIndex]][x]
                        en_score += math.log(self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.pt_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.pt_table[tweet[firstDigitIndex]][x]
                        pt_score += math.log(self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                firstDigitIndex += 1
                secondDigitIndex += 1
            

            biggestValue = eu_score
            answer = 'eu'

            if ca_score > biggestValue:
                biggestValue = ca_score
                answer = 'ca'
            if gl_score > biggestValue:
                biggestValue = gl_score
                answer = 'gl'
            if es_score > biggestValue:
                biggestValue = es_score
                answer = 'es'
            if en_score > biggestValue:
                biggestValue = en_score
                answer = 'en'
            if pt_score > biggestValue:
                biggestValue = pt_score
                answer = 'pt'

            #print("ANSWER: " + answer)

            return answer, biggestValue, smoothingValue

        elif nGramInt == 3:
            # for vocInt = 0 and nGramInt = 1

            # index of the character we're scanning in the tweet
            firstDigitIndex = 0
            secondDigitIndex = 1
            thirdDigitIndex = 2


            for k in self.eu_table.keys():
                for l in self.eu_table.keys():
                    for m in self.eu_table.keys():
                        self.eu_table[k][l][m] += smoothingValue
                        self.ca_table[k][l][m] += smoothingValue
                        self.gl_table[k][l][m] += smoothingValue
                        self.es_table[k][l][m] += smoothingValue
                        self.en_table[k][l][m] += smoothingValue
                        self.pt_table[k][l][m] += smoothingValue

            # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
            eu_score = 0
            ca_score = 0
            gl_score = 0
            es_score = 0
            en_score = 0
            pt_score = 0

            for y in range(len(tweet) - 2):
                if checkKey(self.eu_table, tweet[firstDigitIndex]):
                    if checkKey(self.eu_table, tweet[secondDigitIndex]):
                        if checkKey(self.eu_table, tweet[thirdDigitIndex]):

                            firstTwoCharactersTotal = 0
                            for x in self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            eu_score += math.log(self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)
                            
                            firstTwoCharactersTotal = 0
                            for x in self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            ca_score += math.log(self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            gl_score += math.log(self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            es_score += math.log(self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            en_score += math.log(self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            pt_score += math.log(self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                firstDigitIndex += 1
                secondDigitIndex += 1
                thirdDigitIndex += 1

            biggestValue = eu_score
            answer = 'eu'

            if ca_score > biggestValue:
                biggestValue = ca_score
                answer = 'ca'
            if gl_score > biggestValue:
                biggestValue = gl_score
                answer = 'gl'
            if es_score > biggestValue:
                biggestValue = es_score
                answer = 'es'
            if en_score > biggestValue:
                biggestValue = en_score
                answer = 'en'
            if pt_score > biggestValue:
                biggestValue = pt_score
                answer = 'pt'

            #print("ANSWER: " + answer)

            return answer, biggestValue, smoothingValue


    def train(self, path, fileName, vocabularyList, vocInt, nGramInt):
        p = path # path to the folder with input files
        f = fileName + '.txt' # the name of input file
        fullPath = p + f # full path

        tweetID =  ''
        userID = ''
        language = ''
        tweet = ''

        counter = 0


        lineCounter = 0

        # Temporary Counter
        randomCounter = 0

        # table creation
        if nGramInt == 1:
            self.eu_table = createUnigramDictionary(vocabularyList)
            self.ca_table = createUnigramDictionary(vocabularyList)
            self.gl_table = createUnigramDictionary(vocabularyList)
            self.es_table = createUnigramDictionary(vocabularyList)
            self.en_table = createUnigramDictionary(vocabularyList)
            self.pt_table = createUnigramDictionary(vocabularyList)
        elif nGramInt == 2:
            self.eu_table = createBigramDictionary(vocabularyList)
            self.ca_table = createBigramDictionary(vocabularyList)
            self.gl_table = createBigramDictionary(vocabularyList)
            self.es_table = createBigramDictionary(vocabularyList)
            self.en_table = createBigramDictionary(vocabularyList)
            self.pt_table = createBigramDictionary(vocabularyList)
        elif nGramInt == 3:
            self.eu_table = createTrigramDictionary(vocabularyList)
            self.ca_table = createTrigramDictionary(vocabularyList)
            self.gl_table = createTrigramDictionary(vocabularyList)
            self.es_table = createTrigramDictionary(vocabularyList)
            self.en_table = createTrigramDictionary(vocabularyList)
            self.pt_table = createTrigramDictionary(vocabularyList)



        if nGramInt == 1:

            # read the input file
            with open(fullPath, encoding="utf8") as f:
                # split every number in a line
                for line in f:
                    # populate every variable
                    for word in line.split("\t"):
                        if counter == 0:
                            tweetID = word
                            counter += 1 
                        elif counter == 1:
                            userID = word
                            counter += 1
                        elif counter == 2:
                            language = word
                            counter += 1
                        else:
                            tweet = word
                            counter = 0

                    if language == 'eu':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength):
                            alreadyKey = False
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)
                            for k in self.eu_table.keys(): 
                                if tweet[x] == k:
                                    self.eu_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 1
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'ca':
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            for k in self.ca_table.keys():
                                if tweet[x] == k:
                                    self.ca_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 1
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'gl':
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            for k in self.gl_table.keys():
                                if tweet[x] == k:
                                    self.gl_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 1
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'es':
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            for k in self.es_table.keys():
                                if tweet[x] == k:
                                    self.es_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 1
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'en':
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            for k in self.en_table.keys():
                                if tweet[x] == k:
                                    self.en_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 1
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'pt':
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            for k in self.pt_table.keys():
                                if tweet[x] == k:
                                    self.pt_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 1
                    lineCounter += 1
                    print(lineCounter)
        elif nGramInt == 2:
            lineNumber = 0
            # read the input file
            with open(fullPath, encoding="utf8") as f:
                # split every number in a line
                for line in f:
                    firstDigitIndex = 0
                    secondDigitIndex = 1

                    # populate every variable
                    for word in line.split("\t"):
                        if counter == 0:
                            tweetID = word
                            counter += 1 
                        elif counter == 1:
                            userID = word
                            counter += 1
                        elif counter == 2:
                            language = word
                            counter += 1
                        else:
                            tweet = word
                            counter = 0 
                    # "Ruano, el autor que escribía para Goebbels, sobre próximo libro d @RosaSalaRose : http://t.co/qSabWfvj92 vía @LaVanguardia"
                    if language == 'eu':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.eu_table.keys():
                                if x == firstCharacter:
                                    for y in self.eu_table[x].keys():
                                        if y == secondCharacter:
                                            self.eu_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    if not checkKey(self.eu_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    if not checkKey(self.eu_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    self.eu_table[firstCharacter][secondCharacter] += 1
                    elif language == 'ca':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.ca_table.keys():
                                if x == firstCharacter:
                                    for y in self.ca_table[x].keys():
                                        if y == secondCharacter:
                                            self.ca_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    if not checkKey(self.ca_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        for x in self.ca_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    if not checkKey(self.ca_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0
                                        for x in self.ca_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    self.ca_table[firstCharacter][secondCharacter] += 1

                                    
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'gl':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.gl_table.keys():
                                if x == firstCharacter:
                                    for y in self.gl_table[x].keys():
                                        if y == secondCharacter:
                                            self.gl_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    if not checkKey(self.gl_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        for x in self.gl_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    if not checkKey(self.gl_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0
                                        for x in self.ca_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    self.gl_table[firstCharacter][secondCharacter] += 1

                                    
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'es':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.es_table.keys():
                                if x == firstCharacter:
                                    for y in self.es_table[x].keys():
                                        if y == secondCharacter:
                                            self.es_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    if not checkKey(self.es_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        for x in self.es_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    if not checkKey(self.es_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0
                                        for x in self.es_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    self.es_table[firstCharacter][secondCharacter] += 1

                                    
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'en':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.en_table.keys():
                                if x == firstCharacter:
                                    for y in self.en_table[x].keys():
                                        if y == secondCharacter:
                                            self.en_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    if not checkKey(self.en_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        for x in self.en_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    if not checkKey(self.en_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0
                                        for x in self.en_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    self.en_table[firstCharacter][secondCharacter] += 1

                                    
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'pt':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.pt_table.keys():
                                if x == firstCharacter:
                                    for y in self.pt_table[x].keys():
                                        if y == secondCharacter:
                                            self.pt_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    if not checkKey(self.pt_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        for x in self.pt_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    if not checkKey(self.pt_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0
                                        for x in self.pt_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    self.pt_table[firstCharacter][secondCharacter] += 1

                                    
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    lineNumber += 1
                    print(lineNumber)
        elif nGramInt == 3:
            lineNumber = 0
            # read the input file
            with open(fullPath, encoding="utf8") as f:
                # split every number in a line
                for line in f:
                    firstDigitIndex = 0
                    secondDigitIndex = 1
                    thirdDigitIndex = 2

                    # populate every variable
                    for word in line.split("\t"):
                        if counter == 0:
                            tweetID = word
                            counter += 1 
                        elif counter == 1:
                            userID = word
                            counter += 1
                        elif counter == 2:
                            language = word
                            counter += 1
                        else:
                            tweet = word
                            counter = 0 
                    # "Ruano, el autor que escribía para Goebbels, sobre próximo libro d @RosaSalaRose : http://t.co/qSabWfvj92 vía @LaVanguardia"
                    if language == 'eu':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.eu_table.keys():
                                if x == firstCharacter:
                                    for y in self.eu_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.eu_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    self.eu_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    if not checkKey(self.eu_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}


                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[firstCharacter][x][y] = 0
                                                self.ca_table[firstCharacter][x][y] = 0
                                                self.gl_table[firstCharacter][x][y] = 0
                                                self.es_table[firstCharacter][x][y] = 0
                                                self.en_table[firstCharacter][x][y] = 0
                                                self.pt_table[firstCharacter][x][y] = 0

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[x][firstCharacter][y] = 0
                                                self.ca_table[x][firstCharacter][y] = 0
                                                self.gl_table[x][firstCharacter][y] = 0
                                                self.es_table[x][firstCharacter][y] = 0
                                                self.en_table[x][firstCharacter][y] = 0
                                                self.pt_table[x][firstCharacter][y] = 0

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[x][y][firstCharacter] = 0
                                                self.ca_table[x][y][firstCharacter] = 0
                                                self.gl_table[x][y][firstCharacter] = 0
                                                self.es_table[x][y][firstCharacter] = 0
                                                self.en_table[x][y][firstCharacter] = 0
                                                self.pt_table[x][y][firstCharacter] = 0


                                    if not checkKey(self.eu_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}


                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[secondCharacter][x][y] = 0
                                                self.ca_table[secondCharacter][x][y] = 0
                                                self.gl_table[secondCharacter][x][y] = 0
                                                self.es_table[secondCharacter][x][y] = 0
                                                self.en_table[secondCharacter][x][y] = 0
                                                self.pt_table[secondCharacter][x][y] = 0

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[x][secondCharacter][y] = 0
                                                self.ca_table[x][secondCharacter][y] = 0
                                                self.gl_table[x][secondCharacter][y] = 0
                                                self.es_table[x][secondCharacter][y] = 0
                                                self.en_table[x][secondCharacter][y] = 0
                                                self.pt_table[x][secondCharacter][y] = 0

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[x][y][secondCharacter] = 0
                                                self.ca_table[x][y][secondCharacter] = 0
                                                self.gl_table[x][y][secondCharacter] = 0
                                                self.es_table[x][y][secondCharacter] = 0
                                                self.en_table[x][y][secondCharacter] = 0
                                                self.pt_table[x][y][secondCharacter] = 0

                                    if not checkKey(self.eu_table, thirdCharacter):
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}


                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}
                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[thirdCharacter][x][y] = 0
                                                self.ca_table[thirdCharacter][x][y] = 0
                                                self.gl_table[thirdCharacter][x][y] = 0
                                                self.es_table[thirdCharacter][x][y] = 0
                                                self.en_table[thirdCharacter][x][y] = 0
                                                self.pt_table[thirdCharacter][x][y] = 0

                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[x][thirdCharacter][y] = 0
                                                self.ca_table[x][thirdCharacter][y] = 0
                                                self.gl_table[x][thirdCharacter][y] = 0
                                                self.es_table[x][thirdCharacter][y] = 0
                                                self.en_table[x][thirdCharacter][y] = 0
                                                self.pt_table[x][thirdCharacter][y] = 0


                                        for x in self.eu_table.keys():
                                            for y in self.eu_table.keys():
                                                self.eu_table[x][y][thirdCharacter] = 0
                                                self.ca_table[x][y][thirdCharacter] = 0
                                                self.gl_table[x][y][thirdCharacter] = 0
                                                self.es_table[x][y][thirdCharacter] = 0
                                                self.en_table[x][y][thirdCharacter] = 0
                                                self.pt_table[x][y][thirdCharacter] = 0

                                    self.eu_table[firstCharacter][secondCharacter][thirdCharacter] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    if language == 'ca':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.ca_table.keys():
                                if x == firstCharacter:
                                    for y in self.ca_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.ca_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    self.ca_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    if not checkKey(self.ca_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}


                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[firstCharacter][x][y] = 0
                                                self.ca_table[firstCharacter][x][y] = 0
                                                self.gl_table[firstCharacter][x][y] = 0
                                                self.es_table[firstCharacter][x][y] = 0
                                                self.en_table[firstCharacter][x][y] = 0
                                                self.pt_table[firstCharacter][x][y] = 0

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[x][firstCharacter][y] = 0
                                                self.ca_table[x][firstCharacter][y] = 0
                                                self.gl_table[x][firstCharacter][y] = 0
                                                self.es_table[x][firstCharacter][y] = 0
                                                self.en_table[x][firstCharacter][y] = 0
                                                self.pt_table[x][firstCharacter][y] = 0

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[x][y][firstCharacter] = 0
                                                self.ca_table[x][y][firstCharacter] = 0
                                                self.gl_table[x][y][firstCharacter] = 0
                                                self.es_table[x][y][firstCharacter] = 0
                                                self.en_table[x][y][firstCharacter] = 0
                                                self.pt_table[x][y][firstCharacter] = 0


                                    if not checkKey(self.ca_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}


                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[secondCharacter][x][y] = 0
                                                self.ca_table[secondCharacter][x][y] = 0
                                                self.gl_table[secondCharacter][x][y] = 0
                                                self.es_table[secondCharacter][x][y] = 0
                                                self.en_table[secondCharacter][x][y] = 0
                                                self.pt_table[secondCharacter][x][y] = 0

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[x][secondCharacter][y] = 0
                                                self.ca_table[x][secondCharacter][y] = 0
                                                self.gl_table[x][secondCharacter][y] = 0
                                                self.es_table[x][secondCharacter][y] = 0
                                                self.en_table[x][secondCharacter][y] = 0
                                                self.pt_table[x][secondCharacter][y] = 0

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[x][y][secondCharacter] = 0
                                                self.ca_table[x][y][secondCharacter] = 0
                                                self.gl_table[x][y][secondCharacter] = 0
                                                self.es_table[x][y][secondCharacter] = 0
                                                self.en_table[x][y][secondCharacter] = 0
                                                self.pt_table[x][y][secondCharacter] = 0

                                    if not checkKey(self.ca_table, thirdCharacter):
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        for x in self.ca_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}


                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}
                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[thirdCharacter][x][y] = 0
                                                self.ca_table[thirdCharacter][x][y] = 0
                                                self.gl_table[thirdCharacter][x][y] = 0
                                                self.es_table[thirdCharacter][x][y] = 0
                                                self.en_table[thirdCharacter][x][y] = 0
                                                self.pt_table[thirdCharacter][x][y] = 0

                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[x][thirdCharacter][y] = 0
                                                self.ca_table[x][thirdCharacter][y] = 0
                                                self.gl_table[x][thirdCharacter][y] = 0
                                                self.es_table[x][thirdCharacter][y] = 0
                                                self.en_table[x][thirdCharacter][y] = 0
                                                self.pt_table[x][thirdCharacter][y] = 0


                                        for x in self.ca_table.keys():
                                            for y in self.ca_table.keys():
                                                self.eu_table[x][y][thirdCharacter] = 0
                                                self.ca_table[x][y][thirdCharacter] = 0
                                                self.gl_table[x][y][thirdCharacter] = 0
                                                self.es_table[x][y][thirdCharacter] = 0
                                                self.en_table[x][y][thirdCharacter] = 0
                                                self.pt_table[x][y][thirdCharacter] = 0

                                    self.ca_table[firstCharacter][secondCharacter][thirdCharacter] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    if language == 'gl':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.gl_table.keys():
                                if x == firstCharacter:
                                    for y in self.gl_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.gl_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    self.gl_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    if not checkKey(self.gl_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}


                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[firstCharacter][x][y] = 0
                                                self.ca_table[firstCharacter][x][y] = 0
                                                self.gl_table[firstCharacter][x][y] = 0
                                                self.es_table[firstCharacter][x][y] = 0
                                                self.en_table[firstCharacter][x][y] = 0
                                                self.pt_table[firstCharacter][x][y] = 0

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[x][firstCharacter][y] = 0
                                                self.ca_table[x][firstCharacter][y] = 0
                                                self.gl_table[x][firstCharacter][y] = 0
                                                self.es_table[x][firstCharacter][y] = 0
                                                self.en_table[x][firstCharacter][y] = 0
                                                self.pt_table[x][firstCharacter][y] = 0

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[x][y][firstCharacter] = 0
                                                self.ca_table[x][y][firstCharacter] = 0
                                                self.gl_table[x][y][firstCharacter] = 0
                                                self.es_table[x][y][firstCharacter] = 0
                                                self.en_table[x][y][firstCharacter] = 0
                                                self.pt_table[x][y][firstCharacter] = 0


                                    if not checkKey(self.gl_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}


                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[secondCharacter][x][y] = 0
                                                self.ca_table[secondCharacter][x][y] = 0
                                                self.gl_table[secondCharacter][x][y] = 0
                                                self.es_table[secondCharacter][x][y] = 0
                                                self.en_table[secondCharacter][x][y] = 0
                                                self.pt_table[secondCharacter][x][y] = 0

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[x][secondCharacter][y] = 0
                                                self.ca_table[x][secondCharacter][y] = 0
                                                self.gl_table[x][secondCharacter][y] = 0
                                                self.es_table[x][secondCharacter][y] = 0
                                                self.en_table[x][secondCharacter][y] = 0
                                                self.pt_table[x][secondCharacter][y] = 0

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[x][y][secondCharacter] = 0
                                                self.ca_table[x][y][secondCharacter] = 0
                                                self.gl_table[x][y][secondCharacter] = 0
                                                self.es_table[x][y][secondCharacter] = 0
                                                self.en_table[x][y][secondCharacter] = 0
                                                self.pt_table[x][y][secondCharacter] = 0

                                    if not checkKey(self.gl_table, thirdCharacter):
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        for x in self.gl_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}


                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}
                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[thirdCharacter][x][y] = 0
                                                self.ca_table[thirdCharacter][x][y] = 0
                                                self.gl_table[thirdCharacter][x][y] = 0
                                                self.es_table[thirdCharacter][x][y] = 0
                                                self.en_table[thirdCharacter][x][y] = 0
                                                self.pt_table[thirdCharacter][x][y] = 0

                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[x][thirdCharacter][y] = 0
                                                self.ca_table[x][thirdCharacter][y] = 0
                                                self.gl_table[x][thirdCharacter][y] = 0
                                                self.es_table[x][thirdCharacter][y] = 0
                                                self.en_table[x][thirdCharacter][y] = 0
                                                self.pt_table[x][thirdCharacter][y] = 0


                                        for x in self.gl_table.keys():
                                            for y in self.gl_table.keys():
                                                self.eu_table[x][y][thirdCharacter] = 0
                                                self.ca_table[x][y][thirdCharacter] = 0
                                                self.gl_table[x][y][thirdCharacter] = 0
                                                self.es_table[x][y][thirdCharacter] = 0
                                                self.en_table[x][y][thirdCharacter] = 0
                                                self.pt_table[x][y][thirdCharacter] = 0

                                    self.gl_table[firstCharacter][secondCharacter][thirdCharacter] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    if language == 'es':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.es_table.keys():
                                if x == firstCharacter:
                                    for y in self.es_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.es_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    self.es_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    if not checkKey(self.es_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}


                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[firstCharacter][x][y] = 0
                                                self.ca_table[firstCharacter][x][y] = 0
                                                self.gl_table[firstCharacter][x][y] = 0
                                                self.es_table[firstCharacter][x][y] = 0
                                                self.en_table[firstCharacter][x][y] = 0
                                                self.pt_table[firstCharacter][x][y] = 0

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[x][firstCharacter][y] = 0
                                                self.ca_table[x][firstCharacter][y] = 0
                                                self.gl_table[x][firstCharacter][y] = 0
                                                self.es_table[x][firstCharacter][y] = 0
                                                self.en_table[x][firstCharacter][y] = 0
                                                self.pt_table[x][firstCharacter][y] = 0

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[x][y][firstCharacter] = 0
                                                self.ca_table[x][y][firstCharacter] = 0
                                                self.gl_table[x][y][firstCharacter] = 0
                                                self.es_table[x][y][firstCharacter] = 0
                                                self.en_table[x][y][firstCharacter] = 0
                                                self.pt_table[x][y][firstCharacter] = 0


                                    if not checkKey(self.es_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}


                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[secondCharacter][x][y] = 0
                                                self.ca_table[secondCharacter][x][y] = 0
                                                self.gl_table[secondCharacter][x][y] = 0
                                                self.es_table[secondCharacter][x][y] = 0
                                                self.en_table[secondCharacter][x][y] = 0
                                                self.pt_table[secondCharacter][x][y] = 0

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[x][secondCharacter][y] = 0
                                                self.ca_table[x][secondCharacter][y] = 0
                                                self.gl_table[x][secondCharacter][y] = 0
                                                self.es_table[x][secondCharacter][y] = 0
                                                self.en_table[x][secondCharacter][y] = 0
                                                self.pt_table[x][secondCharacter][y] = 0

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[x][y][secondCharacter] = 0
                                                self.ca_table[x][y][secondCharacter] = 0
                                                self.gl_table[x][y][secondCharacter] = 0
                                                self.es_table[x][y][secondCharacter] = 0
                                                self.en_table[x][y][secondCharacter] = 0
                                                self.pt_table[x][y][secondCharacter] = 0

                                    if not checkKey(self.es_table, thirdCharacter):
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        for x in self.es_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}


                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}
                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[thirdCharacter][x][y] = 0
                                                self.ca_table[thirdCharacter][x][y] = 0
                                                self.gl_table[thirdCharacter][x][y] = 0
                                                self.es_table[thirdCharacter][x][y] = 0
                                                self.en_table[thirdCharacter][x][y] = 0
                                                self.pt_table[thirdCharacter][x][y] = 0

                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[x][thirdCharacter][y] = 0
                                                self.ca_table[x][thirdCharacter][y] = 0
                                                self.gl_table[x][thirdCharacter][y] = 0
                                                self.es_table[x][thirdCharacter][y] = 0
                                                self.en_table[x][thirdCharacter][y] = 0
                                                self.pt_table[x][thirdCharacter][y] = 0


                                        for x in self.es_table.keys():
                                            for y in self.es_table.keys():
                                                self.eu_table[x][y][thirdCharacter] = 0
                                                self.ca_table[x][y][thirdCharacter] = 0
                                                self.gl_table[x][y][thirdCharacter] = 0
                                                self.es_table[x][y][thirdCharacter] = 0
                                                self.en_table[x][y][thirdCharacter] = 0
                                                self.pt_table[x][y][thirdCharacter] = 0

                                    self.es_table[firstCharacter][secondCharacter][thirdCharacter] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    if language == 'en':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.en_table.keys():
                                if x == firstCharacter:
                                    for y in self.en_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.en_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    self.en_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    if not checkKey(self.en_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}


                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[firstCharacter][x][y] = 0
                                                self.ca_table[firstCharacter][x][y] = 0
                                                self.gl_table[firstCharacter][x][y] = 0
                                                self.es_table[firstCharacter][x][y] = 0
                                                self.en_table[firstCharacter][x][y] = 0
                                                self.pt_table[firstCharacter][x][y] = 0

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[x][firstCharacter][y] = 0
                                                self.ca_table[x][firstCharacter][y] = 0
                                                self.gl_table[x][firstCharacter][y] = 0
                                                self.es_table[x][firstCharacter][y] = 0
                                                self.en_table[x][firstCharacter][y] = 0
                                                self.pt_table[x][firstCharacter][y] = 0

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[x][y][firstCharacter] = 0
                                                self.ca_table[x][y][firstCharacter] = 0
                                                self.gl_table[x][y][firstCharacter] = 0
                                                self.es_table[x][y][firstCharacter] = 0
                                                self.en_table[x][y][firstCharacter] = 0
                                                self.pt_table[x][y][firstCharacter] = 0


                                    if not checkKey(self.en_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}


                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[secondCharacter][x][y] = 0
                                                self.ca_table[secondCharacter][x][y] = 0
                                                self.gl_table[secondCharacter][x][y] = 0
                                                self.es_table[secondCharacter][x][y] = 0
                                                self.en_table[secondCharacter][x][y] = 0
                                                self.pt_table[secondCharacter][x][y] = 0

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[x][secondCharacter][y] = 0
                                                self.ca_table[x][secondCharacter][y] = 0
                                                self.gl_table[x][secondCharacter][y] = 0
                                                self.es_table[x][secondCharacter][y] = 0
                                                self.en_table[x][secondCharacter][y] = 0
                                                self.pt_table[x][secondCharacter][y] = 0

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[x][y][secondCharacter] = 0
                                                self.ca_table[x][y][secondCharacter] = 0
                                                self.gl_table[x][y][secondCharacter] = 0
                                                self.es_table[x][y][secondCharacter] = 0
                                                self.en_table[x][y][secondCharacter] = 0
                                                self.pt_table[x][y][secondCharacter] = 0

                                    if not checkKey(self.en_table, thirdCharacter):
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        for x in self.en_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}


                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}
                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[thirdCharacter][x][y] = 0
                                                self.ca_table[thirdCharacter][x][y] = 0
                                                self.gl_table[thirdCharacter][x][y] = 0
                                                self.es_table[thirdCharacter][x][y] = 0
                                                self.en_table[thirdCharacter][x][y] = 0
                                                self.pt_table[thirdCharacter][x][y] = 0

                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[x][thirdCharacter][y] = 0
                                                self.ca_table[x][thirdCharacter][y] = 0
                                                self.gl_table[x][thirdCharacter][y] = 0
                                                self.es_table[x][thirdCharacter][y] = 0
                                                self.en_table[x][thirdCharacter][y] = 0
                                                self.pt_table[x][thirdCharacter][y] = 0


                                        for x in self.en_table.keys():
                                            for y in self.en_table.keys():
                                                self.eu_table[x][y][thirdCharacter] = 0
                                                self.ca_table[x][y][thirdCharacter] = 0
                                                self.gl_table[x][y][thirdCharacter] = 0
                                                self.es_table[x][y][thirdCharacter] = 0
                                                self.en_table[x][y][thirdCharacter] = 0
                                                self.pt_table[x][y][thirdCharacter] = 0

                                    self.en_table[firstCharacter][secondCharacter][thirdCharacter] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    if language == 'pt':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.pt_table.keys():
                                if x == firstCharacter:
                                    for y in self.pt_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.pt_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    self.pt_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            if vocInt == 2 and alreadyKey == False:
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    if not checkKey(self.pt_table, firstCharacter):
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}


                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[firstCharacter][x][y] = 0
                                                self.ca_table[firstCharacter][x][y] = 0
                                                self.gl_table[firstCharacter][x][y] = 0
                                                self.es_table[firstCharacter][x][y] = 0
                                                self.en_table[firstCharacter][x][y] = 0
                                                self.pt_table[firstCharacter][x][y] = 0

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[x][firstCharacter][y] = 0
                                                self.ca_table[x][firstCharacter][y] = 0
                                                self.gl_table[x][firstCharacter][y] = 0
                                                self.es_table[x][firstCharacter][y] = 0
                                                self.en_table[x][firstCharacter][y] = 0
                                                self.pt_table[x][firstCharacter][y] = 0

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[x][y][firstCharacter] = 0
                                                self.ca_table[x][y][firstCharacter] = 0
                                                self.gl_table[x][y][firstCharacter] = 0
                                                self.es_table[x][y][firstCharacter] = 0
                                                self.en_table[x][y][firstCharacter] = 0
                                                self.pt_table[x][y][firstCharacter] = 0


                                    if not checkKey(self.pt_table, secondCharacter):
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}


                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[secondCharacter][x][y] = 0
                                                self.ca_table[secondCharacter][x][y] = 0
                                                self.gl_table[secondCharacter][x][y] = 0
                                                self.es_table[secondCharacter][x][y] = 0
                                                self.en_table[secondCharacter][x][y] = 0
                                                self.pt_table[secondCharacter][x][y] = 0

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[x][secondCharacter][y] = 0
                                                self.ca_table[x][secondCharacter][y] = 0
                                                self.gl_table[x][secondCharacter][y] = 0
                                                self.es_table[x][secondCharacter][y] = 0
                                                self.en_table[x][secondCharacter][y] = 0
                                                self.pt_table[x][secondCharacter][y] = 0

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[x][y][secondCharacter] = 0
                                                self.ca_table[x][y][secondCharacter] = 0
                                                self.gl_table[x][y][secondCharacter] = 0
                                                self.es_table[x][y][secondCharacter] = 0
                                                self.en_table[x][y][secondCharacter] = 0
                                                self.pt_table[x][y][secondCharacter] = 0

                                    if not checkKey(self.pt_table, thirdCharacter):
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        for x in self.pt_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}


                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}
                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[thirdCharacter][x][y] = 0
                                                self.ca_table[thirdCharacter][x][y] = 0
                                                self.gl_table[thirdCharacter][x][y] = 0
                                                self.es_table[thirdCharacter][x][y] = 0
                                                self.en_table[thirdCharacter][x][y] = 0
                                                self.pt_table[thirdCharacter][x][y] = 0

                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[x][thirdCharacter][y] = 0
                                                self.ca_table[x][thirdCharacter][y] = 0
                                                self.gl_table[x][thirdCharacter][y] = 0
                                                self.es_table[x][thirdCharacter][y] = 0
                                                self.en_table[x][thirdCharacter][y] = 0
                                                self.pt_table[x][thirdCharacter][y] = 0


                                        for x in self.pt_table.keys():
                                            for y in self.pt_table.keys():
                                                self.eu_table[x][y][thirdCharacter] = 0
                                                self.ca_table[x][y][thirdCharacter] = 0
                                                self.gl_table[x][y][thirdCharacter] = 0
                                                self.es_table[x][y][thirdCharacter] = 0
                                                self.en_table[x][y][thirdCharacter] = 0
                                                self.pt_table[x][y][thirdCharacter] = 0

                                    self.pt_table[firstCharacter][secondCharacter][thirdCharacter] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1 

                    lineNumber += 1
                    print(lineNumber)                   

    def scoreFile (self, path, fileName, vocInt, nGramInt, smoothingValue):
        #Writing into the trace file for Unigram
        tweetCounter = 0

        correctCounter = 0

        eu_tweet_counter = 0
        ca_tweet_counter = 0
        gl_tweet_counter = 0
        es_tweet_counter = 0
        en_tweet_counter = 0
        pt_tweet_counter = 0

        eu_tweet_counter_correct = 0
        ca_tweet_counter_correct = 0
        gl_tweet_counter_correct = 0
        es_tweet_counter_correct = 0
        en_tweet_counter_correct = 0
        pt_tweet_counter_correct = 0

        eu_tweet_counter_guessed = 0
        ca_tweet_counter_guessed = 0
        gl_tweet_counter_guessed = 0
        es_tweet_counter_guessed = 0
        en_tweet_counter_guessed = 0
        pt_tweet_counter_guessed = 0

        with open(path + fileName + ".txt", encoding="utf8") as w:
            testPath ="trace_"+ str(vocInt) + "_"+ str(nGramInt)+ "_" + str(smoothingValue) + ".txt"
            writeFile = open(testPath,"w+", encoding="utf8")
            for line in w:
                if tweetCounter == 20:
                    break
                tweetCounter += 1
                word = line.split("\t")
                 
                if word[2] == 'eu':
                    eu_tweet_counter += 1
                elif word[2] == 'ca':
                    ca_tweet_counter += 1
                elif word[2] == 'gl':
                    gl_tweet_counter += 1
                elif word[2] == 'es':
                    es_tweet_counter += 1
                elif word[2] == 'en':
                    en_tweet_counter += 1
                elif word[2] == 'pt':
                    pt_tweet_counter += 1

                guessedLanguage, guessedScore, smoothingValue = self.score(word[3], nGramInt, smoothingValue)

                if guessedLanguage == 'eu':
                    eu_tweet_counter_guessed += 1
                elif guessedLanguage == 'ca':
                    ca_tweet_counter_guessed += 1
                elif guessedLanguage == 'gl':
                    gl_tweet_counter_guessed += 1
                elif guessedLanguage == 'es':
                    es_tweet_counter_guessed += 1
                elif guessedLanguage == 'en':
                    en_tweet_counter_guessed += 1
                elif guessedLanguage == 'pt':
                    pt_tweet_counter_guessed += 1

                if guessedLanguage == word[2]:
                    correctOrNot = "Correct"
                    if word[2] == 'eu':
                        eu_tweet_counter_correct += 1
                    elif word[2] == 'ca':
                        ca_tweet_counter_correct += 1
                    elif word[2] == 'gl':
                        gl_tweet_counter_correct += 1
                    elif word[2] == 'es':
                        es_tweet_counter_correct += 1
                    elif word[2] == 'en':
                        en_tweet_counter_correct += 1
                    elif word[2] == 'pt':
                        pt_tweet_counter_correct += 1
                    correctCounter += 1
                else:
                    correctOrNot = "Wrong"             
                writeFile.write(word[0] + "  " + guessedLanguage + "  " + str(guessedScore) + "  " + word[2] + "  " + correctOrNot + "\n")
            writeFile.close()
        
        statisticFileName ="stat_"+ str(vocInt) + "_"+ str(nGramInt)+ "_" + str(smoothingValue) + ".txt"
        writeFile = open(statisticFileName,"w+", encoding="utf8")
        
        # Accuracy
        accuracy = 0

        writeFile.write("Accuracy:\n")

        if tweetCounter != 0:
            accuracy = correctCounter / tweetCounter
        
        writeFile.write(str(correctCounter) + "/" + str(tweetCounter) + " = ~" + str(round(accuracy * 100, 2)) + "%\n")
        
        writeFile.write('\n')

        # Precision
        eu_precision = 0
        ca_precision = 0
        gl_precision = 0
        es_precision = 0
        en_precision = 0
        pt_precision = 0

        writeFile.write("Precision:\n")
        if eu_tweet_counter_guessed != 0:
            eu_precision = eu_tweet_counter_correct / eu_tweet_counter_guessed 
        writeFile.write("EU: " + str(eu_tweet_counter_correct) + "/" + str(eu_tweet_counter_guessed) + " =  ~" + str(round(eu_precision * 100, 2)) + "%\n")
        
        if ca_tweet_counter_guessed != 0:
            ca_precision = ca_tweet_counter_correct / ca_tweet_counter_guessed 
        writeFile.write("CA: " + str(ca_tweet_counter_correct) + "/" + str(ca_tweet_counter_guessed) + " =  ~" + str(round(ca_precision * 100, 2)) + "%\n")
        
        if gl_tweet_counter_guessed != 0:
            gl_precision = gl_tweet_counter_correct / gl_tweet_counter_guessed 
        writeFile.write("GL: " + str(gl_tweet_counter_correct) + "/" + str(gl_tweet_counter_guessed) + " =  ~" + str(round(gl_precision * 100, 2)) + "%\n")
        
        if es_tweet_counter_guessed != 0:
            es_precision = es_tweet_counter_correct / es_tweet_counter_guessed 
        writeFile.write("ES: " + str(es_tweet_counter_correct) + "/" + str(es_tweet_counter_guessed) + " =  ~" + str(round(es_precision * 100, 2)) + "%\n")
        
        if en_tweet_counter_guessed != 0:
            en_precision = en_tweet_counter_correct / en_tweet_counter_guessed 
        writeFile.write("EN: " + str(en_tweet_counter_correct) + "/" + str(en_tweet_counter_guessed) + " =  ~" + str(round(en_precision * 100, 2)) + "%\n")
        
        if pt_tweet_counter_guessed != 0:
            pt_precision = pt_tweet_counter_correct / pt_tweet_counter_guessed 
        writeFile.write("PT: " + str(pt_tweet_counter_correct) + "/" + str(pt_tweet_counter_guessed) + " =  ~" + str(round(pt_precision * 100, 2)) + "%\n")
        
        writeFile.write('\n')

        # Recall
        eu_recall = 0
        ca_recall = 0
        gl_recall = 0
        es_recall = 0
        en_recall = 0
        pt_recall = 0

        writeFile.write("Recall:\n")

        if eu_tweet_counter != 0:
            eu_recall = eu_tweet_counter_correct / eu_tweet_counter
        writeFile.write("EU: " + str(eu_tweet_counter_correct) + "/" + str(eu_tweet_counter) + " =  ~" + str(round(eu_recall * 100, 2)) + "%\n")

        if ca_tweet_counter != 0:
            ca_recall = ca_tweet_counter_correct / ca_tweet_counter
        writeFile.write("CA: " + str(ca_tweet_counter_correct) + "/" + str(ca_tweet_counter) + " =  ~" + str(round(ca_recall * 100, 2)) + "%\n")

        if gl_tweet_counter != 0:
            gl_recall = gl_tweet_counter_correct / gl_tweet_counter
        writeFile.write("GL: " + str(gl_tweet_counter_correct) + "/" + str(gl_tweet_counter) + " =  ~" + str(round(gl_recall * 100, 2)) + "%\n")

        if es_tweet_counter != 0:
            es_recall = es_tweet_counter_correct / es_tweet_counter
        writeFile.write("ES: " + str(es_tweet_counter_correct) + "/" + str(es_tweet_counter) + " =  ~" + str(round(es_recall * 100, 2)) + "%\n")

        if en_tweet_counter != 0:
            en_recall = en_tweet_counter_correct / en_tweet_counter
        writeFile.write("EN: " + str(en_tweet_counter_correct) + "/" + str(en_tweet_counter) + " =  ~" + str(round(en_recall * 100, 2)) + "%\n")

        if pt_tweet_counter != 0:
            pt_recall = pt_tweet_counter_correct / pt_tweet_counter
        writeFile.write("PT: " + str(pt_tweet_counter_correct) + "/" + str(pt_tweet_counter) + " =  ~" + str(round(pt_recall * 100, 2)) + "%\n")

        writeFile.write('\n')

        # F1-measure = 2PR/P+R

        eu_F1 = 0
        ca_F1 = 0
        gl_F1 = 0
        es_F1 = 0
        en_F1 = 0
        pt_F1 = 0

        if eu_precision + eu_recall != 0:
            eu_F1 = (2 * eu_precision * eu_recall) / (eu_precision + eu_recall)
        if ca_precision + ca_recall != 0:
            ca_F1 = (2 * ca_precision * ca_recall) / (ca_precision + ca_recall)
        if gl_precision + gl_recall != 0:
            gl_F1 = (2 * gl_precision * gl_recall) / (gl_precision + gl_recall)
        if es_precision + es_recall != 0:
            es_F1 = (2 * es_precision * es_recall) / (es_precision + es_recall)
        if en_precision + en_recall != 0:
            en_F1 = (2 * en_precision * en_recall) / (en_precision + en_recall)
        if pt_precision + pt_recall != 0:
            pt_F1 = (2 * pt_precision * pt_recall) / (pt_precision + pt_recall)

        writeFile.write("F1-measure:\n")

        writeFile.write("EU: ~" + str(round(eu_recall * 100, 2)) + "%\n")
        writeFile.write("CA: ~" + str(round(ca_recall * 100, 2)) + "%\n")
        writeFile.write("GL: ~" + str(round(gl_recall * 100, 2)) + "%\n")
        writeFile.write("ES: ~" + str(round(es_recall * 100, 2)) + "%\n")
        writeFile.write("EN: ~" + str(round(en_recall * 100, 2)) + "%\n")
        writeFile.write("PT: ~" + str(round(pt_recall * 100, 2)) + "%\n")

        writeFile.write('\n')

        # Average Precision

        average_precision = (eu_precision + ca_precision + gl_precision + es_precision + en_precision + pt_precision) / 6

        writeFile.write("Average Precision:\n")
        writeFile.write("~" + str(round(average_precision * 100, 2)) + "%\n")

        writeFile.write('\n')

        # Average Precision

        average_recall = (eu_recall + ca_recall + gl_recall + es_recall + en_recall + pt_recall) / 6

        writeFile.write("Average Recall:\n")
        writeFile.write("~" + str(round(average_recall * 100, 2)) + "%\n")

        writeFile.write('\n')

        # Average F1-measure

        average_F1 = (eu_F1 + ca_F1 + gl_F1 + es_F1 + en_F1 + pt_F1) / 6

        writeFile.write("Average F1-measure:\n")
        writeFile.write("~" + str(round(average_F1 * 100, 2)) + "%\n")

        writeFile.write('\n')

        # Weighted Average Precision

        weighted_average_precision = (eu_tweet_counter * eu_precision + ca_tweet_counter * ca_precision + gl_tweet_counter * gl_precision + es_tweet_counter * es_precision + en_tweet_counter * en_precision + pt_tweet_counter * pt_precision) / tweetCounter

        writeFile.write("Weighted Precision:\n")
        writeFile.write("~" + str(round(weighted_average_precision * 100, 2)) + "%\n")

        writeFile.write('\n')

        # Weighted Average Precision

        weighted_average_recall = (eu_tweet_counter * eu_recall + ca_tweet_counter * ca_recall + gl_tweet_counter * gl_recall + es_tweet_counter * es_recall + en_tweet_counter * en_recall + pt_tweet_counter * pt_recall) / tweetCounter

        writeFile.write("Weighted Recall:\n")
        writeFile.write("~" + str(round(weighted_average_recall * 100, 2)) + "%\n")

        writeFile.write('\n')

        # Weighted Average F1-measure

        weighted_average_F1 = (eu_tweet_counter * eu_F1 + ca_tweet_counter * ca_F1 + gl_tweet_counter * gl_F1 + es_tweet_counter * es_F1 + en_tweet_counter * en_F1 + pt_tweet_counter * pt_F1) / tweetCounter

        writeFile.write("Weighted F1-measure:\n")
        writeFile.write("~" + str(round(weighted_average_F1 * 100, 2)) + "%\n")

        writeFile.close()


# MAIN

# Vocabulary 0, a-z lowercase
voc0 = []
voc0.append('a')
voc0.append('b')
voc0.append('c')
voc0.append('d')
voc0.append('e')
voc0.append('f')
voc0.append('g')
voc0.append('h')
voc0.append('i')
voc0.append('j')
voc0.append('k')
voc0.append('l')
voc0.append('m')
voc0.append('n')
voc0.append('o')
voc0.append('p')
voc0.append('q')
voc0.append('r')
voc0.append('s')
voc0.append('t')
voc0.append('u')
voc0.append('v')
voc0.append('w')
voc0.append('x')
voc0.append('y')
voc0.append('z')

voc1 = []
voc1.append('a')
voc1.append('b')
voc1.append('c')
voc1.append('d')
voc1.append('e')
voc1.append('f')
voc1.append('g')
voc1.append('h')
voc1.append('i')
voc1.append('j')
voc1.append('k')
voc1.append('l')
voc1.append('m')
voc1.append('n')
voc1.append('o')
voc1.append('p')
voc1.append('q')
voc1.append('r')
voc1.append('s')
voc1.append('t')
voc1.append('u')
voc1.append('v')
voc1.append('w')
voc1.append('x')
voc1.append('y')
voc1.append('z')
voc1.append('A')
voc1.append('B')
voc1.append('C')
voc1.append('D')
voc1.append('E')
voc1.append('F')
voc1.append('G')
voc1.append('H')
voc1.append('I')
voc1.append('J')
voc1.append('K')
voc1.append('L')
voc1.append('M')
voc1.append('N')
voc1.append('O')
voc1.append('P')
voc1.append('Q')
voc1.append('R')
voc1.append('S')
voc1.append('T')
voc1.append('U')
voc1.append('V')
voc1.append('W')
voc1.append('X')
voc1.append('Y')
voc1.append('Z')

path = './'
trainFileName = 'training-tweets'
testFileName = 'test-tweets-given'

AI_one = AI()

AI_one_vocList = voc0
AI_one_vocInt = 0
AI_one_nGramInt = 1
AI_one_smoothingValue = 0.5

AI_one.train(path, trainFileName, AI_one_vocList, AI_one_vocInt, AI_one_nGramInt)
AI_one.scoreFile(path, testFileName , AI_one_vocInt, AI_one_nGramInt, AI_one_smoothingValue)
