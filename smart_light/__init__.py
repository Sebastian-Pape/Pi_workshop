from flask import Flask, jsonify, render_template

from . import control

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/light_on', methods=['POST'])
def light_on():
    control.light_on()
    return jsonify(status='success')



@app.route('/light_off', methods=['POST'])
def light_off():
    control.light_off()
    return jsonify(status='success')



@app.route('/an', methods=['POST'])
def an():
    control.an()
    return jsonify(status='success')



@app.route('/aus', methods=['POST'])
def aus():
    control.aus()
    return jsonify(status='success')
