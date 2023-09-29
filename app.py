from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # Lógica para lidar com os dados recebidos e salvar no TinyDB
        # ...
        new_data = request.json.get('data')  # Assume que os dados são enviados como {"data": "exemplo"}
        db.insert({'data': new_data})
        return jsonify({"message": "Data saved successfully"})
    else:
        # Lógica para retornar os dados do TinyDB
        # ...
        data_from_tinydb = db.all()
        return jsonify({"data": data_from_tinydb})

if __name__ == '__main__':
    app.run(debug=True)