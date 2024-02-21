from flask import Flask, request, jsonify, render_template
from gcp_wrap import try_gemi

app = Flask(__name__)

# Cloud project id.
PROJECT_ID = "bjss-hack-7th-feb"  # @param {type:"string"}

# The region you want to launch jobs in.
REGION = "europe-west2"  # @param {type:"string"}

# The Cloud Storage bucket for storing experiments output. Fill it without the 'gs://' prefix.
GCS_BUCKET = (
    "cloud-ai-platform-1be12f39-2968-407c-9114-8345e0f1e1de"  # @param {type:"string"}
)

# The service account for deploying fine tuned model.
SERVICE_ACCOUNT = (
    "imggen@bjss-hack-7th-feb.iam.gserviceaccount.com"  # @param {type:"string"}
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/user_story")
def user_story():
    if request.method == "POST":
        ac = request.json.get("ac")


@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text-input']
    # response = interview(0, PROJECT_ID, REGION)
    response = try_gemi(text)
    # response = response.replace('**',  '\n')
    return response


if __name__ == "__main__":
    app.run(port=5001, debug=True)