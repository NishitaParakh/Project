#----------------------------------------------
# MODULE 5 - REPORT MODULE
#----------------------------------------------  
import datetime   
def display_report(activity,sensor_data,analysis,action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n==================================================")
    print("                TIME OF REPORT")
    print("====================================================")
    print("             ", timestamp)
    print("==================================================\n")

    print("\n=================POLLUTION REPORT=================")
    print("Environment Monitored :", activity)
    print("----------------------------------------------------")

    print("Sensor Readings: ")
    for key,value in sensor_data.items():
        print("   ",key,":",value)

    print("\nAir Quality Analysis:")
    for key,value in analysis.items():
        print("   ",key,":",value)
    
    print("\nRecommended Action: ")
    print("  ",action)
    print("==================================================\n")