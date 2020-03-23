import re
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

# run the the A* function on the input file with heuristic function 0
def test(path, fileName):
	p = path # path to the folder with input files
	f = fileName + '.txt' # the name of input file
	fullPath = p + f # full path

	tweetID =  ''
	userID = ''
	language = ''
	tweet = ''

	counter = 0 # used to split the line into different variables

	characterCounterTotal = 0  # total number of characters scanned

	# still not sure if these variables below will be useful

	characterCounterEU = 0 # total number of EU characters scanned
	characterCounterCA = 0 # total number of CA characters scanned
	characterCounterGL = 0 # total number of GL characters scanned
	characterCounterES = 0 # total number of ES characters scanned
	characterCounterEN = 0 # total number of EN characters scanned
	characterCounterPT = 0 # total number of PT characters scanned


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
					characterCounterTotal += 1 # increment total characters scanned
					characterCounterEU += 1 # increment total EU characters scanned
					# test all keys of the respective dictionary (count all the n-grams in the current vocabulary)
					for k in voc0size1_eu.keys(): 
						if tweet[x] == k:
							voc0size1_eu[k] += 1
			elif language == 'ca':
				
				tweetLength = len(tweet)

				for x in range(0, tweetLength):
					characterCounterTotal += 1
					characterCounterCA += 1
					for k in voc0size1_eu.keys():
						if tweet[x] == k:
							voc0size1_ca[k] += 1
			elif language == 'gl':
				
				tweetLength = len(tweet)

				for x in range(0, tweetLength):
					characterCounterTotal += 1
					characterCounterGL += 1
					for k in voc0size1_eu.keys():
						if tweet[x] == k:
							voc0size1_gl[k] += 1
			elif language == 'es':

				tweetLength = len(tweet)

				for x in range(0, tweetLength):
					characterCounterTotal += 1
					characterCounterES += 1
					for k in voc0size1_eu.keys():
						if tweet[x] == k:
							voc0size1_es[k] += 1
			elif language == 'en':
				
				tweetLength = len(tweet)

				for x in range(0, tweetLength):
					characterCounterTotal += 1
					characterCounterEN += 1
					for k in voc0size1_eu.keys():
						if tweet[x] == k:
							voc0size1_en[k] += 1
			elif language == 'pt':
				
				tweetLength = len(tweet)

				for x in range(0, tweetLength):
					characterCounterTotal += 1
					characterCounterPT += 1
					for k in voc0size1_eu.keys():
						if tweet[x] == k:
							voc0size1_pt[k] += 1		
			

	# test print the vocabulary for language EU
	for k in voc0size1_eu.keys():
		print(k, voc0size1_eu[k])

	# test print character total
	print()
	print(characterCounterTotal)
	print()

	# test tweet sample
	print()
	print("TEST TWEET")
	print()

	# 1st sample
	testTweet = "@AnderDelPozo @PesqueWhite hahaha yo tambien me he quedao pillao ahahha"

	testTweetLowered = testTweet.lower()

	# create a dictioanry for this sample
	testVoc = {
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

	testCharacterCounter = 0

	tweetLength = len(testTweet)

	for x in range(0, tweetLength):
		testCharacterCounter += 1
		for k in testVoc.keys():
			if testTweet[x] == k:
				testVoc[k] += 1

	for k in testVoc.keys():
		print(k, testVoc[k])

	'''

	score(), helper function to calculate Naive Bayes
	vocInt,
	0 = converted lowercase a-z
	1 = lowercase and uppercase a-z
	2 = lowercase and uppcase a-z and isAlpha

	nGramInt,
	1 = unigram
	2 = bigram
	3 = trigram
	'''

	# "@AnderDelPozo @PesqueWhite hahaha yo tambien me he quedao pillao ahahha"
	
	def score(tweet, vocInt, nGramInt):

		# for vocInt = 0 and nGramInt = 1

		# index of the character we're scanning in the tweet
		currentIndex = 0

		# initialize the scores to their respective probabilities, P(eu), P(ca), etc...
		eu_score = characterCounterEU / characterCounterTotal 
		ca_score = characterCounterCA / characterCounterTotal 
		gl_score = characterCounterGL / characterCounterTotal
		es_score = characterCounterES / characterCounterTotal
		en_score = characterCounterEN / characterCounterTotal
		pt_score = characterCounterPT / characterCounterTotal

		# update the scores if the character is in the vocabulary
		for k in voc0size1_eu.keys():
			if tweet[currentIndex] == k:
				eu_score *= voc0size1_eu[k] / characterCounterEU # multiply by P(character | eu)
				ca_score *= voc0size1_ca[k] / characterCounterCA # multiply by P(character | ca)
				gl_score *= voc0size1_gl[k] / characterCounterGL # multiply by P(character | gl)
				es_score *= voc0size1_es[k] / characterCounterES # multiply by P(character | es)
				en_score *= voc0size1_en[k] / characterCounterEN # multiply by P(character | en)
				pt_score *= voc0size1_pt[k] / characterCounterPT # multiply by P(character | pt)

		# show scores
		print(eu_score)
		print(ca_score)
		print(gl_score)
		print(es_score)
		print(en_score)
		print(pt_score)

	# test score function with example tweet
	tweetEx1 = "Moitas gracias  @FelixCastro_L 😊 eso non se duda jajaja".lower()
	score(tweetEx1, 0, 1)

# main
test('./', 'training-tweets')

#extracing @username from tweet msg
testTweet = "@AnderDelPozo @PesqueWhite hahaha yo tambien me he quedao pillao ahahha"

#detects user tag
tagUser = re.compile('@\w+\s')

#detects email address
email = re.compile('\w+@\w+\.[a-z]{3}')
text="To email Guido, @AnderDelPozo @PesqueWhite try guido@python.org. or the older address guido@google.com."
test2=email.findall(text)

##test3=tagUser.findall(text)
test3=tagUser.findall(testTweet)

print(test2)
print(test3)
print(testTweet)
print(len(test3))

#successfully removed @userTags. repeat same for removing emails
testTweet = testTweet.replace(test3[0], '')
print(testTweet)
testTweet = testTweet.replace(test3[1], '')
print(testTweet)

#extracting domain URL's
#re.findall(r'(https?://[^\s]+)', myString)