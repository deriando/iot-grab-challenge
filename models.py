from flask import Flask
from sqlalchemy.dialects.mysql import DOUBLE, INTEGER, FLOAT, TEXT
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class telemetry(db.Model):
    __tablename__ = "telemetry"
    id = db.Column(INTEGER, primary_key=True, nullable=False)
    bookingid = db.Column(TEXT, nullable=False)
    accuracy = db.Column(FLOAT)
    bearing = db.Column(FLOAT)
    acceleration_x = db.Column(DOUBLE)
    acceleration_y = db.Column(DOUBLE)
    acceleration_z = db.Column(DOUBLE)
    gyro_x = db.Column(DOUBLE)
    gyro_y = db.Column(DOUBLE)
    gyro_z = db.Column(DOUBLE)
    seconds = db.Column(INTEGER)
    speed = db.Column(DOUBLE)
    speedkmhour = db.Column(DOUBLE)
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    '''
    def __repr__(self):
        return {
            'id'                : self.id,
            'bookingid'         : self.bookingid,
            'accuracy'          : self.accuracy,
            'bearing'           : self.bearing,
            'acceleration_x'    : self.acceleration_x,
            'acceleration_y'    : self.acceleration_y,
            'acceleration_z'    : self.acceleration_z,
            'gyro_x'            : self.gyro_x,
            'gyro_y'            : self.gyro_y,
            'gyro_z'            : self.gyro_z,
            'seconds'           : self.seconds,
            'speed'             : self.speed,
            'speedkmhour'       : self.speedkmhour
        }'''

class telemetrySchema(Schema):
    id = fields.Int()
    bookingid = fields.String()
    accuracy = fields.Float()
    bearing = fields.Float()
    acceleration_x = fields.Float()
    acceleration_y = fields.Float()
    acceleration_z = fields.Float()
    gyro_x = fields.Float()
    gyro_y = fields.Float()
    gyro_z = fields.Float()
    seconds = fields.Int()
    speed = fields.Float()
    speedkmhour = fields.Float()