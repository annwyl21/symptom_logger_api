from collections import Counter
import re
import nltk
from nltk.corpus import stopwords

class Summarize():
	
	@staticmethod
	def organize_data(data):
		symptom_string = ""
		
		#extract data from json
		for i in range(len(data)):
			symptom_string += data[i]['description']
			symptom_string += ". "
		
		return symptom_string
	
	@staticmethod
	def create_summary(data):

		symptom_string = Summarize.organize_data(data)
		
		max_words = 12
		num_sents = 3

		# remove punctuation
		tokens = nltk.word_tokenize(symptom_string.lower())
		# create list of words without stopwords
		string_stopwords_removed = Summarize.remove_stop_words(tokens)
		# create dictionary of word frequencies
		word_freq = Summarize.get_word_freq(string_stopwords_removed)
		# create dictionary of sentence scores
		sent_scores = Summarize.score_sentences(symptom_string, word_freq, max_words)

		counts = Counter(sent_scores)
		summary_sentences = [sent for sent, _ in counts.most_common(int(num_sents))]
		summary = ' '.join(summary_sentences)
		return summary

	@staticmethod
	def remove_stop_words(tokens):
		stop_words = set(stopwords.words('english'))
		return [word for word in tokens if word not in stop_words and word.isalpha()]
	
	@staticmethod
	def get_word_freq(tokens):
		return nltk.FreqDist(tokens)
	
	@staticmethod
	def score_sentences(symptoms, word_freq, max_words):
		sent_scores = dict()
		sentences = nltk.sent_tokenize(symptoms)
		for sent in sentences:
			words = nltk.word_tokenize(sent.lower())
			sent_word_count = len(words)
			if sent_word_count <= int(max_words):
				sent_scores[sent] = sum(word_freq[word] for word in words if word in word_freq)
		return sent_scores

if __name__ == '__main__':

	myjson = [{"date":"2023-10-01","time":"20:49","pain_score":1,"description":"Slight discomfort in right hip"},
	{"date":"2023-10-03","time":"14:07","pain_score":2,"description":"right hip feels stiff to move, difficulty standing for long periods"},
	{"date":"2023-10-05","time":"07:23","pain_score":3,"description":"Noticeable pain in right hip, especially when climbing stairs."},
	{"date":"2023-10-07","time":"19:21","pain_score":4,"description":"Pain in right hip while sitting"},
	{"date":"2023-10-09","time":"19:56","pain_score":5,"description":"Moderate pain in the right hip, difficulty turning in bed."},
	{"date":"2023-10-11","time":"14:12","pain_score":6,"description":"Sharp pain in right hip while climbing stairs."},
	{"date":"2023-10-13","time":"07:36","pain_score":7,"description":"Intense pain in right hip on waking, maybe I slept on my hip."},
	{"date":"2023-10-15","time":"07:10","pain_score":8,"description":"Hard to get out of bed today, right hip really bothering me"},
	{"date":"2023-10-17","time":"09:30","pain_score":9,"description":"Pain in right hip after walking."},
	{"date":"2023-10-19","time":"09:36","pain_score":10,"description":"Right hip really hurts today, walking is really slow and laboured"},
	{"date":"2023-10-21","time":"16:53","pain_score":10,"description":"Right hip feels really painful, can hardly get up the stairs"},
	{"date":"2023-10-23","time":"07:55","pain_score":10,"description":"Right hip feels very painful after sleeping on it."}]

	data = Summarize.organize_data(myjson)
	summary = Summarize.create_summary(myjson)
	# print(summary)