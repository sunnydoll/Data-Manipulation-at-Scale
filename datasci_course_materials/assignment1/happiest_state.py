import sys
import json

def dictGenerate(fp):
	afinnfile = fp
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	# print scores.items() # Print every (term, score) pair in the dictionary
	return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

if __name__ == '__main__':
    main()
