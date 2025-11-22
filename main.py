#==============================================
#      MINI POLLUTION MONITORING SYSTEM
#==============================================


#----------------------------------------------
#                MAIN PROGRAM
#----------------------------------------------  
from M1sensor import get_readings, choose
from M2analyzer import analyze, taking_action
from M3report import display_report

def main():
    print("\n--------------------------------------------------\n")
    print("         MINI POLLUTION MONITORING SYSTEM\n")
    print("----------------------------------------------------\n")
    print("Colecting and analyzing Air Quality...\n")

    activity = choose()
    sensor_data = get_readings(activity)
    analysis = analyze(sensor_data)
    action = taking_action(analysis)
    display_report(activity,sensor_data,analysis,action)

    again = input("\nDo you want to run again?(YES/NO): ")
    if again.lower() == "yes":
        main()

main()




