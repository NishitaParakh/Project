#----------------------------------------------
# MODULE 1 - SENSOR MODULE
#----------------------------------------------


location_ranges = {
    "Traffic" : {"PM2.5" : (40,200), "AQI": (80,300),"CO2":(50,200)},
    "Indoors" : {"PM2.5" : (10,80), "AQI": (20,120),"CO2":(30,120)},
    "Factory" : {"PM2.5" : (60,250), "AQI": (60,350),"CO2":(100,400)},
    "Park" : {"PM2.5" : (5,40), "AQI": (10,80),"CO2":(20,80)},
    "Kitchen" : {"PM2.5" : (20,100), "AQI": (30,150),"CO2":(50,250)}

    }
def get_readings(location):
    print(f"\nEnter pollution readings for {location}:") 

    if location not in location_ranges:
        pm25 = int(input("Enter PM2.5 value: "))
        aqi = int(input("Enter AQI value: "))
        co2 = int(input("Enter CO2 value: ")) 
        return {"PM2.5": pm25, "AQI": aqi, "CO2": co2}
    else:
        ranges = location_ranges[location]
    
    low, high = ranges["PM2.5"]
    print(f"\n PM2.5 Range for {location}: {low} - {high}")
    while True:
        pm25 = int(input("Enter PM2.5 value: "))
        if low <= pm25 <= high:
            break
        print(f"Invalid!")

    low, high = ranges["AQI"]
    print(f"\n AQI Range for {location}: {low} - {high}")
    while True:
        aqi = int(input("Enter AQI value: "))
        if low <= aqi <= high:
            break
        print(f"Invalid!")
    
    low, high = ranges["CO2"]
    print(f"\n CO2 Range for {location}: {low} - {high}")
    while True:
        co2 = int(input("Enter CO2 value: "))
        if low <= co2 <= high:
            break
        print(f"Invalid!")
    return{"PM2.5":pm25, "AQI":aqi,"CO2":co2}

#----------------------------------------------
# MODULE 2 - SELECT ACTIVITY
#----------------------------------------------
def choose():
    print("\nChoose Location:")
    print("1. Traffic Area","2. Indoors", "3. Factory", "4. Park", "5. Kitchen", "6. Other(Custom)", sep='\n')
    
    choice = input("Enter Location (1-6): ")

    locations = {
        "1" : "Traffic",
        "2" : "Indoors",
        "3" : "Factory",
        "4" : "Park",
        "5" : "Kitchen",
        "6" : "Custom"
    }

    selected = locations.get(choice, "Custom")
    if selected == "Custom":
        selected = input("Enter your custom location: ")
    return selected