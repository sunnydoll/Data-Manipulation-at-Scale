import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def dictGenerate(fp):
	afinnfile = fp
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	# print scores.items() # Print every (term, score) pair in the dictionary
	return scores


def scoreTweets(tweet_file, sentDict):
	newScores = {}
	for line in tweet_file:
		tweet_score = 0
		result = json.loads(line)
		string = result.get('text','').encode("ascii", "ignore")
		words = string.strip().split()
		newWords= []
		for word in words:
			word = word.encode('utf-8')
			word_score = int(sentDict.get(word,'1000000'))
			if word_score == 1000000:
				newWords.append(word)
			else:
				tweet_score = tweet_score + word_score
		for word in newWords:
			newScores[word] = newScores.get(word,0) + tweet_score
	return newScores


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentDict = dictGenerate(sent_file)
    newScores = scoreTweets(tweet_file, sentDict)
    for key, value in sorted(newScores.iteritems(), key = lambda (k,v): (v,k)):
		print "%s %s" % (key, value)

if __name__ == '__main__':
    main()
