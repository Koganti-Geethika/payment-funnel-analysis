from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("../data/payments.csv")

@app.route("/")
def home():
    return {
        "message": "Payment Funnel API is running",
        "endpoint": "/funnel",
        "full_url": "http://localhost:5000/funnel"
    }

@app.route("/funnel")
def funnel():
    funnel_counts = df.groupby("step")["user_id"].nunique().reset_index()
    return jsonify(funnel_counts.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
