from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Backend! Docker + Nginx works!"

@app.route('/api')
def api():
    return jsonify({"status": "ok", "message": "Docker + Nginx works!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
