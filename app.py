from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def F1():
    return render_template("f1.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final = [np.array(int_features)]
    print(int_features)
    print(final)
    prediction = model.predict_proba(final)
    output = '{0:.{1}f}'.format(prediction[0][1], 2)

    if output > str(0.5):
        return render_template('f1.html', pred='Probability of winning is High.\n Score :{}'.format(output))
    else:
        return render_template('f1.html', pred='Probability of winning is Low.\n Score : {}'.format(output))


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)
