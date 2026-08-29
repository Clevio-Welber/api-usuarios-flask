from flask import Flask, jsonify
from routes.users import users_bp

app = Flask(__name__)

app.register_blueprint(users_bp)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API conectada e funcionando"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )