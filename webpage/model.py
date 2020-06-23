from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#s = sql.select(telemetry)
#tele = conn.execute(s)

""" class socketFeed(Base):
    __tablename__ = "socketfeed"
    id = Column(Integer, primary_key=True)
    bookingid = Column(Text)
    startdatetime_value = Column(DateTime)
    enddatetime_value = Column(DateTime)
    timestamp_value = Column(Time)
    def __repr__(self):
        return "<socketFeed(bookid='%s', startdatetime='%s', enddatetime_value='%s', timestamp_value='%s'" % (
            self.bookid, self.startdatetime_value, self.enddatetime_value, self.timestamp_value)
 """

""" class telemetry(Base):
    __tablename__ = "telemetry"
    id = Column(Integer, primary_key=True)
    bookingid = Column(Text)
    accuracy = Column(Float)
    bearing = Column(Float)
    acceleration_x = Column(Double)
    acceleration_y = Column(Double)
    acceleration_z = Column(Double)
    gyro_x = Column(Double)
    gyro_y = Column(Double)
    gyro_z = Column(Double)
    seconds = Column(Integer)
    speed = Column(Double)
    speedkmhour = Column(Double) """

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class socketFeed(db.Model):
    __tablename__ = "socketfeed"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    bookingid = db.Column(db.Text, nullable=False)
    startdatetime_value = db.Column(db.DateTime)
    enddatetime_value = db.Column(db.DateTime)
    timestamp_value = db.Column(db.Time)
    def __repr__(self):
        return "<socketFeed(bookingid='%s', startdatetime_value='%s', enddatetime_value='%s', timestamp_value='%s'" % (
            self.bookingid, self.startdatetime_value, self.enddatetime_value, self.timestamp_value)