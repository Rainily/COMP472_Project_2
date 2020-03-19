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


# main
test('./', 'training-tweets')