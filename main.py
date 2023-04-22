import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "StudyNetwork.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
#-------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------------
#program line starts here 
#-------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

#-------------------------------------------------------------------------------------------------------------------------------------------
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4444, debug=True)