from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Secure DevSecOps!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Test change for CI
