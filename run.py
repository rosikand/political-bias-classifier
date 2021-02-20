"""
File: run.py 
-------------------
This is the runner file of the program. 
When executed, the user will be asked for input. This input
is then sent to the training model. The output is printed out.
"""

from pred import predict_text

print('This program classifies a a sequence of text as either "partisan" or "neutral". Enter some text below and see the classification!')

# get user input 
txt = input('Enter text: ')
print(predict_text(txt))