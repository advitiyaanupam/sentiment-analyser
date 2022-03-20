from flask import Flask,request,json
from utility import sentence_lookup,pred_class
import pickle
import tensorflow as tf
import re


app = Flask(__name__)

sentiment_model_path = "sentiment_analyser.pkl" #"C:\\Users\\anupam.a.yadav\\Documents\\deployment\\sentiment_analyser.pkl" #
sentiment_model = pickle.load(open(sentiment_model_path,'rb'))

@app.route('/ping',methods=['GET'])
def check_health():
    return "pong"

@app.route('/predict',methods=['POST'])
def get_test_params():
    params = json.loads(request.data.decode('utf8'))
    print("params",params)

    if params.get("id"):
        sentence = sentence_lookup(params["id"])
        print("sentence is -- ",sentence)
        if sentence != "Please enter a valid key":
            pred = sentiment_model.predict([sentence])
            pred = pred_class(pred)
        else:
            pred = sentence

    elif params.get("sentence"):
        sen = params["sentence"].strip()
        sen = re.sub('[@_!#$%^&*()<>?/\|}{~:]', '',sen)
        if len(sen)==0:
            pred = "Please enter a valid sentence"
        else:
            pred = sentiment_model.predict([sen])
            pred = pred_class(pred)
        
    else:
       pred =  "Invalid Parameters"

    return {"result":pred}

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=8848)
