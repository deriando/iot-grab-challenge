from flask import Flask
from sqlalchemy.sql.expression import func
from model import iotapp, db, telemetry
from datetime import datetime, timedelta
import time, random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()
db.init_app(app)
datetime_start = datetime.now()

def getRandomBookingIDs(numberToGet):
    teleData = telemetry.query.order_by(func.rand()).limit(numberToGet).all()
    return (teleData)

def insertIOTApp(teleData):
    i = 0
    while i < len(teleData):
        seconds = teleData[i].seconds
        datetime_value = datetime_start + timedelta(seconds=seconds)
        timestamp_value = datetime.now()
        datetimestart_value = str(datetime_start)
        bookingid = teleData[i].bookingid
        bookingidwithtime = f"{bookingid}_{datetimestart_value}"
        accuracy = teleData[i].accuracy
        bearing = teleData[i].bearing
        acceleration_x = teleData[i].acceleration_x
        acceleration_y = teleData[i].acceleration_y
        acceleration_z = teleData[i].acceleration_z
        gyro_x = teleData[i].gyro_x
        gyro_y = teleData[i].gyro_y
        gyro_z = teleData[i].gyro_z
        speed = teleData[i].speed
        speedkmhour = teleData[i].speedkmhour

        insert = iotapp(datetime_value, timestamp_value, datetimestart_value, bookingid, bookingidwithtime, accuracy, bearing, acceleration_x, acceleration_y, acceleration_z, gyro_x, gyro_y, gyro_z, seconds, speed, speedkmhour)
        db.session.add(insert)
        db.session.commit()
        i += 1


if __name__ == "__main__":
    try:
        while True:
            insertIOTApp(getRandomBookingIDs(3))
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"New records inserted at {current_time}")
            time.sleep(random.randrange(2,10))

    except KeyboardInterrupt:
        print('Stopped')