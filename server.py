from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    sign_in = False 
    return render_template("index.html", sign_in = sign_in)

@app.route("/user/<username>")
def show(username):
    return f"Hi {username}"

if __name__ == "__main__":
    app.run()

# If flask app runs into some errors, we can add debug = True as an argument for run()
