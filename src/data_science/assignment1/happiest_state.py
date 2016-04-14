import sys
import json
import re

state_codes = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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
    states = {}
    for line in tweet_file:
        score = 0
        tweet  =  json.loads(line)
        state = None
        if 'user' in tweet.keys():
            user  =  tweet['user']
            state = determine_state(user)
        if state <> None and 'text' in tweet.keys():
            text = tweet['text'].encode('utf-8')
            #print 'text', text
            #print 'text: ', text
            words = text.split()
            #print 'words: ', len(words)
            for word in words:
                if word in sentiments.keys():
                    score = score +  sentiments[word]
            if score <> 0:
                #print 'score', score
                if state in states.keys():
                    states[state] = score + states[state]
                else:
                    states[state] = score
    max_score = 0
    happiest_state = None
    for state in states.keys():
        if max_score < states[state]:
            max_score = states[state]
            happiest_state = state
    print happiest_state
        
def mapStringToStateCode(code):
    if code in state_codes.keys():
        return code
    return None
            
def determine_state(user):
    state_code = None
    #if 'coordinates' in user.keys():
    #    coordinates = user['coordinates'].encode('utf-8')
    #if state_code <> None:
    #    return state_code
        
    if 'location' in user.keys() and user['location']:
        location = user['location'].encode('utf-8')
        if location <> None and len(location) > 3:
            match = re.search(r'(\w+)', location)
            if match:
                maybe_code = match.group(1)
                if len(maybe_code) < 25:
                    for state_code in state_codes.keys():
                        if state_codes[state_code] == maybe_code:
                            #print 'state_code', state_code
                            return state_code 
    return None

if __name__ == '__main__':
    main()
    #print '---------------------------------------------------------------'
