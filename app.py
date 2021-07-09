from flask import Flask,request,render_template
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np

app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def main():
    if request.method=='POST':
        religious=float(request.form['religious'])
        age=float(request.form['age'])
        marriage_rating=float(request.form['marriage_rating'])
        years_married=float(request.form['years_married'])
        children=float(request.form['children'])
        occupation=float(request.form['occupation'])
        education=float(request.form['education'])
        hus_occupation=float(request.form['hus_occupation'])
        data=[marriage_rating,age,years_married,children,religious,education,occupation,hus_occupation]
        print(data)
        data = np.array(data)
        data=data.reshape(1,-1)
        scaler=StandardScaler()
        data=scaler.fit_transform(data)
        print(data)
        model=pickle.load(open('martialModel.pickle','rb'))
        y=model.predict(data)
        print("Y",y[0])
        if y:
            result="Women have atleat one affairs."
        else:
            result="Women have no affairs."
        return render_template('success.html',result=result)
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)