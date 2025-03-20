from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

#Comentario 1
#Comentario 2
#COMENTARIO DE CONEXION BRAYAN
#Comentario 3 Will
#20/03/2025 07:00
#CAMBIO 7:46
