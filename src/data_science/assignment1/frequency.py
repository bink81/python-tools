import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    terms = {}
    count = 0
    for line in tweet_file:
        tweet = {}
        tweet  =  json.loads(line)
        if 'text' in tweet.keys():
            text = tweet['text'].encode('utf-8')
            #print 'text: ', text
            words = text.split()
            #print 'words: ', len(words)
            # now we know tweet's score!
            for word in words:
                if word in terms.keys():
                    terms[word] = terms[word] + 1
                else:
                    terms[word] = 0
                    count =count + 1
                    
    for term in terms.keys():                
        print term, (terms[term] * 1.0) / (count * 1.0)

if __name__ == '__main__':
    main()
    #print '---------------------------------------------------------------'
