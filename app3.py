from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Superstore API!"})

@app.route('/data')
def get_data():
    df = pd.read_excel('superstore.xls')
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
