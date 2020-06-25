from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import DOUBLE

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class telemetry(db.Model):
    __tablename__ = "telemetry"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bookingid = db.Column(db.Text, nullable=False)
    accuracy = db.Column(db.Float)
    bearing = db.Column(db.Float)
    acceleration_x = db.Column(DOUBLE)
    acceleration_y = db.Column(DOUBLE)
    acceleration_z = db.Column(DOUBLE)
    gyro_x = db.Column(DOUBLE)
    gyro_y = db.Column(DOUBLE)
    gyro_z = db.Column(DOUBLE)
    seconds = db.Column(db.Integer)
    speed = db.Column(DOUBLE)
    speedkmhour = db.Column(DOUBLE)
    def __repr__(self):
        return "['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s'], ['%s']" % (
            self.id, self.bookingid, self.accuracy, self.bearing, self.acceleration_x, self.acceleration_y, self.acceleration_z, 
            self.gyro_x, self.gyro_y, self.gyro_z, self.seconds, self.speed, self.speedkmhour)

""" class socketFeed(db.Model):
    __tablename__ = "socketfeed"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bookingid = db.Column(db.Text, nullable=False)
    startdatetime_value = db.Column(db.DateTime)
    enddatetime_value = db.Column(db.DateTime)
    timestamp_value = db.Column(db.Time)
    def __repr__(self):
        return "[bookingid='%s'], [startdatetime_value='%s'], [enddatetime_value='%s'], [timestamp_value='%s']" % (
            self.bookingid, self.startdatetime_value, self.enddatetime_value, self.timestamp_value) """