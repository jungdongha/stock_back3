from flask import Blueprint, jsonify, request
from app.analysis import cal_data, predict_increase, get_stock_code

main = Blueprint('main', __name__)

@main.route('/api/stock/search', methods=['GET'])
def search_stock():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    result = get_stock_code(keyword)
    return jsonify(result)

@main.route('/api/stock/analyze', methods=['GET'])
def analyze_stock():
    stock_name = request.args.get('stockName')
    interval = request.args.get('interval', 'monthly')
    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400
    
    # stock_code를 얻는 과정 추가
    stock_code = get_stock_code(stock_name)
    if not stock_code:
        return jsonify({"error": "Invalid stock name"}), 400
    
    analysis_result = cal_data(stock_code)  # interval 파라미터 제거
    return jsonify({
        "stockName": stock_name,
        "interval": interval,
        "data": analysis_result
    })

@main.route('/api/stock/predict', methods=['GET'])
def predict_stock():
    stock_name = request.args.get('stockName')
    interval = request.args.get('interval', 'monthly')
    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400
    
    prediction_result = predict_increase(stock_name, interval)
    return jsonify({
        "stockName": stock_name,
        "prediction": prediction_result
    })
