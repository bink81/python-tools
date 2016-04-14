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
    term_sentiments = {}
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
                    term_sentiments[word] = sentiments[word]
            # now we know tweet's score!
            for word in words:
                if word in sentiments.keys():
                    term_sentiments[word] = sentiments[word]
                else:
                    denominator = (score * 1.0) / (len(words) * 1.0)
                    if word in term_sentiments.keys():
                        term_sentiments[word] = term_sentiments[word] +  denominator
                    else:
                        term_sentiments[word] = denominator
    for term_sentiment in term_sentiments.keys():                
        print term_sentiment, term_sentiments[term_sentiment]

if __name__ == '__main__':
    main()
    #print '---------------------------------------------------------------'
