from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/calculadora-web', methods=['GET', 'POST'])
def calculadora_flask():
    resultado = ""
    if request.method == 'POST':
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            # Realizar operación matemática
            if operacion == 'suma':
                resultado = num1 + num2
                if resultado == 0:
                    resultado = "La suma es cero."
            elif operacion == 'resta':
                resultado = num1 - num2
                if resultado == 0:
                    resultado = "La resta es cero."
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
                if resultado == 0:
                    resultado = "La multiplicación es cero."
            elif operacion == 'division':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "No se puede dividir entre 0"
        except ValueError:
            resultado = "Por favor ingresa numeros validos."
    
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
