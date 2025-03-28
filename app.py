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


