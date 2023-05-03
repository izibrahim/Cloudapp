from flask import Flask, render_template,request
import os
import requests
from collections import OrderedDict
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello this app is deploy to study the Cloud it will count the word in the text if any word repeat it will count the word and display the count of the word'



@app.route('/index')
def countword():
   return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    text = request.form.get('text')
    print(text)  # Extract the value of the 'text' field from the form data
    split_word = text.split()
    convert_to_set = set(split_word)
    countfileone = dict()
    for x in split_word:
      g = split_word.count(x)
      countfileone[x] = g
    
  
#    return f'The text contains {new_dict} words.'
    return render_template('output.html',output=countfileone)


if __name__ == '__main__':
    app.run(debug=True)

'''
Certainly! This line of code is used to count the occurrences of each word in a file.

Here's a step-by-step breakdown of what's happening:

count_word is a variable that contains a single word from the file being processed.
countfileone is a dictionary that will store the word counts.
countfileone.get(count_word, 0) gets the current count for the count_word key in the dictionary. If the key doesn't exist yet, it returns 0.
countfileone.get(count_word, 0) + 1 increments the count for the count_word key by 1.
countfileone[count_word] = countfileone.get(count_word,0) + 1 sets the new count for the count_word key in the dictionary.
So, in summary, this line of code is checking if the count_word key already exists in the dictionary. If it does, the count is incremented by 1. If it doesn't, a new key is created with a count of 1.

I hope that helps! Let me know if you have any further questions.
'''
