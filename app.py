# app.py
import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Cargar modelo y vectorizador previamente entrenados
model = joblib.load('modelo_entrenado.pkl')
vectorizer = joblib.load('vectorizador.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    texto = data.get('texto', '')

    if not texto:
        return jsonify({'prediction': 'Texto vacío'}), 400

    vector = vectorizer.transform([texto])
    prediccion = model.predict(vector)[0]

    return jsonify({'prediction': prediccion})

if __name__ == '__main__':
    app.run(debug=True)