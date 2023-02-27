from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
import numpy as np
from flask import Flask, request, jsonify, render_template

#Initialize the flask App
app = Flask(__name__,static_folder='static')


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict1',methods=['POST'])
def predict1():
    inp = request.form.get("inp")
    #initializing the model
    score = sia.polarity_scores(inp)

    if score["neg"] != 0:
        message = 'Negative'
    else:
        message = 'Positive'
        
    return render_template('index.html', prediction_text=message)
    

if __name__ == "__main__":
    app.run(debug=True)

