import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('gas.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    for rendering the results on the HTML GUI 
    '''
    x_test=[[int(x) for x in request.form.values()]]

    prediction=model.predict(x_test)
    print(prediction)
    pred=prediction[[0]]
    #output=np.round(pred[0],3)
    #output=str(output)+'$dollars'

    return render_template('index.html',prediction_text='Gas price is{} Dollars'.format(pred))
if __name__=="__main__":
    app.run(debug=True)