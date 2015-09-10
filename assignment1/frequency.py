import sys
import json
import operator

def parse_tweets(tweet_file):
    terms = {}
    normalizer = 0
    tweet_file.seek(0)
    for tweet in tweet_file:
        tweetjson = json.loads(tweet)
        if 'text' in tweetjson.keys():
            tweet_text = tweetjson['text']
            words = tweet_text.lower().split()
            for word in words:
                if word not in terms:
                    terms[word] = 0
                terms[word] += 1
                normalizer += 1
    sorted_terms = sorted(terms.items(), key=operator.itemgetter(1))
    for term, frequency in sorted_terms:
        print "{} {}".format(term.encode('utf-8'), (1.0 * frequency)/normalizer)

def main():
    tweet_file = open(sys.argv[1])
    parse_tweets(tweet_file)

if __name__ == '__main__':
    main()
