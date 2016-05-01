import sys
import json


def getHashTags(tweet_file):
	occurrences = {}
	for line in tweet_file:
		res = json.loads(line)
		entities = res.get('entities', None)
		if entities != None:
			hashtags = entities.get('hashtags', None)
			if hashtags!=None:
				for i in range(0, len(hashtags)):
					term = hashtags[i].get('text').encode('ascii', 'ignore')
					occurrences[term] = int(occurrences.get(term, 0)) - 1
	return occurrences

def main():
	tweet_file = open(sys.argv[1])
	occurrences = {}
	count = 0
	occurrences = getHashTags(tweet_file)
	for key, value in sorted(occurrences.iteritems(), key = lambda (k,v): (v,k)):
		if key != '' and count < 10:
			print "%s %f" % (key, -occurrences[key])
			count = count+1


if __name__ == '__main__':
    main()
