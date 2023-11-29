# Import the dependencies.
import flask
import sqlalchemy
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_
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
station_class = Base.classes.station

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
#Precipitation Route
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

#Stations Route
@app.route("/api/v1.0/stations")
def stat():
    session=Session(engine)
  
    stat_results = session.query(station_class.station, station_class.name).all()
    session.close()
   
    stat_list = []
    for station, name in stat_results:
        stat_dict = {}
        stat_dict["station"]=station
        stat_dict["name"]=name
        stat_list.append(stat_dict)

    return jsonify(stat_list)

#Tobs Route
@app.route("/api/v1.0/tobs")
def tobs():    
    session=Session(engine)
   
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days = 365)
   
    tobs_results = session.query(measurement.station, measurement.date, measurement.tobs).\
        filter(measurement.date >= prev_year, measurement.station == "USC00519281").all()
    session.close()

    tobs_list = []
    for station, date, tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["station"]=station
        tobs_dict["date"]=date
        tobs_dict["tobs"]=tobs
        tobs_list.append(tobs_dict)

    return jsonify(tobs_list)

@app.route("/api/v1.0/temp/<start>")
def stats(start=None):
    start = dt.datetime.strptime(start, "%m%d%Y") 
    start_results = session.query(func.avg(measurement.tobs), func.max(measurement.tobs), func.min(measurement.tobs)).\
        filter(measurement.date >= start).all()

    session.close()
    return jsonify(Temperatures = list(np.ravel(start_results)))
   
@app.route("/api/v1.0/temp/<start>/<end_date>")
def start_end(start=None, end_date=None):
    start = dt.datetime.strptime(start, "%m%d%Y")
    end_date = dt.datetime.strptime(end_date, "%m%d%Y")
    start_end_results = session.query(func.avg(measurement.tobs), func.max(measurement.tobs), func.min(measurement.tobs)).\
        filter(and_(measurement.date >= start , measurement.date <= end_date)).all()

    session.close()
    return jsonify(Temperatures = list(np.ravel(start_end_results)))

if __name__ == "__main__":
    app.run(debug=True)