from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

df=pd.read_csv("House_Rent_Dataset.csv")
df.drop(columns=["Posted On","Point of Contact","Area Locality"],inplace=True)
df_encoded=pd.get_dummies(df,columns=['Floor','Area Type','City','Furnishing Status','Tenant Preferred'])

y=df_encoded['Rent']
X=df_encoded.drop(columns=['Rent'])

model=LinearRegression()
model.fit(X,y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    bhk=int(request.form.get('bhk'))
    size=int(request.form.get('size'))
    bath=int(request.form.get('bathroom'))
    flr=request.form.get('floor')
    ar=request.form.get('area')
    city=request.form.get('city')
    furn=request.form.get('f')
    ten=request.form.get('t')

    input_dict={'BHK':bhk,'Size':size,'Bathroom':bath,'Floor':flr,'Area Type':ar,'City':city,'Furnishing Status':furn,'Tenant Preferred':ten}

    input_df=pd.DataFrame([input_dict])
    input_encoded=pd.get_dummies(input_df)
    input_encoded=input_encoded.reindex(columns=X.columns,fill_value=0)
    predicted_rent=model.predict(input_encoded)[0]
    return render_template('result.html',pred=int(predicted_rent))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
