from flask import Flask, request, jsonify
from flask_cors import CORS
from bugfix_model.fix_code import fix_code

app = Flask(__name__)
CORS(app)  

@app.route('/api/bugfix', methods=['POST'])
def bugfix():
    data = request.get_json()
    code = data.get("code")

    if not code:
        return jsonify({"error": "No code provided."}), 400

    try:
        fixed_code, logs = fix_code(code)
        return jsonify({
            "fixed_code": fixed_code,
            "logs": logs or "No issues detected."
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
