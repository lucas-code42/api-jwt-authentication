from flask import Flask, request, jsonify, request
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)

secret_key = "1234"

@app.route('/secret', methods=["GET"])
def secret_route():
    raw_token = request.headers.get("Authorization")
    if not raw_token:
        return jsonify({
            "error": "Nao autorizado"
        }), 401
    
    print(raw_token)
    token = raw_token.split()[1]
    try:
        token_information = jwt.decode(token, key=secret_key, algorithms="HS256")
        print(token_information)
        return jsonify({
            "msg": "autorizado"
        }), 200
    except:
        return jsonify({
            "error": "Nao autorizado"
        }), 401


@app.route('/auth', methods=["POST"])
def auth_token():
    token = jwt.encode({'exp': datetime.utcnow() + timedelta(seconds=40)}, key=secret_key, algorithm="HS256")
    return jsonify({
        'token': token
    }, 200)

if __name__ == "__main__":
    app.run(debug=True)