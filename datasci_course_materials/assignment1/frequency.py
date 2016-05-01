import sys
import json


def freqTweets(tweet_file):
	occurrences = {}
	for line in tweet_file:
		count = 0
		tweet = json.loads(line)
		text = tweet.get('text','').encode("ascii", "ignore")
		words = text.split()
		for word in words:
			occurrences[word] = int(occurrences.get(word, 0)) + 1
			count = count + 1
	return occurrences


def main():
    tweet_file = open(sys.argv[1])
    occurrences = {}
    occurrences = freqTweets(tweet_file)
    for key in occurrences.keys():
    	print "%s %0.4f" % (key, 1.0 * occurrences[key] / len(occurrences))



if __name__ == '__main__':
    main()
