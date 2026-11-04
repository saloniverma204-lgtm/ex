import joblib
from flask import Flask,request,jsonify

app=Flask(__name__)
model=joblib.load("model.pkl")

@app.route("/")
def home():
  return jsonify({"message":"Auto deploy version"})

# @app.route("/predict",methods=["POST"])
# def predict():
#   data=request.get_json()
#   s_l=data["Seplal_length"]
#   s_w=data["sepal_width"]
#   p_l=["petal_length"]
#   p_w=["petal_width"]
#   pred=model.predict([[s_l,s_w,p_l,p_w]])
#   return jsonify({"prediction":pred[0]})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001)