import json

from flask import Blueprint, jsonify

from .controllers import get_random_kanji

api_bp = Blueprint("api", __name__)


@api_bp.route('/', methods=['GET'])
def home_page():
    return "API kanji"


@api_bp.route('/jplt/4', methods=['GET'])
def get_old_jpl4_kanji():
    # Read the JSON file
    with open("json/jplt_4.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(len(data))
        return jsonify(data)


@api_bp.route('/jplt/3', methods=['GET'])
def get_old_jpl3_kanji():
    # Read the JSON file
    with open("json/jplt_3.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(len(data))
        return jsonify(data)


@api_bp.route('/jplt/2', methods=['GET'])
def get_old_jpl2_kanji():
    # Read the JSON file
    with open("json/jplt_2.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(len(data))
        return jsonify(data)


@api_bp.route('/jplt/1', methods=['GET'])
def get_old_jpl1_kanji():
    # Read the JSON file
    with open("json/jplt_1.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        print(len(data))
        return jsonify(data)


@api_bp.route('/jplt/<int:jplt>/random/<int:nombre>', methods=['GET'])
def get_random_jplt_kanji(jplt, nombre):

    return  jsonify(get_random_kanji(jplt, nombre))
