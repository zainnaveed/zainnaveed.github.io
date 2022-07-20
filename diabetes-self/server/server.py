
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_data_columns', methods=['GET'])
def  get_data_columns():
    response = jsonify({
        'data_columns': util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_diabetes', methods=['GET','POST'])
def get_diabetes():
    pregnancies= int(request.form["pregnancies"])
    glucose= int(request.form["glucose"])
    bloodpressure = int(request.form["bloodpressure"])
    skinthickness=float(request.form["skinthickness"])
    insulin=int(request.form["insulin"])
    bmi= float(request.form["bmi"])
    diabetespedigreefunction=float(request.form["diabetespedigreefunction"])
    age=int(request.form["age"])
    response = jsonify({
        'diabetes': util.get_diabetes(pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age)})
    
    response.headers.add('Access-Control-Allow-Origin', '*')

    return(response)


if __name__ == "__main__":
 print("Starting Python Flask Server For predicting diabetes...")
 util.load_saved_artifacts()
 app.run()