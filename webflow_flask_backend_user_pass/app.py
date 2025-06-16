from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, usuario TEXT, contraseña TEXT)')

@app.route('/api/enviar', methods=['POST'])
def guardar():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contraseña = datos.get('contraseña')

    if not usuario or not contraseña:
        return jsonify({'error': 'Faltan datos'}), 400

    with sqlite3.connect('database.db') as conn:
        conn.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, contraseña))
    return jsonify({'ok': True}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)