from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/check')
def check_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Missing URL param"}), 400
    try:
        response = requests.get(url, timeout=5)
        return jsonify({"url": url, "status_code": response.status_code})
    except Exception as e:
        return jsonify({"url": url, "error": str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

