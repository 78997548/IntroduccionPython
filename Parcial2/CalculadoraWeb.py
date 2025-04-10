from flask  import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_AMODIFICATIONS'] = False

db = SQLAlchemy(app)
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)



@app.route('/crear-articulo', methods=['GET','POST'])
def crear_articulo():
    
    # PROCESAR EL FORMULARIO
    if request.method == 'POST':
        num1 = float(request.form('num1'))
        num2 = float(request.form('num2'))
        operacion = request.form('operacion')

        if operacion == 'suma':
            resultado = num1 + num2
        
        
     
#get que recibe informacion
#post q envia informacion
#patch que modifica parcialmente la info
#put q modifica completamente la info
#delete q elimina la info

    return '''
    <h1>Calculador</h1>
    <form method="POST">
    <input type="number" name="num1" placeholder="Primer Numero"><br>
    <input type="number" name="num2" placeholder="Segundo Numero"><br>
    <select name="operacion">
    <button type="submit">Crear</button>
    </form>
    '''

@app.route('/articulo/<int:articulo_id>')
def articulo(articulo_id):
    return f"articulo {articulo_id}"


if __name__ == "__main__":
    app.run(debug=True)