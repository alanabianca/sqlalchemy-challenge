# Import the dependencies.
import flask
import sqlalchemy
import datetime as dt

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table

measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precip():
    session=Session(engine)
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
    sel = [measurement.date, measurement.prcp]

    results = session.query(*sel).filter(measurement.date >= prev_year).all()

    session.close()

    all_results = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"]=date
        precip_dict["prcp"]=prcp
        all_results.append(precip_dict)

    return jsonify(all_results)

@app.route("/api/v1.0/stations")
def stat():
    session=Session(engine)
  
    stat_results = session.query(station.station, station.name).all()
    session.close()
   
    stat_list = []
    for station, name in stat_results:
        stat_dict = {}
        stat_dict["station"]=station
        stat_dict["name"]=name
        stat_list.append(stat_dict)

    return jsonify(stat_results)


#@app.route("/api/v1.0/tobs")

#@app.route("/api/v1.0/<start>")
#AND
#@app.route("/api/v1.0/<start>/<end>")

if __name__ == "__main__":
    app.run(debug=True)