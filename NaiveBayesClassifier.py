<<<<<<< Updated upstream
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
            
=======
'''
Reynald Servera - 40043437
Kenneth Serrano - 27056699
Patrick Chan - 26661025

Project 2 - Naive Bayes Classifier
April 5th, 2020
'''

import math
import time
import re

# Function to print sum 
def checkKey(dict, key): 
    if key in dict.keys(): 
        return True
    return False

# Removes unwanted parts of tweets
def removeRegEx(tweet):
    #remove digits
    copy = tweet
    copy = ''.join([i for i in copy if not i.isdigit()])

    #remove email
    email = re.compile('\w+@\w+\.[a-z]{3}')
    emailList = email.findall(copy)

    for i in emailList:
        copy = copy.replace(i, '')

    ltList = re.findall(r'&lt;', copy)

    for i in ltList:
        copy = copy.replace(i, '')

    #remove @userTags
    userNames = re.compile('@\w+\s')
    userNamesList = userNames.findall(copy)

    for i in userNamesList:
        copy = copy.replace(i, '')

    #remove url
    urlList = re.findall(r'(https?://[^\s]+)', copy)

    for i in urlList:
        copy = copy.replace(i, '')

    emojiAndSymbolList = re.findall(r'[^\w\s,]', copy)

    for i in emojiAndSymbolList:
        copy = copy.replace(i, '')

    return copy


# create a 1D dictionary from a vocabulary stored in a list
def createUnigramDictionary(vocabularyList):
    temporaryDictionary = {}

    for x in range(len(vocabularyList)):
        keyName = vocabularyList[x]
        temporaryDictionary[keyName] = 0

    return temporaryDictionary

# create a 2D dictionary from a vocabulary stored in a list
def createBigramDictionary(vocabularyList):

    temporaryDictionary = {}

    for x in range(len(vocabularyList)):
        temporaryDictionary[vocabularyList[x]] = {}
        for y in range(len(vocabularyList)):
            temporaryDictionary[vocabularyList[x]][vocabularyList[y]] = 0


    return temporaryDictionary

# create a 3D dictionary from a vocabulary stored in a list
def createTrigramDictionary(vocabularyList):
    
    temporaryDictionary = {}

    for x in range(len(vocabularyList)):
        temporaryDictionary[vocabularyList[x]] = {}
        for y in range(len(vocabularyList)):
            temporaryDictionary[vocabularyList[x]][vocabularyList[y]] = {}
            for z in range(len(vocabularyList)):
                temporaryDictionary[vocabularyList[x]][vocabularyList[y]][vocabularyList[z]] = 0

    return temporaryDictionary

# create class AI
class AI:
    def __init__(self):
        self.eu_table = {} # dictionary that stores eu n-gram frequencies
        self.ca_table = {} # dictionary that stores ca n-gram frequencies
        self.gl_table = {} # dictionary that stores gl n-gram frequencies
        self.es_table = {} # dictionary that stores es n-gram frequencies
        self.en_table = {} # dictionary that stores en n-gram frequencies
        self.pt_table = {} # dictionary that stores pt n-gram frequencies
        self.eu_tweet_counter = 0 # counts the number of eu training tweets
        self.ca_tweet_counter = 0 # counts the number of ca training tweets
        self.gl_tweet_counter = 0 # counts the number of gl training tweets
        self.es_tweet_counter = 0 # counts the number of es training tweets
        self.en_tweet_counter = 0 # counts the number of en training tweets
        self.pt_tweet_counter = 0 # counts the number of pt training tweets
        self.total_tweet_counter = 0  # counts the number of total training tweets

    # guesses a language of a given tweet by calculating the following for each language:
    # ex: "I like cake!"
    # Bigram
    # log(P(language)) + log(P(i|l) + log(P(k|i)) ... and so on
    #
    # take the biggest score
    def score(self, tweet, vocInt, nGramInt, smoothingValue):
        # for unigram
        if nGramInt == 1:

            digitIndex = 0 # index of the current character in the tweet

            eu_score = 0
            ca_score = 0
            gl_score = 0
            es_score = 0
            en_score = 0
            pt_score = 0

            # vocInt == 3 is our BYOM. In our BYOM, we do not consider the initial probability of the language log(P(language))
            if vocInt != 3:
                eu_score = math.log10(self.eu_tweet_counter/self.total_tweet_counter)
                ca_score = math.log10(self.ca_tweet_counter/self.total_tweet_counter)
                gl_score = math.log10(self.gl_tweet_counter/self.total_tweet_counter)
                es_score = math.log10(self.es_tweet_counter/self.total_tweet_counter)
                en_score = math.log10(self.en_tweet_counter/self.total_tweet_counter)
                pt_score = math.log10(self.pt_tweet_counter/self.total_tweet_counter)
            
            # apply smoothing to all frequency dictionaries
>>>>>>> Stashed changes
            for k in self.eu_table.keys():
                self.eu_table[k] += smoothingValue
                self.ca_table[k] += smoothingValue
                self.gl_table[k] += smoothingValue
                self.es_table[k] += smoothingValue
                self.en_table[k] += smoothingValue
                self.pt_table[k] += smoothingValue

<<<<<<< Updated upstream
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
=======
            # variables that will hold total number of ngrams in each language dictionary
            eu_totalCharacters = 0
            ca_totalCharacters = 0
            gl_totalCharacters = 0
            es_totalCharacters = 0
            en_totalCharacters = 0
            pt_totalCharacters = 0

            # count all the ngrams in each language dictionary
            for x in self.eu_table.keys():
                eu_totalCharacters += self.eu_table[x]
                ca_totalCharacters += self.ca_table[x]
                gl_totalCharacters += self.gl_table[x]
                es_totalCharacters += self.es_table[x]
                en_totalCharacters += self.en_table[x]
                pt_totalCharacters += self.pt_table[x]


            # for each language calculate the probability of the current character
            # score += log(P(x)), where x is a vocabulary character in the string 
            for y in range(len(tweet)):
                if checkKey(self.eu_table, tweet[digitIndex]):
                    eu_score += math.log10(self.eu_table[tweet[digitIndex]] / eu_totalCharacters) # multiply by P(character | eu)
                    ca_score += math.log10(self.ca_table[tweet[digitIndex]] / ca_totalCharacters) # multiply by P(character | eu)
                    gl_score += math.log10(self.gl_table[tweet[digitIndex]] / gl_totalCharacters) # multiply by P(character | eu)
                    es_score += math.log10(self.es_table[tweet[digitIndex]] / es_totalCharacters) # multiply by P(character | eu)
                    en_score += math.log10(self.en_table[tweet[digitIndex]] / en_totalCharacters) # multiply by P(character | eu)
                    pt_score += math.log10(self.pt_table[tweet[digitIndex]] / pt_totalCharacters) # multiply by P(character | eu)
                digitIndex += 1

            # return the biggest score out of all languages
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
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
=======
            return answer, biggestValue

        # for bigram
        elif nGramInt == 2:

            # indexes for two characters at a time
            firstDigitIndex = 0
            secondDigitIndex = 1

            # smooth every entry in the frequency dictionaries 
            for k in self.eu_table.keys():
                for l in self.eu_table.keys():
                    self.eu_table[k][l] += smoothingValue
                    self.ca_table[k][l] += smoothingValue
                    self.gl_table[k][l] += smoothingValue
                    self.es_table[k][l] += smoothingValue
                    self.en_table[k][l] += smoothingValue
                    self.pt_table[k][l] += smoothingValue

            eu_score = 0
            ca_score = 0
            gl_score = 0
            es_score = 0
            en_score = 0
            pt_score = 0

            # vocInt == 3 is our BYOM. In our BYOM, we do not consider the initial probability of the language log(P(language))
            if vocInt != 3:
                # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
                eu_score = math.log10(self.eu_tweet_counter/self.total_tweet_counter)
                ca_score = math.log10(self.ca_tweet_counter/self.total_tweet_counter)
                gl_score = math.log10(self.gl_tweet_counter/self.total_tweet_counter)
                es_score = math.log10(self.es_tweet_counter/self.total_tweet_counter)
                en_score = math.log10(self.en_tweet_counter/self.total_tweet_counter)
                pt_score = math.log10(self.pt_tweet_counter/self.total_tweet_counter)

            # for each language calculate the probability of two consecutive characters
            # score += log(P(x | y)), where x is a vocabulary character in the string and y is the previous character
            for y in range(len(tweet) - 1):
                if checkKey(self.eu_table, tweet[firstDigitIndex]):
                    if checkKey(self.eu_table, tweet[secondDigitIndex]):

                        firstCharacterTotal = 0
                        for x in self.eu_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.eu_table[tweet[firstDigitIndex]][x]
                        eu_score += math.log10(self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)
                        
                        firstCharacterTotal = 0
                        for x in self.ca_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.ca_table[tweet[firstDigitIndex]][x]
                        ca_score += math.log10(self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.gl_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.gl_table[tweet[firstDigitIndex]][x]
                        gl_score += math.log10(self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.es_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.es_table[tweet[firstDigitIndex]][x]
                        es_score += math.log10(self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.en_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.en_table[tweet[firstDigitIndex]][x]
                        en_score += math.log10(self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                        firstCharacterTotal = 0
                        for x in self.pt_table[tweet[firstDigitIndex]].keys():
                            firstCharacterTotal += self.pt_table[tweet[firstDigitIndex]][x]
                        pt_score += math.log10(self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]] / firstCharacterTotal) # multiply by P(character | eu)

                firstDigitIndex += 1
                secondDigitIndex += 1
            
            # return the biggest score out of all languages
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
            #print("ANSWER: " + answer)

            return answer, biggestValue, vocInt, smoothingValue

        elif nGramInt == 3:
            # for vocInt = 0 and nGramInt = 1

            # index of the character we're scanning in the tweet
=======
            return answer, biggestValue

        # for trigram
        elif nGramInt == 3:

            # indexes for three characters at a time
>>>>>>> Stashed changes
            firstDigitIndex = 0
            secondDigitIndex = 1
            thirdDigitIndex = 2

<<<<<<< Updated upstream
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
=======
            # smooth every entry in the frequency dictionaries 
            for k in self.eu_table.keys():
                for l in self.eu_table.keys():
                    for m in self.eu_table.keys():
                        self.eu_table[k][l][m] += smoothingValue
                        self.ca_table[k][l][m] += smoothingValue
                        self.gl_table[k][l][m] += smoothingValue
                        self.es_table[k][l][m] += smoothingValue
                        self.en_table[k][l][m] += smoothingValue
                        self.pt_table[k][l][m] += smoothingValue

            eu_score = 0
            ca_score = 0
            gl_score = 0
            es_score = 0
            en_score = 0
            pt_score = 0

            if vocInt != 3:
                # initialize the scores to their respective probabilities, P(eu), P(ca), etc...
                eu_score = math.log10(self.eu_tweet_counter/self.total_tweet_counter)
                ca_score = math.log10(self.ca_tweet_counter/self.total_tweet_counter)
                gl_score = math.log10(self.gl_tweet_counter/self.total_tweet_counter)
                es_score = math.log10(self.es_tweet_counter/self.total_tweet_counter)
                en_score = math.log10(self.en_tweet_counter/self.total_tweet_counter)
                pt_score = math.log10(self.pt_tweet_counter/self.total_tweet_counter)


            # for each language calculate the probability of three consecutive characters
            # score += log(P(x | yz)), where x is a vocabulary character in the string and zy is the previous two characters            
            for y in range(len(tweet) - 2):
                if checkKey(self.eu_table, tweet[firstDigitIndex]):
                    if checkKey(self.eu_table, tweet[secondDigitIndex]):
                        if checkKey(self.eu_table, tweet[thirdDigitIndex]):

                            firstTwoCharactersTotal = 0
                            for x in self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            eu_score += math.log10(self.eu_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)
                            
                            firstTwoCharactersTotal = 0
                            for x in self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            ca_score += math.log10(self.ca_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            gl_score += math.log10(self.gl_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            es_score += math.log10(self.es_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            en_score += math.log10(self.en_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                            firstTwoCharactersTotal = 0
                            for x in self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]].keys():
                                firstTwoCharactersTotal += self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][x]
                            pt_score += math.log10(self.pt_table[tweet[firstDigitIndex]][tweet[secondDigitIndex]][tweet[thirdDigitIndex]] / firstTwoCharactersTotal) # multiply by P(character | eu)

                firstDigitIndex += 1
                secondDigitIndex += 1
                thirdDigitIndex += 1

            # return the biggest score out of all languages
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
            return answer, biggestValue, vocInt, smoothingValue


    def train(self, path, fileName, vocInt, nGramInt):
=======
            return answer, biggestValue

    # training function:
    # takes a training file loaded with tweets and fills in a frequency dictionary for every possible language
    def train(self, path, fileName, vocabularyList, vocInt, nGramInt):
>>>>>>> Stashed changes
        p = path # path to the folder with input files
        f = fileName + '.txt' # the name of input file
        fullPath = p + f # full path

        tweetID =  ''
        userID = ''
        language = ''
        tweet = ''

        counter = 0
<<<<<<< Updated upstream

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

=======
        lineCounter = 0

        # dictionary creation
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

        # for unigram
        if nGramInt == 1:
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
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
=======
                    self.total_tweet_counter += 1 

                    # for our BYOM, remove unwanted text from tweets
                    if vocInt == 3:
                        tweet = removeRegEx(tweet)

                    # same process for every languages, but in their respective dictionaries.
                    if language == 'eu':
                        self.eu_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each character in the tweet
                        for x in range(0, tweetLength):
                            alreadyKey = False # if key doesn't exist yet
                            # test all keys of the respective dictionary
                            for k in self.eu_table.keys():
                                # if the key is in the dictionary, increment it.
                                if tweet[x] == k:
                                    self.eu_table[k] += 1
                                    alreadyKey = True
                            # if vocInt == 2 (isalpha) or vocInt == 3 (BYOM),
                            # then dynamically add keys to the dictionaries if isalpha() returns true and the key doesn't current exist.
                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 1
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'ca':
                        self.ca_tweet_counter += 1
>>>>>>> Stashed changes
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
<<<<<<< Updated upstream
                            self.characterCounterTotal += 1
                            self.characterCounterCA += 1
=======
>>>>>>> Stashed changes
                            for k in self.ca_table.keys():
                                if tweet[x] == k:
                                    self.ca_table[k] += 1
                                    alreadyKey = True

<<<<<<< Updated upstream
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
=======
                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 1
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'gl':
                        self.gl_tweet_counter += 1
>>>>>>> Stashed changes
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
<<<<<<< Updated upstream
                            self.characterCounterTotal += 1
                            self.characterCounterGL += 1
=======
>>>>>>> Stashed changes
                            for k in self.gl_table.keys():
                                if tweet[x] == k:
                                    self.gl_table[k] += 1
                                    alreadyKey = True

<<<<<<< Updated upstream
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
=======
                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 1
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'es':
                        self.es_tweet_counter += 1
>>>>>>> Stashed changes
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
<<<<<<< Updated upstream
                            self.characterCounterTotal += 1
                            self.characterCounterES += 1
=======
>>>>>>> Stashed changes
                            for k in self.es_table.keys():
                                if tweet[x] == k:
                                    self.es_table[k] += 1
                                    alreadyKey = True

<<<<<<< Updated upstream
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
=======
                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 1
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'en':
                        self.en_tweet_counter += 1
>>>>>>> Stashed changes
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
<<<<<<< Updated upstream
                            self.characterCounterTotal += 1
                            self.characterCounterEN += 1
=======
>>>>>>> Stashed changes
                            for k in self.en_table.keys():
                                if tweet[x] == k:
                                    self.en_table[k] += 1
                                    alreadyKey = True

<<<<<<< Updated upstream
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
=======
                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 1
                                    self.pt_table[tweet[x]] = 0
                    elif language == 'pt':
                        self.pt_tweet_counter += 1
>>>>>>> Stashed changes
                        tweetLength = len(tweet)

                        for x in range(0, tweetLength):
                            alreadyKey = False
<<<<<<< Updated upstream
                            self.characterCounterTotal += 1
                            self.characterCounterPT += 1
=======
>>>>>>> Stashed changes
                            for k in self.pt_table.keys():
                                if tweet[x] == k:
                                    self.pt_table[k] += 1
                                    alreadyKey = True

<<<<<<< Updated upstream
                            if vocInt == 2 and alreadyKey == False:
                            	if tweet[x].isalpha():
                                	self.eu_table[tweet[x]] = 0
                                	self.ca_table[tweet[x]] = 0
                                	self.gl_table[tweet[x]] = 0
                                	self.es_table[tweet[x]] = 0
                                	self.en_table[tweet[x]] = 0
                                	self.pt_table[tweet[x]] = 1
                

        elif nGramInt == 2:
=======
                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
                                if tweet[x].isalpha():
                                    self.eu_table[tweet[x]] = 0
                                    self.ca_table[tweet[x]] = 0
                                    self.gl_table[tweet[x]] = 0
                                    self.es_table[tweet[x]] = 0
                                    self.en_table[tweet[x]] = 0
                                    self.pt_table[tweet[x]] = 1
                    lineCounter += 1
                    print(lineCounter)
        # for bigram
        elif nGramInt == 2:

            lineNumber = 0

>>>>>>> Stashed changes
            # read the input file
            with open(fullPath, encoding="utf8") as f:
                # split every number in a line
                for line in f:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
                            counter = 0

                    self.total_tweet_counter += 1

                    # for our BYOM, remove unwanted text from tweets
                    if vocInt == 3:
                        tweet = removeRegEx(tweet)

                    # same process for every languages, but in their respective dictionaries.
                    if language == 'eu':
                        self.eu_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned

                        # iterate through each set of two characters in the tweet
                        for x in range(0, tweetLength - 1):
                            alreadyKey = False # if key doesn't exist yet

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]

                            for x in self.eu_table.keys():
                                if x == firstCharacter:
                                    for y in self.eu_table[x].keys():
                                        if y == secondCharacter:
                                            # if both keys are present, increment the entry.
                                            self.eu_table[x][y] += 1
                                            alreadyKey = True
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                    break

                            # if vocInt == 2 (isalpha) or vocInt == 3 (BYOM),
                            # then dynamically add keys to the dictionaries if isalpha() returns true and the key sequence doesn't current exist..
                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
                                # if the bigram is accepted by isalpha(),
                                if firstCharacter.isalpha() and secondCharacter.isalpha():
                                    # if the first character is not a key in the dictionary,
                                    if not checkKey(self.eu_table, firstCharacter):
                                        # create an entry of the character in the first level of the 2D dictionary
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}

                                        # fill in the second level of the dictionary at the new key index
                                        for x in self.eu_table.keys():
                                            self.eu_table[firstCharacter][x] = 0
                                            self.ca_table[firstCharacter][x] = 0
                                            self.gl_table[firstCharacter][x] = 0
                                            self.es_table[firstCharacter][x] = 0
                                            self.en_table[firstCharacter][x] = 0
                                            self.pt_table[firstCharacter][x] = 0
                                        # add the new character keys to all the second levels of the 2D dictionary
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][firstCharacter] = 0
                                            self.ca_table[x][firstCharacter] = 0
                                            self.gl_table[x][firstCharacter] = 0
                                            self.es_table[x][firstCharacter] = 0
                                            self.en_table[x][firstCharacter] = 0
                                            self.pt_table[x][firstCharacter] = 0

                                    # if the second character is not a key in the dictionary,
                                    if not checkKey(self.eu_table, secondCharacter):
                                        # create an entry of the character in the first level of the 2D dictionary
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}

                                        # fill in the second level of the dictionary at the new key index
                                        for x in self.eu_table.keys():
                                            self.eu_table[secondCharacter][x] = 0
                                            self.ca_table[secondCharacter][x] = 0
                                            self.gl_table[secondCharacter][x] = 0
                                            self.es_table[secondCharacter][x] = 0
                                            self.en_table[secondCharacter][x] = 0
                                            self.pt_table[secondCharacter][x] = 0

                                        # add the new character keys to all the second levels of the 2D dictionary
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][secondCharacter] = 0
                                            self.ca_table[x][secondCharacter] = 0
                                            self.gl_table[x][secondCharacter] = 0
                                            self.es_table[x][secondCharacter] = 0
                                            self.en_table[x][secondCharacter] = 0
                                            self.pt_table[x][secondCharacter] = 0

                                    # increment the approriate entry of this new set of characters
                                    self.eu_table[firstCharacter][secondCharacter] += 1

                    elif language == 'ca':
                        self.ca_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned

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

                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
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
                        self.gl_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
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
                        self.es_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3)  and alreadyKey == False:
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
                        self.en_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
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
                        self.pt_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
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
        # for trigram
        elif nGramInt == 3:
            lineNumber = 0
>>>>>>> Stashed changes
            # read the input file
            with open(fullPath, encoding="utf8") as f:
                # split every number in a line
                for line in f:
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
                            counter = 0 


                    self.total_tweet_counter += 1

                    # for our BYOM, remove unwanted text from tweets
                    if vocInt == 3:
                        tweet = removeRegEx(tweet)

                    # same process for every languages, but in their respective dictionaries.
                    if language == 'eu':
                        self.eu_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
                        # iterate through each set of three characters in the tweet
                        for x in range(0, tweetLength - 2):
                            alreadyKey = False # if key doesn't exist yet

                            firstCharacter = tweet[firstDigitIndex]
                            secondCharacter = tweet[secondDigitIndex]
                            thirdCharacter = tweet[thirdDigitIndex]

                            for x in self.eu_table.keys():
                                if x == firstCharacter:
                                    for y in self.eu_table[x].keys():
                                        if y == secondCharacter:
                                            for z in self.eu_table[x][y].keys():
                                                if z == thirdCharacter:
                                                    # if the sequence of three characters exist in the dictionary, increment it
                                                    self.eu_table[x][y][z] += 1
                                                    alreadyKey = True
                                                if alreadyKey:
                                                    break
                                        if alreadyKey:
                                            break
                                if alreadyKey:
                                        break

                            # if vocInt == 2 (isalpha) or vocInt == 3 (BYOM),
                            # then dynamically add keys to the dictionaries if isalpha() returns true and the key sequence doesn't current exist.
                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
                                # if the trigram is accepted by isalpha(),
                                if firstCharacter.isalpha() and secondCharacter.isalpha() and thirdCharacter.isalpha():
                                    # if the first character is not in the vocabulary,
                                    if not checkKey(self.eu_table, firstCharacter):
                                        # generate first level dictionary entry for that character
                                        self.eu_table[firstCharacter] = {}
                                        self.ca_table[firstCharacter] = {}
                                        self.gl_table[firstCharacter] = {}
                                        self.es_table[firstCharacter] = {}
                                        self.en_table[firstCharacter] = {}
                                        self.pt_table[firstCharacter] = {}
                                        # generate base vocabulary entries in the new character entry
                                        for x in self.eu_table.keys():
                                            self.eu_table[firstCharacter][x] = {}
                                            self.ca_table[firstCharacter][x] = {}
                                            self.gl_table[firstCharacter][x] = {}
                                            self.es_table[firstCharacter][x] = {}
                                            self.en_table[firstCharacter][x] = {}
                                            self.pt_table[firstCharacter][x] = {}
                                        # generate second level dictionary entry in all the character entries
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][firstCharacter] = {}
                                            self.ca_table[x][firstCharacter] = {}
                                            self.gl_table[x][firstCharacter] = {}
                                            self.es_table[x][firstCharacter] = {}
                                            self.en_table[x][firstCharacter] = {}
                                            self.pt_table[x][firstCharacter] = {}

                                        # generate second level dictionary entry for the new entry
                                        self.eu_table[firstCharacter][firstCharacter] = {}
                                        self.ca_table[firstCharacter][firstCharacter] = {}
                                        self.gl_table[firstCharacter][firstCharacter] = {}
                                        self.es_table[firstCharacter][firstCharacter] = {}
                                        self.en_table[firstCharacter][firstCharacter] = {}
                                        self.pt_table[firstCharacter][firstCharacter] = {}

                                        # generate third level character entries for all entries that concern the new character
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
                                        # generate first level dictionary entry for that character
                                        self.eu_table[secondCharacter] = {}
                                        self.ca_table[secondCharacter] = {}
                                        self.gl_table[secondCharacter] = {}
                                        self.es_table[secondCharacter] = {}
                                        self.en_table[secondCharacter] = {}
                                        self.pt_table[secondCharacter] = {}
                                        # generate base vocabulary entries in the new character entry
                                        for x in self.eu_table.keys():
                                            self.eu_table[secondCharacter][x] = {}
                                            self.ca_table[secondCharacter][x] = {}
                                            self.gl_table[secondCharacter][x] = {}
                                            self.es_table[secondCharacter][x] = {}
                                            self.en_table[secondCharacter][x] = {}
                                            self.pt_table[secondCharacter][x] = {}
                                        # generate second level dictionary entry in all the character entries
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][secondCharacter] = {}
                                            self.ca_table[x][secondCharacter] = {}
                                            self.gl_table[x][secondCharacter] = {}
                                            self.es_table[x][secondCharacter] = {}
                                            self.en_table[x][secondCharacter] = {}
                                            self.pt_table[x][secondCharacter] = {}

                                        # generate second level dictionary entry for the new entry
                                        self.eu_table[secondCharacter][secondCharacter] = {}
                                        self.ca_table[secondCharacter][secondCharacter] = {}
                                        self.gl_table[secondCharacter][secondCharacter] = {}
                                        self.es_table[secondCharacter][secondCharacter] = {}
                                        self.en_table[secondCharacter][secondCharacter] = {}
                                        self.pt_table[secondCharacter][secondCharacter] = {}

                                        # generate third level character entries for all entries that concern the new character
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
                                        # generate first level dictionary entry for that character
                                        self.eu_table[thirdCharacter] = {}
                                        self.ca_table[thirdCharacter] = {}
                                        self.gl_table[thirdCharacter] = {}
                                        self.es_table[thirdCharacter] = {}
                                        self.en_table[thirdCharacter] = {}
                                        self.pt_table[thirdCharacter] = {}
                                        # generate base vocabulary entries in the new character entry
                                        for x in self.eu_table.keys():
                                            self.eu_table[thirdCharacter][x] = {}
                                            self.ca_table[thirdCharacter][x] = {}
                                            self.gl_table[thirdCharacter][x] = {}
                                            self.es_table[thirdCharacter][x] = {}
                                            self.en_table[thirdCharacter][x] = {}
                                            self.pt_table[thirdCharacter][x] = {}
                                        # generate second level dictionary entry in all the character entries
                                        for x in self.eu_table.keys():
                                            self.eu_table[x][thirdCharacter] = {}
                                            self.ca_table[x][thirdCharacter] = {}
                                            self.gl_table[x][thirdCharacter] = {}
                                            self.es_table[x][thirdCharacter] = {}
                                            self.en_table[x][thirdCharacter] = {}
                                            self.pt_table[x][thirdCharacter] = {}

                                        # generate second level dictionary entry for the new entry
                                        self.eu_table[thirdCharacter][thirdCharacter] = {}
                                        self.ca_table[thirdCharacter][thirdCharacter] = {}
                                        self.gl_table[thirdCharacter][thirdCharacter] = {}
                                        self.es_table[thirdCharacter][thirdCharacter] = {}
                                        self.en_table[thirdCharacter][thirdCharacter] = {}
                                        self.pt_table[thirdCharacter][thirdCharacter] = {}

                                        # generate third level character entries for all entries that concern the new character                                                              
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
                                    # increment the approriate entry of this new set of characters
                                    self.eu_table[firstCharacter][secondCharacter][thirdCharacter] += 1

                            firstDigitIndex += 1
                            secondDigitIndex += 1
                            thirdDigitIndex += 1

                    if language == 'ca':
                        self.ca_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
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
                        self.gl_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
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
                        self.es_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
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
                        self.en_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3)and alreadyKey == False:
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
                        self.pt_tweet_counter += 1
                        tweetLength = len(tweet) # length of the tweet being scanned
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

                            if (vocInt == 2 or vocInt == 3) and alreadyKey == False:
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
    # function that will score each line of a test file and produce a trace file + a statistic file
    def scoreFile (self, path, fileName, vocInt, nGramInt, smoothingValue):

        startTime = time.time()

        tweetCounter = 0

        correctCounter = 0

>>>>>>> Stashed changes
        eu_tweet_counter = 0
        ca_tweet_counter = 0
        gl_tweet_counter = 0
        es_tweet_counter = 0
        en_tweet_counter = 0
        pt_tweet_counter = 0
<<<<<<< Updated upstream
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
=======

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

                if vocInt != 3:
                    guessedLanguage, guessedScore = self.score(word[3], vocInt, nGramInt, smoothingValue)
                else:
                    guessedLanguage, guessedScore = self.score(removeRegEx(word[3]), vocInt, nGramInt, smoothingValue)


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
                tweetCounter += 1
            writeFile.close()
        
        statisticFileName ="stat_"+ str(vocInt) + "_"+ str(nGramInt)+ "_" + str(smoothingValue) + ".txt"
        writeFile = open(statisticFileName,"w+", encoding="utf8")
        
        writeFile.write("vocInt = " + str(vocInt) + ", nGramInt = " + str(nGramInt) + ", smoothingValue = " + str(smoothingValue) + "\n")
        writeFile.write('\n')

        # Training Info

        writeFile.write("Training Information:\n")
        writeFile.write("EU tweets: " + str(self.eu_tweet_counter) + "\n")
        writeFile.write("CA tweets: " + str(self.ca_tweet_counter) + "\n")
        writeFile.write("GL tweets: " + str(self.gl_tweet_counter) + "\n")
        writeFile.write("ES tweets: " + str(self.es_tweet_counter) + "\n")
        writeFile.write("EN tweets: " + str(self.en_tweet_counter) + "\n")
        writeFile.write("PT tweets: " + str(self.pt_tweet_counter) + "\n")
        writeFile.write("Total training tweets: " + str(self.total_tweet_counter) + "\n")


        writeFile.write('\n')

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

        writeFile.write('\n')

        writeFile.write("Test Time: ~" + str(round((time.time() - startTime), 4)) + " seconds.")

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
AI_two = AI()
AI_three = AI()
AI_four = AI()
AI_five = AI()

# BYOM

AI_one_vocList = voc1
AI_one_vocInt = 3
AI_one_nGramInt = 2
AI_one_smoothingValue = 1

AI_one.train(path, trainFileName, AI_one_vocList, AI_one_vocInt, AI_one_nGramInt)
AI_one.scoreFile(path, testFileName , AI_one_vocInt, AI_one_nGramInt, AI_one_smoothingValue)

# V=0, n=1, d=0

AI_two_vocList = voc0
AI_two_vocInt = 0
AI_two_nGramInt = 1
AI_two_smoothingValue = 0

AI_two.train(path, trainFileName, AI_two_vocList, AI_two_vocInt, AI_two_nGramInt)
AI_two.scoreFile(path, testFileName , AI_two_vocInt, AI_two_nGramInt, AI_two_smoothingValue)

# V=1, n=2, d=0.5

AI_three_vocList = voc1
AI_three_vocInt = 1
AI_three_nGramInt = 2
AI_three_smoothingValue = 0.5

AI_three.train(path, trainFileName, AI_three_vocList, AI_three_vocInt, AI_three_nGramInt)
AI_three.scoreFile(path, testFileName , AI_three_vocInt, AI_three_nGramInt, AI_three_smoothingValue)

AI_four_vocList = voc1
AI_four_vocInt = 1
AI_four_nGramInt = 3
AI_four_smoothingValue = 1

AI_four.train(path, trainFileName, AI_four_vocList, AI_four_vocInt, AI_four_nGramInt)
AI_four.scoreFile(path, testFileName , AI_four_vocInt, AI_four_nGramInt, AI_four_smoothingValue)

AI_five_vocList = voc1
AI_five_vocInt = 2
AI_five_nGramInt = 2
AI_five_smoothingValue = 0.3

AI_five.train(path, trainFileName, AI_five_vocList, AI_five_vocInt, AI_five_nGramInt)
AI_five.scoreFile(path, testFileName , AI_five_vocInt, AI_five_nGramInt, AI_five_smoothingValue)
>>>>>>> Stashed changes
