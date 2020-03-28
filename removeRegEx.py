import re
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

#extracing @username from tweet msg
randomTweet = "😋 @AnderDelPozo @PesqueWhite  http://t.co/JYEE8rfdSH hahaha yo tambien me ¿Mi idolo? http://t.co/6xyXrhzAil Buenaas nocheees guido@google.com ♥♥♥√√√√ mañana tolosa *-*  he quedao pillao ahahha try guido@python.org compras x&lt;33333😋"
print("before: " + randomTweet)

randomTweet = removeRegEx(randomTweet)
print("after: " + randomTweet)