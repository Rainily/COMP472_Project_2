import math
# v = 0 , a-z lowercase
# n-gram size = 1

# eu
voc0size1_eu = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}

# ca
voc0size1_ca = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}

# gl
voc0size1_gl = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}

# es
voc0size1_es = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}

# en
voc0size1_en = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}

# pt
voc0size1_pt = {
	'a': 0,
	'b': 0,
	'c': 0,
	'd': 0,
	'e': 0,
	'f': 0,
	'g': 0,
	'h': 0,
	'i': 0,
	'j': 0,
	'k': 0,
	'l': 0,
	'm': 0,
	'n': 0,
	'o': 0,
	'p': 0,
	'q': 0,
	'r': 0,
	's': 0,
	't': 0,
	'u': 0,
	'v': 0,
	'w': 0,
	'x': 0,
	'y': 0,
	'z': 0
}

# DYNAMIC GENERATION

# Vocabulary 0, a-z lowercase
alphabetListVoc0 = []

alphabetListVoc0.append('a')
alphabetListVoc0.append('b')
alphabetListVoc0.append('c')
alphabetListVoc0.append('d')
alphabetListVoc0.append('e')
alphabetListVoc0.append('f')
alphabetListVoc0.append('g')
alphabetListVoc0.append('h')
alphabetListVoc0.append('i')
alphabetListVoc0.append('j')
alphabetListVoc0.append('k')
alphabetListVoc0.append('l')
alphabetListVoc0.append('m')
alphabetListVoc0.append('n')
alphabetListVoc0.append('o')
alphabetListVoc0.append('p')
alphabetListVoc0.append('q')
alphabetListVoc0.append('r')
alphabetListVoc0.append('s')
alphabetListVoc0.append('t')
alphabetListVoc0.append('u')
alphabetListVoc0.append('v')
alphabetListVoc0.append('w')
alphabetListVoc0.append('x')
alphabetListVoc0.append('y')
alphabetListVoc0.append('z')

def createBigramDictionary(vocabularyList):

	temporaryDictionary = {}

	for x in range(len(vocabularyList)):
		for y in range(len(vocabularyList)):
			keyName = vocabularyList[x] + vocabularyList[y]
			temporaryDictionary[keyName] = 0

	return temporaryDictionary

def createTrigramDictionary(vocabularyList):
	
	temporaryDictionary = {}

	for x in range(len(vocabularyList)):
		for y in range(len(vocabularyList)):
			for z in range(len(vocabularyList)):
				keyName = vocabularyList[x] + vocabularyList[y] + vocabularyList[z] 
				temporaryDictionary[keyName] = 0

<<<<<<< Updated upstream
	return temporaryDictionary

voc0size2_eu = createBigramDictionary(alphabetListVoc0)
voc0size2_ca = createBigramDictionary(alphabetListVoc0)
voc0size2_gl = createBigramDictionary(alphabetListVoc0)
voc0size2_es = createBigramDictionary(alphabetListVoc0)
voc0size2_en = createBigramDictionary(alphabetListVoc0)
voc0size2_pt = createBigramDictionary(alphabetListVoc0)
voc0size3_eu = createTrigramDictionary(alphabetListVoc0)
voc0size3_ca = createTrigramDictionary(alphabetListVoc0)
voc0size3_gl = createTrigramDictionary(alphabetListVoc0)
voc0size3_es = createTrigramDictionary(alphabetListVoc0)
voc0size3_en = createTrigramDictionary(alphabetListVoc0)
voc0size3_pt = createTrigramDictionary(alphabetListVoc0)
=======
    return temporaryDictionary
>>>>>>> Stashed changes

# create class

class AI:
<<<<<<< Updated upstream
	def __init__(self):
		self.characterCounterEU = 0 # total number of EU characters scanned
		self.characterCounterCA = 0 # total number of CA characters scanned
		self.characterCounterGL = 0 # total number of GL characters scanned
		self.characterCounterES = 0 # total number of ES characters scanned
		self.characterCounterEN = 0 # total number of EN characters scanned
		self.characterCounterPT = 0 # total number of PT characters scanned
		self.characterCounterTotal = 0

		# testTweet = 'blah blah blah'
	def score(self, tweet, vocInt, nGramInt, smoothingValue):
		if nGramInt == 1:


			# initialize the scores to their respective probabilities, P(eu), P(ca), etc...
			eu_score = math.log(self.characterCounterEU / self.characterCounterTotal) # P(eu)
			ca_score = math.log(self.characterCounterCA / self.characterCounterTotal)
			gl_score = math.log(self.characterCounterGL / self.characterCounterTotal)
			es_score = math.log(self.characterCounterES / self.characterCounterTotal)
			en_score = math.log(self.characterCounterEN / self.characterCounterTotal)
			pt_score = math.log(self.characterCounterPT / self.characterCounterTotal)
			
			for k in voc0size1_eu.keys():
				voc0size1_eu[k] += smoothingValue
				voc0size1_ca[k] += smoothingValue
				voc0size1_gl[k] += smoothingValue
				voc0size1_es[k] += smoothingValue
				voc0size1_en[k] += smoothingValue
				voc0size1_pt[k] += smoothingValue

			self.characterCounterEU += len(voc0size1_eu) * smoothingValue
			self.characterCounterCA += len(voc0size1_ca) * smoothingValue
			self.characterCounterGL += len(voc0size1_gl) * smoothingValue
			self.characterCounterES += len(voc0size1_es) * smoothingValue
			self.characterCounterEN += len(voc0size1_en) * smoothingValue
			self.characterCounterPT += len(voc0size1_pt) * smoothingValue

			for x in range(len(tweet)):
				# update the scores if the character is in the vocabulary
				for k in voc0size1_eu.keys():
					if tweet[x] == k:
						eu_score *= math.log(voc0size1_eu[k] / self.characterCounterEU) # multiply by P(character | eu)
						ca_score *= math.log(voc0size1_ca[k] / self.characterCounterCA) # multiply by P(character | ca)
						gl_score *= math.log(voc0size1_gl[k] / self.characterCounterGL) # multiply by P(character | gl)
						es_score *= math.log(voc0size1_es[k] / self.characterCounterES) # multiply by P(character | es)
						en_score *= math.log(voc0size1_en[k] / self.characterCounterEN) # multiply by P(character | en)
						pt_score *= math.log(voc0size1_pt[k] / self.characterCounterPT) # multiply by P(character | pt)

			# show scores
			print("EU SCORE:" + str(eu_score))
			print("CA SCORE:" + str(ca_score))
			print("GL SCORE:" + str(gl_score))
			print("ES SCORE:" + str(es_score))
			print("EN SCORE:" + str(en_score))
			print("PT SCORE:" + str(pt_score))

		elif nGramInt == 2:
			# for vocInt = 0 and nGramInt = 1

			# index of the character we're scanning in the tweet
			firstDigitIndex = 0
			secondDigitIndex = 1

			print(self.characterCounterEN)
			print(self.characterCounterCA)
			print(self.characterCounterGL)
			print(self.characterCounterES)
			print(self.characterCounterEN)
			print(self.characterCounterPT)

			# initialize the scores to their respective probabilities, P(eu), P(ca), etc...
			eu_score = math.log(self.characterCounterEU / self.characterCounterTotal)
			ca_score = math.log(self.characterCounterCA / self.characterCounterTotal)
			gl_score = math.log(self.characterCounterGL / self.characterCounterTotal)
			es_score = math.log(self.characterCounterES / self.characterCounterTotal)
			en_score = math.log(self.characterCounterEN / self.characterCounterTotal)
			pt_score = math.log(self.characterCounterPT / self.characterCounterTotal)

			for x in range(len(tweet) - 1):

				for k in voc0size2_eu.keys():
					voc0size2_eu[k] += smoothingValue
					voc0size2_ca[k] += smoothingValue
					voc0size2_gl[k] += smoothingValue
					voc0size2_es[k] += smoothingValue
					voc0size2_en[k] += smoothingValue
					voc0size2_pt[k] += smoothingValue

				self.characterCounterEU += len(voc0size2_eu) * smoothingValue
				self.characterCounterCA += len(voc0size2_ca) * smoothingValue
				self.characterCounterGL += len(voc0size2_gl) * smoothingValue
				self.characterCounterES += len(voc0size2_es) * smoothingValue
				self.characterCounterEN += len(voc0size2_en) * smoothingValue
				self.characterCounterPT += len(voc0size2_pt) * smoothingValue

				# update the scores if the character is in the vocabulary
				for k in voc0size1_eu.keys():
					if tweet[firstDigitIndex] + tweet[secondDigitIndex] == k:
						eu_score *= math.log(voc0size2_eu[k] / self.characterCounterEU) # multiply by P(character | eu)
						ca_score *= math.log(voc0size2_ca[k] / self.characterCounterCA) # multiply by P(character | ca)
						gl_score *= math.log(voc0size2_gl[k] / self.characterCounterGL) # multiply by P(character | gl)
						es_score *= math.log(voc0size2_es[k] / self.characterCounterES) # multiply by P(character | es)
						en_score *= math.log(voc0size2_en[k] / self.characterCounterEN) # multiply by P(character | en)
						pt_score *= math.log(voc0size2_pt[k] / self.characterCounterPT) # multiply by P(character | pt)
						firstDigitIndex += 1
						secondDigitIndex += 1

		elif nGramInt == 3:
			# for vocInt = 0 and nGramInt = 1

			# index of the character we're scanning in the tweet
			firstDigitIndex = 0
			secondDigitIndex = 1
			thirdDigitIndex = 2

			print(self.characterCounterEN)
			print(self.characterCounterCA)
			print(self.characterCounterGL)
			print(self.characterCounterES)
			print(self.characterCounterEN)
			print(self.characterCounterPT)

			# initialize the scores to their respective probabilities, P(eu), P(ca), etc...
			eu_score = math.log(self.characterCounterEU / self.characterCounterTotal)
			ca_score = math.log(self.characterCounterCA / self.characterCounterTotal)
			gl_score = math.log(self.characterCounterGL / self.characterCounterTotal)
			es_score = math.log(self.characterCounterES / self.characterCounterTotal)
			en_score = math.log(self.characterCounterEN / self.characterCounterTotal)
			pt_score = math.log(self.characterCounterPT / self.characterCounterTotal)

			for x in range(len(tweet) - 1):

				for k in voc0size3_eu.keys():
					voc0size3_eu[k] += smoothingValue
					voc0size3_ca[k] += smoothingValue
					voc0size3_gl[k] += smoothingValue
					voc0size3_es[k] += smoothingValue
					voc0size3_en[k] += smoothingValue
					voc0size3_pt[k] += smoothingValue

				self.characterCounterEU += len(voc0size3_eu) * smoothingValue
				self.characterCounterCA += len(voc0size3_ca) * smoothingValue
				self.characterCounterGL += len(voc0size3_gl) * smoothingValue
				self.characterCounterES += len(voc0size3_es) * smoothingValue
				self.characterCounterEN += len(voc0size3_en) * smoothingValue
				self.characterCounterPT += len(voc0size3_pt) * smoothingValue

				# update the scores if the character is in the vocabulary
				for k in voc0size3_eu.keys():
					if tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex] == k:
						eu_score *= math.log(voc0size3_eu[k] / self.characterCounterEU) # multiply by P(character | eu)
						ca_score *= math.log(voc0size3_ca[k] / self.characterCounterCA) # multiply by P(character | ca)
						gl_score *= math.log(voc0size3_gl[k] / self.characterCounterGL) # multiply by P(character | gl)
						es_score *= math.log(voc0size3_es[k] / self.characterCounterES) # multiply by P(character | es)
						en_score *= math.log(voc0size3_en[k] / self.characterCounterEN) # multiply by P(character | en)
						pt_score *= math.log(voc0size3_pt[k] / self.characterCounterPT) # multiply by P(character | pt)
						firstDigitIndex += 1
						secondDigitIndex += 1
						thirdDigitIndex += 1

			# show scores
			print("EU SCORE:" + str(eu_score))
			print("CA SCORE:" + str(ca_score))
			print("GL SCORE:" + str(gl_score))
			print("ES SCORE:" + str(es_score))
			print("EN SCORE:" + str(en_score))
			print("PT SCORE:" + str(pt_score))

	def train(self, path, fileName, nGramInt):
		p = path # path to the folder with input files
		f = fileName + '.txt' # the name of input file
		fullPath = p + f # full path

		tweetID =  ''
		userID = ''
		language = ''
		tweet = ''

		counter = 0

		lineCounter = 0

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
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterEU += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)
							for k in voc0size1_eu.keys(): 
								if tweet[x] == k:
									voc0size1_eu[k] += 1
					elif language == 'ca':
						
						tweetLength = len(tweet)

						for x in range(0, tweetLength):
							self.characterCounterTotal += 1
							self.characterCounterCA += 1
							for k in voc0size1_ca.keys():
								if tweet[x] == k:
									voc0size1_ca[k] += 1
					elif language == 'gl':
						
						tweetLength = len(tweet)

						for x in range(0, tweetLength):
							self.characterCounterTotal += 1
							self.characterCounterGL += 1
							for k in voc0size1_gl.keys():
								if tweet[x] == k:
									voc0size1_gl[k] += 1
					elif language == 'es':

						tweetLength = len(tweet)

						for x in range(0, tweetLength):
							self.characterCounterTotal += 1
							self.characterCounterES += 1
							for k in voc0size1_es.keys():
								if tweet[x] == k:
									voc0size1_es[k] += 1
					elif language == 'en':
						
						tweetLength = len(tweet)

						for x in range(0, tweetLength):
							self.characterCounterTotal += 1
							self.characterCounterEN += 1
							for k in voc0size1_en.keys():
								if tweet[x] == k:
									voc0size1_en[k] += 1
					elif language == 'pt':
						
						tweetLength = len(tweet)

						for x in range(0, tweetLength):
							self.characterCounterTotal += 1
							self.characterCounterPT += 1
							for k in voc0size1_pt.keys():
								if tweet[x] == k:
									voc0size1_pt[k] += 1
		elif nGramInt == 2:
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
					if language == 'eu':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterEU += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
							for k in voc0size2_eu.keys(): 
								if currentSubdivision == k:
									voc0size2_eu[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
					elif language == 'ca':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterCA += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
							for k in voc0size2_ca.keys(): 
								if currentSubdivision == k:
									voc0size2_ca[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
					elif language == 'gl':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterGL += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
							for k in voc0size2_gl.keys(): 
								if currentSubdivision == k:
									voc0size2_gl[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
					elif language == 'es':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterES += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
							for k in voc0size2_es.keys():
								if currentSubdivision == k:
									voc0size2_es[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
					elif language == 'en':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterEN += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
							for k in voc0size2_en.keys(): 
								if currentSubdivision == k:
									voc0size2_en[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
					elif language == 'pt':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterPT += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
							for k in voc0size2_pt.keys(): 
								if currentSubdivision == k:
									voc0size2_pt[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
					lineCounter += 1

		elif nGramInt == 3:
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
					if language == 'eu':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterEU += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
							
							# Breaks when Third Digit reaches length of tweet
							if(thirdDigitIndex==tweetLength-1):
								break

							for k in voc0size3_eu.keys(): 
								if currentSubdivision == k:
									voc0size3_eu[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
							thirdDigitIndex += 1
					elif language == 'ca':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterCA += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]

							# Breaks when Third Digit reaches length of tweet
							if(thirdDigitIndex==tweetLength-1):
								break
							
							for k in voc0size3_ca.keys(): 
								if currentSubdivision == k:
									voc0size3_ca[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
							thirdDigitIndex += 1
					elif language == 'gl':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterGL += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
							
							# Breaks when Third Digit reaches length of tweet
							if(thirdDigitIndex==tweetLength-1):
								break
							
							for k in voc0size3_gl.keys(): 
								if currentSubdivision == k:
									voc0size3_gl[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
							thirdDigitIndex += 1
					elif language == 'es':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterES += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
							
							# Breaks when Third Digit reaches length of tweet
							if(thirdDigitIndex==tweetLength-1):
								break
							
							for k in voc0size3_es.keys():
								if currentSubdivision == k:
									voc0size3_es[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
							thirdDigitIndex += 1
					elif language == 'en':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterEN += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
							
							# Breaks when Third Digit reaches length of tweet
							if(thirdDigitIndex==tweetLength-1):
								break
							
							for k in voc0size3_en.keys(): 
								if currentSubdivision == k:
									voc0size3_en[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
							thirdDigitIndex += 1
					elif language == 'pt':
						tweetLength = len(tweet) # length of the tweet being scanned
						# iterate through each character in the tweet
						for x in range(0, tweetLength - 1):
							self.characterCounterTotal += 1 # increment total characters scanned
							self.characterCounterPT += 1 # increment total EU characters scanned
							# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

							currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
							
							# Breaks when Third Digit reaches length of tweet
							if(thirdDigitIndex==tweetLength-1):
								break
							
							for k in voc0size3_pt.keys(): 
								if currentSubdivision == k:
									voc0size3_pt[k] += 1
							firstDigitIndex += 1
							secondDigitIndex += 1
							thirdDigitIndex += 1
					lineCounter += 1

					print()
					print(lineCounter)
					print()

					print("------------------------")
					print(self.characterCounterEN)
					print(self.characterCounterCA)
					print(self.characterCounterGL)
					print(self.characterCounterES)
					print(self.characterCounterEN)
					print(self.characterCounterPT)
					print(self.characterCounterTotal)
		# test score function with example tweet
		tweetEx1 = "bainan etzaite otoi nitaz betiko agurtu".lower()
		self.score(tweetEx1, 0, nGramInt, 0.5)


# main
AI_one = AI()
AI_one.train('./', 'training-tweets-half2', 3)
=======
    def __init__(self):
        self.characterCounterEU = 0 # total number of EU characters scanned
        self.characterCounterCA = 0 # total number of CA characters scanned
        self.characterCounterGL = 0 # total number of GL characters scanned
        self.characterCounterES = 0 # total number of ES characters scanned
        self.characterCounterEN = 0 # total number of EN characters scanned
        self.characterCounterPT = 0 # total number of PT characters scanned
        self.characterCounterTotal = 0
        self.eu_table = {}
        self.ca_table = {}
        self.gl_table = {}
        self.es_table = {}
        self.en_table = {}
        self.pt_table = {}

        # testTweet = 'blah blah blah'
    def score(self, tweet, vocInt, nGramInt, smoothingValue):
        if nGramInt == 1:


            # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
            eu_score = math.log(self.characterCounterEU / self.characterCounterTotal) # P(eu)
            ca_score = math.log(self.characterCounterCA / self.characterCounterTotal)
            gl_score = math.log(self.characterCounterGL / self.characterCounterTotal)
            es_score = math.log(self.characterCounterES / self.characterCounterTotal)
            en_score = math.log(self.characterCounterEN / self.characterCounterTotal)
            pt_score = math.log(self.characterCounterPT / self.characterCounterTotal)
            
            for k in self.eu_table.keys():
                self.eu_table[k] += smoothingValue
                self.ca_table[k] += smoothingValue
                self.gl_table[k] += smoothingValue
                self.es_table[k] += smoothingValue
                self.en_table[k] += smoothingValue
                self.pt_table[k] += smoothingValue

            self.characterCounterEU += len(self.eu_table) * smoothingValue
            self.characterCounterCA += len(self.ca_table) * smoothingValue
            self.characterCounterGL += len(self.gl_table) * smoothingValue
            self.characterCounterES += len(self.es_table) * smoothingValue
            self.characterCounterEN += len(self.en_table) * smoothingValue
            self.characterCounterPT += len(self.pt_table) * smoothingValue

            for x in range(len(tweet)):
                # update the scores if the character is in the vocabulary
                for k in self.eu_table.keys():
                    if tweet[x] == k:
                        eu_score *= math.log(self.eu_table[k] / self.characterCounterEU) # multiply by P(character | eu)
                        ca_score *= math.log(self.ca_table[k] / self.characterCounterCA) # multiply by P(character | ca)
                        gl_score *= math.log(self.gl_table[k] / self.characterCounterGL) # multiply by P(character | gl)
                        es_score *= math.log(self.es_table[k] / self.characterCounterES) # multiply by P(character | es)
                        en_score *= math.log(self.en_table[k] / self.characterCounterEN) # multiply by P(character | en)
                        pt_score *= math.log(self.pt_table[k] / self.characterCounterPT) # multiply by P(character | pt)

            # show scores
            '''
            print("EU SCORE:" + str(eu_score))
            print("CA SCORE:" + str(ca_score))
            print("GL SCORE:" + str(gl_score))
            print("ES SCORE:" + str(es_score))
            print("EN SCORE:" + str(en_score))
            print("PT SCORE:" + str(pt_score))
            '''

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

            return answer, biggestValue, vocInt, smoothingValue




        elif nGramInt == 2:
            # for vocInt = 0 and nGramInt = 1

            # index of the character we're scanning in the tweet
            firstDigitIndex = 0
            secondDigitIndex = 1

            # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
            eu_score = math.log(self.characterCounterEU / self.characterCounterTotal)
            ca_score = math.log(self.characterCounterCA / self.characterCounterTotal)
            gl_score = math.log(self.characterCounterGL / self.characterCounterTotal)
            es_score = math.log(self.characterCounterES / self.characterCounterTotal)
            en_score = math.log(self.characterCounterEN / self.characterCounterTotal)
            pt_score = math.log(self.characterCounterPT / self.characterCounterTotal)

            for x in range(len(tweet) - 1):

                for k in self.eu_table.keys():
                    self.eu_table[k] += smoothingValue
                    self.ca_table[k] += smoothingValue
                    self.gl_table[k] += smoothingValue
                    self.es_table[k] += smoothingValue
                    self.en_table[k] += smoothingValue
                    self.pt_table[k] += smoothingValue

                self.characterCounterEU += len(self.eu_table) * smoothingValue
                self.characterCounterCA += len(self.ca_table) * smoothingValue
                self.characterCounterGL += len(self.gl_table) * smoothingValue
                self.characterCounterES += len(self.es_table) * smoothingValue
                self.characterCounterEN += len(self.en_table) * smoothingValue
                self.characterCounterPT += len(self.pt_table) * smoothingValue

                # update the scores if the character is in the vocabulary
                for k in self.eu_table.keys():
                    if tweet[firstDigitIndex] + tweet[secondDigitIndex] == k:
                        eu_score *= math.log(self.eu_table[k] / self.characterCounterEU) # multiply by P(character | eu)
                        ca_score *= math.log(self.ca_table[k] / self.characterCounterCA) # multiply by P(character | ca)
                        gl_score *= math.log(self.gl_table[k] / self.characterCounterGL) # multiply by P(character | gl)
                        es_score *= math.log(self.es_table[k] / self.characterCounterES) # multiply by P(character | es)
                        en_score *= math.log(self.en_table[k] / self.characterCounterEN) # multiply by P(character | en)
                        pt_score *= math.log(self.pt_table[k] / self.characterCounterPT) # multiply by P(character | pt)
                        firstDigitIndex += 1
                        secondDigitIndex += 1


            # show scores
            '''
            print("EU SCORE:" + str(eu_score))
            print("CA SCORE:" + str(ca_score))
            print("GL SCORE:" + str(gl_score))
            print("ES SCORE:" + str(es_score))
            print("EN SCORE:" + str(en_score))
            print("PT SCORE:" + str(pt_score))
            '''

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

            return answer, biggestValue, vocInt, smoothingValue

        elif nGramInt == 3:
            # for vocInt = 0 and nGramInt = 1

            # index of the character we're scanning in the tweet
            firstDigitIndex = 0
            secondDigitIndex = 1
            thirdDigitIndex = 2

            # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
            eu_score = math.log(self.characterCounterEU / self.characterCounterTotal)
            ca_score = math.log(self.characterCounterCA / self.characterCounterTotal)
            gl_score = math.log(self.characterCounterGL / self.characterCounterTotal)
            es_score = math.log(self.characterCounterES / self.characterCounterTotal)
            en_score = math.log(self.characterCounterEN / self.characterCounterTotal)
            pt_score = math.log(self.characterCounterPT / self.characterCounterTotal)

            for x in range(len(tweet) - 1):

                for k in eu_table.keys():
                    eu_table[k] += smoothingValue
                    ca_table[k] += smoothingValue
                    gl_table[k] += smoothingValue
                    es_table[k] += smoothingValue
                    en_table[k] += smoothingValue
                    pt_table[k] += smoothingValue

                self.characterCounterEU += len(eu_table) * smoothingValue
                self.characterCounterCA += len(ca_table) * smoothingValue
                self.characterCounterGL += len(gl_table) * smoothingValue
                self.characterCounterES += len(es_table) * smoothingValue
                self.characterCounterEN += len(en_table) * smoothingValue
                self.characterCounterPT += len(pt_table) * smoothingValue

                # update the scores if the character is in the vocabulary
                # na
                for k in eu_table.keys():
                    if tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex] == k:
                        eu_score *= math.log(eu_table[k] / self.characterCounterEU) # multiply by P(character | eu)
                        ca_score *= math.log(ca_table[k] / self.characterCounterCA) # multiply by P(character | ca)
                        gl_score *= math.log(gl_table[k] / self.characterCounterGL) # multiply by P(character | gl)
                        es_score *= math.log(es_table[k] / self.characterCounterES) # multiply by P(character | es)
                        en_score *= math.log(en_table[k] / self.characterCounterEN) # multiply by P(character | en)
                        pt_score *= math.log(pt_table[k] / self.characterCounterPT) # multiply by P(character | pt)
                        firstDigitIndex += 1
                        secondDigitIndex += 1
                        thirdDigitIndex += 1


            # show scores
            '''
            print("EU SCORE:" + str(eu_score))
            print("CA SCORE:" + str(ca_score))
            print("GL SCORE:" + str(gl_score))
            print("ES SCORE:" + str(es_score))
            print("EN SCORE:" + str(en_score))
            print("PT SCORE:" + str(pt_score))
            '''

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

            return answer, biggestValue, vocInt, smoothingValue


    def train(self, path, fileName, vocInt, nGramInt):
        p = path # path to the folder with input files
        f = fileName + '.txt' # the name of input file
        fullPath = p + f # full path

        tweetID =  ''
        userID = ''
        language = ''
        tweet = ''

        counter = 0

        euTrainingTweetNumber = 0
        caTrainingTweetNumber = 0
        glTrainingTweetNumber = 0
        esTrainingTweetNumber = 0
        enTrainingTweetNumber = 0
        ptTrainingTweetNumber = 0

        lineCounter = 0

        # Temporary Counter
        randomCounter = 0
        # vocabulary creation
        if nGramInt == 1:
            self.eu_table = createUnigramDictionary(alphabetListVoc0)
            self.ca_table = createUnigramDictionary(alphabetListVoc0)
            self.gl_table = createUnigramDictionary(alphabetListVoc0)
            self.es_table = createUnigramDictionary(alphabetListVoc0)
            self.en_table = createUnigramDictionary(alphabetListVoc0)
            self.pt_table = createUnigramDictionary(alphabetListVoc0)
        elif nGramInt == 2:
            self.eu_table = createBigramDictionary(alphabetListVoc0)
            self.ca_table = createBigramDictionary(alphabetListVoc0)
            self.gl_table = createBigramDictionary(alphabetListVoc0)
            self.es_table = createBigramDictionary(alphabetListVoc0)
            self.en_table = createBigramDictionary(alphabetListVoc0)
            self.pt_table = createBigramDictionary(alphabetListVoc0)
        elif nGramInt == 3:
            self.eu_table = createTrigramDictionary(alphabetListVoc0)
            self.ca_table = createTrigramDictionary(alphabetListVoc0)
            self.gl_table = createTrigramDictionary(alphabetListVoc0)
            self.es_table = createTrigramDictionary(alphabetListVoc0)
            self.en_table = createTrigramDictionary(alphabetListVoc0)
            self.pt_table = createTrigramDictionary(alphabetListVoc0)



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
                        euTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterEU += 1 # increment total EU characters scanned
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
                        caTrainingTweetNumber += 1
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            self.characterCounterTotal += 1
                            self.characterCounterCA += 1
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
                        glTrainingTweetNumber += 1
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            self.characterCounterTotal += 1
                            self.characterCounterGL += 1
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
                        esTrainingTweetNumber += 1
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            self.characterCounterTotal += 1
                            self.characterCounterES += 1
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
                        enTrainingTweetNumber += 1
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            self.characterCounterTotal += 1
                            self.characterCounterEN += 1
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
                        ptTrainingTweetNumber += 1
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
                            self.characterCounterTotal += 1
                            self.characterCounterPT += 1
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
                

        elif nGramInt == 2:
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
                    if language == 'eu':
                        euTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterEU += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
                            for k in self.eu_table.keys(): 
                                if currentSubdivision == k:
                                    self.eu_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[currentSubdivision] = 1
                                	self.ca_table[currentSubdivision] = 0
                                	self.gl_table[currentSubdivision] = 0
                                	self.es_table[currentSubdivision] = 0
                                	self.en_table[currentSubdivision] = 0
                                	self.pt_table[currentSubdivision] = 0
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'ca':
                        caTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterCA += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
                            for k in self.ca_table.keys(): 
                                if currentSubdivision == k:
                                    self.ca_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[currentSubdivision] = 0
                                	self.ca_table[currentSubdivision] = 1
                                	self.gl_table[currentSubdivision] = 0
                                	self.es_table[currentSubdivision] = 0
                                	self.en_table[currentSubdivision] = 0
                                	self.pt_table[currentSubdivision] = 0
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'gl':
                        glTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterGL += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
                            for k in self.gl_table.keys(): 
                                if currentSubdivision == k:
                                    self.gl_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[currentSubdivision] = 0
                                	self.ca_table[currentSubdivision] = 0
                                	self.gl_table[currentSubdivision] = 1
                                	self.es_table[currentSubdivision] = 0
                                	self.en_table[currentSubdivision] = 0
                                	self.pt_table[currentSubdivision] = 0
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'es':
                        esTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterES += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
                            for k in self.es_table.keys():
                                if currentSubdivision == k:
                                    self.es_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[currentSubdivision] = 0
                                	self.ca_table[currentSubdivision] = 0
                                	self.gl_table[currentSubdivision] = 0
                                	self.es_table[currentSubdivision] = 1
                                	self.en_table[currentSubdivision] = 0
                                	self.pt_table[currentSubdivision] = 0
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'en':
                        enTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterEN += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
                            for k in self.en_table.keys(): 
                                if currentSubdivision == k:
                                    self.en_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[currentSubdivision] = 0
                                	self.ca_table[currentSubdivision] = 0
                                	self.gl_table[currentSubdivision] = 0
                                	self.es_table[currentSubdivision] = 0
                                	self.en_table[currentSubdivision] = 1
                                	self.pt_table[currentSubdivision] = 0
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    elif language == 'pt':
                        ptTrainingTweetNumber += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterPT += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex]
                            for k in self.pt_table.keys(): 
                                if currentSubdivision == k:
                                    self.pt_table[k] += 1
                                    alreadyKey = True

                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[currentSubdivision] = 0
                                	self.ca_table[currentSubdivision] = 0
                                	self.gl_table[currentSubdivision] = 0
                                	self.es_table[currentSubdivision] = 0
                                	self.en_table[currentSubdivision] = 0
                                	self.pt_table[currentSubdivision] = 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                    lineCounter += 1

                    print()
                    print(lineCounter)
                    print()

                    print("------------------------")
                    print(self.characterCounterEN)
                    print(self.characterCounterCA)
                    print(self.characterCounterGL)
                    print(self.characterCounterES)
                    print(self.characterCounterEN)
                    print(self.characterCounterPT)
                    print(self.characterCounterTotal)

        elif nGramInt == 3:
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
                    if language == 'eu':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterEU += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
                            for k in eu_table.keys(): 
                                if currentSubdivision == k:
                                    eu_table[k] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    elif language == 'ca':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterCA += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
                            for k in ca_table.keys(): 
                                if currentSubdivision == k:
                                    ca_table[k] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    elif language == 'gl':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterGL += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
                            for k in gl_table.keys(): 
                                if currentSubdivision == k:
                                    gl_table[k] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    elif language == 'es':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterES += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
                            for k in es_table.keys(): 
                                if currentSubdivision == k:
                                    es_table[k] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    elif language == 'en':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterEN += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
                            for k in en_table.keys(): 
                                if currentSubdivision == k:
                                    en_table[k] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    elif language == 'pt':
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength - 2):
                            self.characterCounterTotal += 1 # increment total characters scanned
                            self.characterCounterPT += 1 # increment total EU characters scanned
                            # test all keys of the respective dictionary (count all the n-grams in the current vocabulary)

                            currentSubdivision = tweet[firstDigitIndex] + tweet[secondDigitIndex] + tweet[thirdDigitIndex]
                            for k in pt_table.keys(): 
                                if currentSubdivision == k:
                                    pt_table[k] += 1
                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1
                    lineCounter += 1

                    # print()
                    # print(lineCounter)
                    # print()

                    # print("------------------------")
                    # print(self.characterCounterEN)
                    # print(self.characterCounterCA)
                    # print(self.characterCounterGL)
                    # print(self.characterCounterES)
                    # print(self.characterCounterEN)
                    # print(self.characterCounterPT)
                    # print(self.characterCounterTotal)


        #for k in es_table.keys(): 
        	#print(k + ":" + str(es_table[k]))
        print("tweet training:")
        print(euTrainingTweetNumber)
        print(caTrainingTweetNumber)
        print(glTrainingTweetNumber)
        print(esTrainingTweetNumber)
        print(enTrainingTweetNumber)
        print(ptTrainingTweetNumber)
        # test score function with example tweet
        # tweetEx1 = "@AnderDelPozo @PesqueWhite hahaha yo tambien me he quedao pillao ahahha".lower()
        self.scoreFile('./', 'test-tweets-given', nGramInt)


    def scoreFile (self, path, fileName, nGramInt):
        #Writing into the trace file for Unigram
        randomCounter = 0
        eu_tweet_counter = 0
        ca_tweet_counter = 0
        gl_tweet_counter = 0
        es_tweet_counter = 0
        en_tweet_counter = 0
        pt_tweet_counter = 0
        with open(path + "test-tweets-given.txt", encoding="utf8") as w:
             for line in w:
                 if randomCounter == 50:
                     break

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

                 guessedLanguage, guessedScore, vocInt, smoothingValue = self.score(word[3], 0, nGramInt, 0.5)
                 if guessedLanguage == word[2]:
                     correctOrNot = "Correct"
                 else:
                     correctOrNot = "Wrong"				
                
                 testPath ="trace_"+ str(vocInt) + "_"+ str(nGramInt)+ "_" + str(smoothingValue) + ".txt"
                 writeFile = open(testPath,"a+", encoding="utf8")
                 writeFile.write(word[0] + "  " + guessedLanguage + "  " + str(guessedScore) + "  " + word[2] + "  " + correctOrNot + "\n")
                 writeFile.close()
                
                 randomCounter += 1
                 '''
        print(eu_tweet_counter)
        print(ca_tweet_counter)
        print(gl_tweet_counter)
        print(es_tweet_counter)
        print(en_tweet_counter)
        print(pt_tweet_counter)
        '''
# main
AI_one = AI()
AI_one.train('./', 'training-tweets', 2, 2)
#AI_one.scoreFile('./', 'test-tweets-given', 2)

#Test





# p = path # path to the folder with input files
# 		f = fileName + '.txt' # the name of input file
# 		fullPath = p + f # full path

# 		tweetID =  ''
# 		userID = ''
# 		language = ''
# 		tweet = ''

# 		counter = 0
# 		lineCounter = 0
# 		rightCounter = 0

# 		randomCounter = 0

# 		# read the input file
# 		with open(fullPath, encoding="utf8") as f:
# 			# split every number in a line
# 			for line in f:
# 				# populate every variable
# 				if randomCounter == 10:
# 					break

# 				for word in line.split("\t"):
# 					if counter == 0:
# 						tweetID = word
# 						counter += 1 
# 					elif counter == 1:
# 						userID = word
# 						counter += 1
# 					elif counter == 2:
# 						language = word
# 						counter += 1
# 					else:
# 						tweet = word
# 						counter = 0

# 				testPath = "trace_0_"+str(nGramInt)+"_0.5.txt"
# 				answer, score = self.score(tweet, 0, nGramInt, 0.5).lower()

# 				if answer == language:
# 		 			correctOrNot = "Correct"
# 		 		else:
# 		 			correctOrNot = "Wrong"
                
# 				writeFile = open(testPath,"a+", encoding="utf8")
# 		 		writeFile.write(tweetID + "  " + answer + "  " + str(score) + "  " + language + "  " + correctOrNot + "\n")
# 		 		writeFile.close()
>>>>>>> Stashed changes
