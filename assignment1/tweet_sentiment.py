import sys
import json

def parse_scores(afinnfile):
    afinnfile.seek(0)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term.lower()] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def print_tweet_scores(tweet_file, scores):
    tweet_file.seek(0)
    for tweet in tweet_file:
        tweetjson = json.loads(tweet)
        if 'text' in tweetjson.keys():
            tweet_text = tweetjson['text']
            words = tweet_text.lower().split()
            score = sum([scores[word] if word in scores else 0 for word in words])
            print score
        else:
            print 0

def main():
    sentiment_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = parse_scores(sentiment_file)
    print_tweet_scores(tweet_file, scores)

if __name__ == '__main__':
    main()
