import sys
import json

def hw():
    print 'Hello, world!'

def parse_scores(afinnfile):
    afinnfile.seek(0)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term.lower()] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def parse_tweets(tweet_file, scores):
    new_terms = {}
    tweet_file.seek(0)
    for tweet in tweet_file:
        tweetjson = json.loads(tweet)
        if 'text' in tweetjson.keys():
            tweet_text = tweetjson['text']
            words = tweet_text.lower().split()
            score = 0
            new_words = []
            for word in words:
                if word in scores:
                    score += scores[word]
                else:
                    new_words.append(word)
            if score != 0:
                for word in new_words:
                    if word not in new_terms:
                        new_terms[word] = []
                    new_terms[word].append(score)

    for (term, scores) in new_terms.items():
        if len(scores) < 3:
            del new_terms[term]
        else:
            score = sum(scores)/float(len(scores))
            if score != 0:
                new_terms[term] = score
            else:
                del new_terms[term]

    for term, score in new_terms.items():
        print "{} {:.2f}".format(term.encode('utf-8'), score)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = parse_scores(sent_file)
    parse_tweets(tweet_file, scores)

if __name__ == '__main__':
    main()
