
from django.shortcuts import render
from flask import Flask, render_template, jsonify, request, render_template

app = Flask(__name__)

# Sample data for demonstration purposes
automobiles = [
    {"id": "1", "brand": "Toyota", "model": "Camry"},
    {"id": "2", "brand": "Honda", "model": "Civic"},
]

# 1) Barcha avtomobillarni ko'rish
@app.route('/avtomobiles', methods=['GET'])
def avtomobiles_list():
    return render_template('avtomobiles_list.html', avtomobiles=automobiles)

# 2) Avtomobil ma'lumotlarini olish
@app.route('/avtomobiles/<string:id>', methods=['GET'])
def avtomobile_detail(id):
    automobile = next((car for car in automobiles if car["id"] == id), None)
    if automobile:
        return render_template('avtomobile_detail.html', automobile=automobile)
    else:
        return jsonify({"xabar": "Avtomobil topilmadi"}), 404

# 3) Avtomobilni o'chirish
@app.route('/avtomobiles/<string:id>/delete', methods=['GET'])
def delete_automobile(id):
    global automobiles
    automobiles = [car for car in automobiles if car["id"] != id]
    return jsonify({"xabar": "Avtomobil muvaffaqiyatli o'chirildi"})

# 4) Yangi avtomobil qo'shish sahifasi
@app.route('/avtomobiles/new', methods=['GET'])
def create_automobile_page():
    return render_template('create_automobile.html')

# Yangi avtomobil qo'shish
@app.route('/avtomobiles/create', methods=['POST'])
def create_automobile():
    data = request.form
    new_automobile = {
        "id": str(len(automobiles) + 1),
        "brand": data.get("brand"),
        "model": data.get("model")
    }
    automobiles.append(new_automobile)
    return jsonify(new_automobile), 201

if __name__ == '__main__':
    app.run(debug=True)
