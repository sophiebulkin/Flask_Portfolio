from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/aboutus/')
def journal():
    #Flask import uses Jinga to render HTML
    return render_template("aboutus.html")

@app.route('/contents/')
def contents():
    #Flask import uses Jinga to render HTML
    return render_template("contents.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')
