from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from model import telemetry

app = Flask(__name__)

# flask config
#app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Add administrative views here
""" class socketAdmin(ModelView):
    form_columns = ["bookingid", "startdatetime_value", "enddatetime_value", "timestamp_value"] """
    
#admin.add_view(ModelView(model.socketFeed, db.session))

@app.route("/get/telemetry")
def getTelemetry():
    for i in model.telemetry.query.count():
        id = telemetry.query.filter_by(id=i).first()


@app.route("/")
def index():
    return render_template('index.html')


app.run()