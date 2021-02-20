![header image](https://drive.google.com/uc?export=download&id=1tbbhZWk__GcjI8lExRTdX-jrhItqKOo4)

## Summary

This program classifies a sequence of text as either "partisan" or "neutral" using a machine learning and sentiment analysis. 

## Model and data

The trained model is stored as pickled file in `compressed_model.pkl`.  Note that the intitial model training was done as part of an extension project for my computer science class. Therefore, I cannot release the code where the model was trained. In short, the model is a Naive Bayes Classifier trained on `data/train.csv` and evaluated on `data/test.csv`. The Textblob library was used. The original data was adapted from [here](https://www.kaggle.com/crowdflower/political-social-media-posts) and was manually preprocessed. 

## Running instructions

If you would like to run this program, please download the repository and follow these steps: 

1. Install the necessary dependencies: `$ pip install -r requirements.txt`. 
2. Install Textblob's corpora: `$ python -m textblob.download_corpora`. 
3. Run `run.py` (`$ python run.py`) and follow the directions within the program. 