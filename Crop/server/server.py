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

@app.route('/get_crop_name', methods=['GET', 'POST'])
def  get_crop_name():
    n = int(request.form['n'])
    p = int(request.form['p'])
    k = int(request.form['k'])
    temperature=float(request.form['temperature'])
    humidity=float(request.form['humidity'])
    ph= float(request.form['ph'])
    rainfall=float(request.form['rainfall'])

    response = jsonify({
        'crop_name': util.get_crop_name(n,p,k,temperature,humidity,ph,rainfall)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response






if __name__ == "__main__":
 print("Starting Python Flask Server For predicting Crop...")
 util.load_saved_artifacts()
 app.run()