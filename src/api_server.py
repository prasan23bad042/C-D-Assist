from flask import Flask, request, jsonify
from flask_cors import CORS  
from bug_fixer import fix_python_code

app = Flask(__name__)
CORS(app) 

@app.route('/api/bugfix', methods=['POST'])
def bugfix():
    try:
        data = request.get_json()
        code = data.get("code", "")
        if not code:
            return jsonify({"error": "No code provided"}), 400

        fixed_code, logs = fix_python_code(code)
        return jsonify({
            "fixed_code": fixed_code,
            "logs": logs
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000,use_reloader=False)
