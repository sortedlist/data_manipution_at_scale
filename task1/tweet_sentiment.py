import sys
import json
import string


def create_dict(sentiment_score_file):
    senti_file = open(sentiment_score_file)
    scores = {} 
    for line in senti_file:
      term, score  = line.split("\t")
      scores[term] = int(score) 
    return scores

def norm_word(word):
    exclude = set(string.punctuation)
    word = ''.join(ch for ch in word.lower() if ch not in exclude)
    return word

def get_senti(senti_dict,line):
	senti_score = 0
	for word in line.split(' '):
		if word in senti_dict:
			senti_score += senti_dict[word]
	return senti_score

def main():
	senti_dict = create_dict(sys.argv[1])
	tweet_file = open(sys.argv[2])
	for line in tweet_file:
		d = json.loads(line.encode('utf8'))
		if 'text' in d.keys():
			norm_tweet = norm_word(d['text'].encode('utf8'))
			print get_senti(senti_dict,norm_tweet)

if __name__ == '__main__':
    main()



