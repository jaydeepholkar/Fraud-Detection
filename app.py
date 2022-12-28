from flask import Flask, render_template,request
import pandas as pd
import numpy as np
app = Flask(__name__)
import pickle
'''def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)'''

model = pickle.load(open("Fraud_detection_dep.pkl",'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guest', methods =["post"])
def Guest():
    Category = request.form["Category"]
    Name_Grocery = request.form["Name_Grocery"] 
    Item_Number = request.form["Item_Number"]
    Quan_send_by_vendor = request.form["Quan_send_by_vendor"]
    Quan_rec_by_procurement = request.form["Quan_rec_by_procurement"]
    Quan_send_by_procurement= request.form["Quan_send_by_procurement"]
    Unit_Purchase_Price = request.form["Unit_Purchase_Price"]
    Unit_Selling_price = request.form["Unit_Selling_price"]
    Eligibility_Criteria = request.form["Eligibility_Criteria"]
    Total_Selling_price = request.form["Total_Selling_price"]
    
    data  = [[Category, Name_Grocery, Item_Number, Quan_send_by_vendor, Quan_rec_by_procurement, Quan_send_by_procurement, Unit_Purchase_Price, Unit_Selling_price, Eligibility_Criteria, Total_Selling_price]]
              
    data1 = np.array(data, dtype=float)
                    
    prediction = model.predict(data1)
    prediction = prediction[0]
    
    return render_template("result.html",y ="Result is" + " " + str(prediction))

if __name__ == '__main__':
    app.run(debug = True)
    