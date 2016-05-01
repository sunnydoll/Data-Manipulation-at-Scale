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

def procTweet(fp, sentDict):
	tweetFile = open("output.txt")
	for line in tweetFile:
		score = 0
		jsonTweet = json.loads(line)
		if jsonTweet.has_key('text'):
			text = jsonTweet['text']
			words = text.split()
			for word in words:
				if word in sentDict:
					score = score + sentDict[word]
		print score

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	# hw()
	# lines(sent_file)
	# lines(tweet_file)
	sentDict = dictGenerate(sent_file)
	procTweet(tweet_file, sentDict)



if __name__ == '__main__':
    main()
