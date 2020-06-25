from flask import Flask, render_template, jsonify
from models import *
from notifications import telegramNotif
import json

telegramNotif('test', 'body')

@app.route("/get/telemetry")
def getTelemetry():
    with app.app_context():
        teleData = telemetry.query.filter_by(id=1).all()
        teleSchema = telemetrySchema(many=True)
        result = teleSchema.dumps(teleData)
        #return {'data': result}
        return jsonify({'data': result})

@app.route("/tables.html")
def tables():
    return render_template('tables.html')

@app.route("/index.html")
def index2():
    return render_template('index.html')

@app.route("/")
def index():
    return render_template('index.html')

#print(getTelemetry())
#app.run(debug=True)