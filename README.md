# sqlalchemy-challenge

## Part 1 - Using python/sqlchemy (climate_starter.ipynb)

## Climate Data##
This code is designed to read in a sqlite file containing two sql tables, one called Station, and another called Measurement.  

The Measurement table contains precipitation (prcp) and temperatature (tobs: temperature observation) data taken from differnet weather stations across Hawaii with the following column headers:
- id
- station
- date
- prcp 
- tobs 

The Station table contains information on the weather stations themselves, with the following column headers:
- id
- station
- name
- latitude
- longitude
- elevation

## Queries ## 
Using automap(base) the files are stored and accessed within the jupyter notebook code to create the following queries:

### Precipitation ###

- What's the most recent date in the data set?

- Pull the previous 12 months of precipitations data. Plotted as a bar graph. 

- Print a summary statistics table of the precipitation data.

### Station Analysis ###

- Calculate the total number of stations in the dataset

- Find the most active station

- List the stations and observation counts in descending order.

- Find the station id with the greatest number of observations

- Calculate the lowest, highest, and average temperatures on the most-active station

- Gather the previous 12 months of TOBS data from the most-active station and plot as a histogram. 

## Part 2 - Using Flask API (app.py)

This code is designed to create a local API that has the following routes:
(/) Home page: 
    Shows all available routes
 
(/api/v1.0/precipitation) Precipitation
     Returns a JSON representation of the last 12 months of precipitation data
     
(/api/v1.0/stations) Station List
    Returns a JSON list of stations
    
(/api/v1.0/tobs)
    Returns a list of temperature observations from the previous year
    
(/api/v1.0/<start>)
    Returns a list of the minimum, average, and maximum temperatures for the range between the given start date and the final date
    
(/api/v1.0/<start>/<end>)
    Returns a list of the minimum, average, and maximum temperatures for the range between the given start date and the end date
    
*Code written by Alana Castellano
*Assistance given by AskBCS Tutors for Dynamic routes API call