from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open("adaboost_model.pkl", "rb"))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    
     if request.method == 'POST':
         
        Age= int(request.form["Age"])
        
        BI_RADS_assessment=str(request.form["BI_RADS_assessment"])
        if (BI_RADS_assessment=="Incomplete - (0)"):
            BI_RADS_assessment=0
            pass
        
        elif (BI_RADS_assessment=="Negative - (1)"):
            BI_RADS_assessment=1.0
            pass
            
        elif (BI_RADS_assessment=="Benign Findings - (2)"):
            BI_RADS_assessment=2.0
            pass
        
        elif (BI_RADS_assessment=="Probably Benign - (3)"):
            BI_RADS_assessment=3.0
            pass
            
        elif (BI_RADS_assessment=="Suspicious Abnormally- (4)"):
            BI_RADS_assessment=4.0
            pass
            
        elif (BI_RADS_assessment=="Highly Suspicious of Malignancy-(5)"):
            BI_RADS_assessment=5.0
            pass
            
        elif (BI_RADS_assessment=="Known Biopsy with proven malignancy - (6)"):
            BI_RADS_assessment=6.0
            pass
        
        else:
            return "Invalid Entry"
            
        
            
        Margin= str(request.form["Margin"])
        if (Margin=="Circumscribed - (1)"):
            Margin=1.0
            pass
        
        elif (Margin=="Microlobulated - (2)"):
            Margin=2.0
            pass
            
        elif (Margin=="Obscured - (3)"):
            Margin=3.0
            pass
            
        elif (Margin=="Ill-Defined - (4)"):
            Margin=4.0
            pass
            
        elif (Margin=="Spiculated(nominal) - (5)"):
            Margin=5.0
            pass
        else:
            return "Invalid Entry"
            
        
        
        Shape = str(request.form["Shape"])
        if (Shape=="Round - (1)"):
            Shapes =1.0
            pass
        elif (Shape=="Oval - (2)"):
            Shapes=2.0
            pass
        elif (Shape=="Lobular - (3)"):
            Shapes=3.0
            pass
        elif (Shape=="Irregular(nominal) - (4)"):
            Shapes=4.0
            pass
        else:
            return "Invalid Entry"
      
            
            
        Density = str(request.form["Density"])
        if (Density=="High - (1)"):
            Density=1.0
            pass
        elif (Density =="Iso - (2)"):
            Density=2.0
            pass
        elif (Density=="Low - (3)"):
            Density=3.0
            pass
        elif ( Density =="Fat-Containing(Ordinal) - (4)"):
            Density=4.0
            pass
        else:
            return "Invalid Entry"
        
        
        prediction= model.predict([[ BI_RADS_assessment,Age,Shapes,Margin,Density]])
    
        if prediction==1:
           return render_template('index.html', Positive="🙁☹MALIGNANT --- PLEASE HAVE DOCTOR'S ADVICE☹🙁")

        else:
            return render_template('index.html', Negative="😀BENIGN --- NO NEED TO WORRY, BE HAPPY😀")
                
if __name__=="__main__":
    app.run(debug=True)
