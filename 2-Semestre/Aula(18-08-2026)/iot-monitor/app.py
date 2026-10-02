from flask import Flask, jsonify

app = Flask(__name__)

# Simulacao de dados de sensor IoT de uma linha de producao
@app.route('/')
def status():
    return 'SENAI Tech DevOps | Aluno: Matheus Raiano'

@app.route('/sensor')
def sensor_data():
    return jsonify({
        'linha': 'Linha-A1',
        'sensor': 'Temperatura',
        'valor': 72.4,
        'unidade': 'Celsius',
        'status': 'NORMAL',
        'aluno': '<Coloque seu nome>'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')