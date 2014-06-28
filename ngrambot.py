# Import the corpus and functions used from nltk library
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import LidstoneProbDist
from nltk.model import NgramModel
import re
import random
import tweepy

# Tokens contains the words for Genesis and Reuters Trade
# tokens = list(genesis.words('english-kjv.txt'))
# tokens.extend(list(reuters.words(categories = 'trade')))

def hammertime(corpus, ngramss=0, numGen=100):
	
	tokens = list(word_tokenize(corpus))
	print tokens[0:900]
	# estimator for smoothing the N-gram model
	estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)

	if ngramss <= 0:
		ngramss = random.randint(2, 4)

	model = NgramModel(ngramss, tokens, False, False, estimator)

	# Apply the language model to generate 50 words in sequence
	text_words = model.generate(numGen)

	# Concatenate all words generated in a string separating them by a space.
	text = ' '.join([word for word in text_words])

	return text

def squidtime(corpus):
	tokens = list(word_tokenize(corpus))
	start = random.randint(0,len(tokens)-25)
	end = random.randint(2,23)
	text_words = tokens[start:start+end]
	text = ' '.join([word for word in text_words])
	return text

f = open('document1.txt')
raw = f.read()
f.close()

if (random.randint(0,1) == 1):
	text = hammertime(raw.lower(), 3, random.randint(20,23))
	#text = hammertime(raw.lower(), 3, 100)
else:
	text = squidtime(raw)


def dashrepl(matchobj):
	return matchobj.group(0)[1:2]

text = re.sub('\s[.:;?,)\'!]', dashrepl, text)

#text = re.split('\.', text[::-1], 1)
#text = text[len(text)-1][::-1]+'.'

text = re.split('^,`]\s', text)
text = text[len(text)-1]

length = random.randint(100, 140)

auth = tweepy.OAuthHandler('UCVRDEHfpj5VWfC8U63zXbyf5', 'lLnj7CRYDn7IYw3IpBdB79YU7qP5OnAj45QLMfo6lkomb2laHu')
auth.set_access_token('2592040632-DZj6re7wRckXHr86HMCBgsUcdzqP5W2goQSRCR1', 'dpNvygkjBLddIUtQ5ftEG1WZiXMFporiGAvavNoHUxHP3')

api = tweepy.API(auth)

print text[0:140]

resp = "yes"

api.update_status(text[0:140])
