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

# create class

class AI:
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
