from flask import Flask, render_template
#from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import model

app = Flask(__name__)

# flask config
#app.config['FLASK_ADMIN_SWATCH'] = 'flatly'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://iotuser:iotpassword@127.0.0.1:3306/iotdatabase"

#admin = Admin(app, name='microblog', template_mode='bootstrap3')
db = SQLAlchemy(app)


# Add administrative views here
""" class socketAdmin(ModelView):
    form_columns = ["bookingid", "startdatetime_value", "enddatetime_value", "timestamp_value"] """
    
#admin.add_view(ModelView(model.socketFeed, db.session))


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


app.run()