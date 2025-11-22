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