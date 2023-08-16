# import pickle
# import warnings

# # Temporarily ignore the specified warning
# with warnings.catch_warnings():
#     warnings.simplefilter("ignore", category=UserWarning)  # Replace with the actual warning class


# file = "pickel_model.pkl"
# with open(file, 'rb') as f1:  
#     logit = pickle.load(f1)
# f1.close()

# urls = []
# new_url = input("Enter a new URL: ")

# # Append the new URL to the list
# urls.append(new_url)

# file = "pickel_vector.pkl"
# with open(file, 'rb') as f2:  
#     vectorizer = pickle.load(f2)
# f2.close()
# vectorizer = vectorizer
# x = vectorizer.transform(urls)
# #score = lgr.score(x_test, y_test)
# y_predict = logit.predict(x)

# print(y_predict[0])

import pickle
import warnings
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pickled model and vectorizer
with open("pickel_model.pkl", "rb") as f1:
    logit = pickle.load(f1)

with open("pickel_vector.pkl", "rb") as f2:
    vectorizer = pickle.load(f2)

# Ignore the specified warning temporarily
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        new_url = data['url']
        x = vectorizer.transform([new_url])
        y_predict = logit.predict(x)
        result = {'prediction': y_predict[0]}
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
