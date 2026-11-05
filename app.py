import numpy as np
from flask import Flask
from flask import request
from flask import render_template
import pickle

flask_app =Flask(__name__, template_folder='templates')
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    int_features=[0]*18

    i_features = [int(x) for x in request.form.values()]

    for i in i_features[3:]:
        int_features[i]=1
    i_features=i_features[:3]+ int_features
    final_features=np.array(i_features).reshape(1,-1)

    prediction = model.predict(final_features)
    output=round(prediction[0],0)


    print(prediction)
    return render_template("index.html", prediction_text="Predicted number of likes:  {}".format(output))

if __name__ == "__main__":
    flask_app.run(debug=True)
