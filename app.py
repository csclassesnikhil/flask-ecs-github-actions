from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello from Flask!"}

@app.route("/hello")
def home1():
    return "hello master developer"    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
