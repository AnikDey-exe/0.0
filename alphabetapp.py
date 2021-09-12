from flask import Flask, jsonify, request

from alphabetprediction import get_pred

app = Flask(__name__)

@app.route("/predict-alphabet", methods=["POST"])

def predict_data():
    image = request.files.get('alphabet')
    prediction = get_pred(image)

    return jsonify({
        "prediction": prediction
    }), 200

if __name__ == "__main__":
    app.run(debug=True)