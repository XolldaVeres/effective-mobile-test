from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Backend! Docker + Nginx works!"

@app.route('/api')
def api():
    return jsonify({"status": "ok", "message": "Docker + Nginx works!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
