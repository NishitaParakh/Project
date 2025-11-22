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

#----------------------------------------------
# MODULE 4 - ACTION REQUIRED
#----------------------------------------------
def taking_action(analysis):
    status = analysis["Status"]
    if status == "Good. Safe to Breathe :)":
        return "Air Quality is safe. No action needed :)"
    elif status == "Moderate":
        return "Open Windows or turn on Ventilation."
    elif status == "Unhealthy for sensitive people!":
        return "Turn on Purifier and avoid doing heavy physical work."
    else:
        print("\nWARNING: AIR QUALITY IS VERY BAD!")
        print("AQI is too HIGH! Health Risk Detected!")
        need = input("Do you want to turn ON the Air Purifier(YES/NO): ")

        if need.lower() == "yes":
            print("\nGOOD DECISION:)",sep='\n')
            print("\nPREVENTION IS BETTER THAN CURE!","          ~Desiderius Erasmus",sep='\n')
            return "Air Purifier turned ON for safety."
        else:
            return "Purifier not turned ON. Wear Masks for safety purposes"