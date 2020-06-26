from flask import Flask, render_template, jsonify
from notifications import telegramNotif
import json
from model import telemetrySchema, telemetry, db

# flask config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# web config
@app.route("/get/telemetry")
def getTelemetry():
    with app.app_context():
        teleData = telemetry.query.filter_by(id=1).all()
        teleSchema = telemetrySchema(many=True) # used marshmallow's schema
        result = teleSchema.dumps(teleData) # dumps json
        #return teleData
        #return jsonify({'data': result})

@app.route("/tables.html")
def tables():
    return render_template('tables.html')

@app.route("/index.html")
def index2():
    return render_template('index.html')

@app.route("/")
def index():
    return render_template('index.html')

#print(len(getTelemetry()))
#app.run(debug=True)