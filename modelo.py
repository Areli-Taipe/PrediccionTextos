# modelo.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Cargar datos
df = pd.read_csv('textos.csv')

X = df['texto']
y = df['categoria']

# Dividir
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocesamiento básico + vectorización
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Entrenamiento
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Evaluación
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Guardar modelo y vectorizador
joblib.dump(model, 'modelo_entrenado.pkl')
joblib.dump(vectorizer, 'vectorizador.pkl')

print(df['categoria'].value_counts())