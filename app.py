from flask import Flask, render_template, request, send_from_directory, jsonify
import requests
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# ----------------------------
# CONFIG - Replace these values
# ----------------------------

API_KEY = "BHQwK93PebW0Cs5Gf36GUqwMYnjxN6qyMxc0T1d46NYL"

DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/6b6c9b40-1066-4e05-9e6b-02589de9eafa/predictions?version=2021-05-01"

def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": API_KEY
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(url, data=data, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json()["access_token"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        pclass = int(request.form.get("Pclass"))
        sex = request.form.get("Sex")
        age = float(request.form.get("Age") or 0)
        sibsp = int(request.form.get("SibSp") or 0)
        parch = int(request.form.get("Parch") or 0)
        fare = float(request.form.get("Fare") or 0.0)
        embarked = request.form.get("Embarked")
    except Exception as e:
        return jsonify(error=f"Invalid input: {e}"), 400

    passenger_id = 999
    name = "Demo Passenger"
    ticket = "000000"
    cabin = ""

    payload = {
        "input_data": [{
            "fields": [
                "PassengerId", "Pclass", "Name", "Sex", "Age",
                "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"
            ],
            "values": [[
                passenger_id, pclass, name, sex, age,
                sibsp, parch, ticket, fare, cabin, embarked
            ]]
        }]
    }

    try:
        token = get_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }
        r = requests.post(DEPLOYMENT_URL, json=payload, headers=headers, timeout=20)
        r.raise_for_status()
        data = r.json()

        # parse based on typical AutoAI response structure
        prediction = int(data["predictions"][0]["values"][0][0])
        # probability -> usually values[0][1] is [prob_no, prob_yes]
        prob_yes = float(data["predictions"][0]["values"][0][1][1]) * 100.0
        return jsonify(prediction=prediction, probability=round(prob_yes, 2))

    except requests.exceptions.RequestException as e:
        try:
            raw = r.text
        except:
            raw = ""
        return jsonify(error=f"Request error: {e}", raw=raw), 500
    except Exception as e:
        return jsonify(error=str(e)), 500

# route to serve the report if user clicks "Project Report"
@app.route("/report")
def report():
    report_local = os.path.join(app.static_folder, "assets", "PREDICTION_REPORT_26_NOV.pdf")
    if os.path.exists(report_local):
        return send_from_directory(os.path.join(app.static_folder, "assets"), "PREDICTION_REPORT_26_NOV.pdf")
    return "Report not found", 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
