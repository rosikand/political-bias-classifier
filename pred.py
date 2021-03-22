"""
File: pred.py 
-------------------
This program utilizes the trained model to make predictions.  
"""

import pickle
import gzip 

def load_model():
	# Load in the model using Pickle 
	f = gzip.open('compressed_trained_model.pklz','rb')
	global loaded_model
	loaded_model = pickle.load(f)
	f.close()


def predict_text(txt):
	"""
	This function uses the loaded model to classify a sequence of text. 
	Parameters:
		- txt: the sequence of text to be classified
	Returns:
		- r_string: a statement displaying the classification and probability
	""" 

	load_model()

	# evaluate a sample
	evaluation = loaded_model.classify(txt)

	# get probability of the evaluation 
	get_prob = loaded_model.prob_classify(txt)
	prob = round((get_prob.prob(evaluation) * 100))

	# build string to be returned 
	r_string = (str(prob) + "% " + evaluation)

	return r_string
