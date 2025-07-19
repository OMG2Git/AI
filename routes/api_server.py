from flask import Blueprint, request, jsonify
from models.news_authenticity_checker import run_checker

api_server = Blueprint('api_server', __name__)

@api_server.route('/api/check', methods=['POST'])
def check_news():
    data = request.get_json()
    url = data.get('url')
    text = data.get('text')
    result = run_checker(url=url, text=text)
    return jsonify(result)