from flask import Flask, render_template

app = Flask(__name__)

@app.route('/consecuencias')
def consecuencias():
    return render_template('consecuencias.html')


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/causas')
def causas():
    return render_template('causa.html')

if __name__ == '__main__':
    app.run(debug=True)
