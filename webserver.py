from flask import Flask, render_template, jsonify
from notifications import telegramNotif
import json
from model import iotapp, iotappSchema, db

# flask config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# web config
@app.route("/get/iot")
def getTelemetry():
    with app.app_context():
        iotData = iotapp.query.order_by(iotapp.datetime_value.desc()).limit(3).all()
        iotSchema = iotappSchema(many=True) # used marshmallow's schema
        result = iotSchema.dumps(iotData) # dumps json
        #return result
        return jsonify(result)

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
app.run(debug=True)