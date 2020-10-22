from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)


#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")


@app.route('/journals/sophiecarter/')
def scjournal():
    #Flask import uses Jinga to render HTML
    return render_template("scjournal.html")

@app.route('/journals/aditimustafayazhisai/')
def amyjournal():
    #Flask import uses Jinga to render HTML
    return render_template("amyjournal.html")


@app.route('/journals/')
def journal():
    #Flask import uses Jinga to render HTML
    return render_template("scjournal.html")

@app.route('/aboutus/carter/')
def aucarter():
    #Flask import uses Jinga to render HTML
    return render_template("carter.html")

@app.route('/aboutus/aditi/')
def auaditi():
    #Flask import uses Jinga to render HTML
    return render_template("aditi.html")

@app.route('/aboutus/isai/')
def auisai():
    #Flask import uses Jinga to render HTML
    return render_template("aditi.html")

@app.route('/aboutus/sophie/')
def ausophie():
    #Flask import uses Jinga to render HTML
    return render_template("sophie.html")

@app.route('/aboutus/mustafa/')
def aumustafa():
    #Flask import uses Jinga to render HTML
    return render_template("mustafa.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')