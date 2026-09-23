from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"service": "shipment-tracker", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

#Deployed API endpoints for shipment tracking

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)