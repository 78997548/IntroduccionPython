from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/causas')
def causas():
    return render_template('causas.html')

if __name__ == '__main__':
    app.run(debug=True)
