import sys
import json
import operator

def print_top_ten_hashtags(tweet_file):
    known_hashtags = {}
    tweet_file.seek(0)
    for tweet in tweet_file:
        try:
            tweetjson = json.loads(tweet)
            if 'entities' in tweetjson:
                hashtags = tweetjson['entities']['hashtags']
                if hashtags:
                    for hashtag in hashtags:
                        hashtag = hashtag['text']
                        if hashtag not in known_hashtags:
                            known_hashtags[hashtag] = 1
                        else:
                            known_hashtags[hashtag] += 1
        except ValueError:
            print tweet
            raw_input('')
    sorted_hashtags = sorted(known_hashtags.items(), key=operator.itemgetter(1))
    sorted_hashtags = sorted_hashtags[-10:]
    for hashtag, freq in reversed(sorted_hashtags):
        print hashtag, freq

def main():
    tweet_file = open(sys.argv[1])
    print_top_ten_hashtags(tweet_file)

if __name__ == '__main__':
    main()
