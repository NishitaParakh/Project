#----------------------------------------------
# MODULE 3 - ANALYZER MODULE
#----------------------------------------------
def analyze(data):
    pm25 = data["PM2.5"]
    aqi = data["AQI"]
    co2 = data["CO2"]

    if aqi <= 50:
        status = "Good. Safe to Breathe :)"
    elif aqi >= 51 and aqi <= 100:
        status = "Moderate"
    elif aqi >= 101 and aqi <= 150:
        status = "Unhealthy for sensitive people!"
    elif aqi >= 151 and aqi <= 250:
        status = "Very Unhealthy!!"
    else:
        status = "HAZARDOUS!!!"
    
    result = {
        "Status" : status,
        "PM2.5" : pm25,
        "AQI" : aqi,
        "CO2" : co2
    }
    return result