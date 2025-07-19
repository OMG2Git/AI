from flask import Blueprint, request, jsonify
from models.new_abc import analyze_with_groq, verify_with_gemini, combine_analysis

api_server2 = Blueprint('api_server2', __name__)

@api_server2.route('/api/llm', methods=['POST'])
def llm_endpoint():
    data = request.get_json()
    url_or_text = data.get('url') or data.get('text')
    groq_result = analyze_with_groq(url_or_text)
    gemini_result = verify_with_gemini(groq_result)
    combined = combine_analysis(groq_result, gemini_result)
    return jsonify(combined)