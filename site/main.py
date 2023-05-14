from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/humidity')
def humidity():
    return render_template('humidite.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/carbone')
def carbone():
    return render_template('carbone.html')


if __name__ == '__main__':

    app.run(debug=True)