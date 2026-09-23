from flask import Flask, jsonify
import os
import random
import faker  # new — for generating fake names

app = Flask(__name__)

GREETINGS = ["Hello", "Hi", "Hey", "Greetings"]

@app.route('/')
def index():
    return jsonify({"service": "shipment-tracker", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/greeting')
def greeting():
    fake = faker.Faker()
    return jsonify({
        "greeting": random.choice(GREETINGS),
        "name": fake.first_name()
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)