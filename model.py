from sqlalchemy.dialects.mysql import DOUBLE, INTEGER, FLOAT, TEXT, DATETIME, TIMESTAMP, VARCHAR, MEDIUMTEXT
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class iotapp(db.Model):
    __tablename__ = "iotapp"
    id = db.Column(INTEGER, primary_key=True, nullable=False)
    datetime_value = db.Column(DATETIME)
    timestamp_value = db.Column(TIMESTAMP)
    datetimestart_value = db.Column(VARCHAR(length=255))
    bookingid = db.Column(MEDIUMTEXT, nullable=False)
    bookingidwithtime = db.Column(MEDIUMTEXT)
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
    def __init__(self, datetime_value, timestamp_value, datetimestart_value, bookingid, bookingidwithtime, accuracy, bearing, 
    acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, seconds, speed, speedkmhour):
        self.datetime_value = datetime_value
        self.timestamp_value = timestamp_value
        self.datetimestart_value = datetimestart_value
        self.bookingid = bookingid
        self.bookingidwithtime = bookingidwithtime
        self.accuracy = accuracy
        self.bearing = bearing
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.acceleration_z = acceleration_z
        self.gyro_x = gyro_x
        self.gyro_y = gyro_y
        self.gyro_z = gyro_z
        self.seconds = seconds
        self.speed = speed
        self.speedkmhour = speedkmhour 


class iotappSchema(Schema):
    id = fields.Int()
    datetime_value = fields.String()
    timestamp_value = fields.String()
    datetimestart_value = fields.String()
    bookingid = fields.String()
    bookingidwithtime = fields.String()
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


class telemetry(db.Model):
    __tablename__ = "telemetry"
    id = db.Column(INTEGER, primary_key=True, nullable=False)
    bookingid = db.Column(MEDIUMTEXT, nullable=False)
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
    
    '''
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    '''

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