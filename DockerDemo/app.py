from flask import Flask
import os
import base64

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

your_name = "Your Name Here" # TODO: Replace with your name
secret_message = "Q29udGFpbmVyc0FyZUlzb2xhdGVkCg=="

@app.route("/")
def hello():
    return "Hello, {}!\n".format(your_name)

@app.route("/secret")
def secret():
    return "The passphrase is: {}\n".format(base64.b64decode(secret_message).decode('utf-8'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)