import sys
import json

def main():
    sent_file = open(sys.argv[1])
#    lines(sent_file)
    sentiments = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sentiments[term] = int(score)  # Convert the score to an integer.
    #print 'terms', len(sentiments)
    
    tweet_file = open(sys.argv[2])
    #lines(tweet_file)
    tweet = {}
    for line in tweet_file:
        score = 0
        tweet  =  json.loads(line)
        if 'text' in tweet.keys():
            text = tweet['text'].encode('utf-8')
            #print 'text: ', text
            words = text.split()
            #print 'words: ', len(words)
            for word in words:
                if word in sentiments.keys():
                    score = score +  sentiments[word]
        print score

if __name__ == '__main__':
    main()
    #print '---------------------------------------------------------------'
