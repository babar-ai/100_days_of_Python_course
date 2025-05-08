from datetime import datetime

hour = int(datetime.now().strftime("%H"))

if(hour>0 and hour<12):
    print(f"Good Morning! its {datetime.now().strftime("%I:%M:%S %p")}")

elif hour>=12 and hour<16: 
    print(f"Good Afternon! its {datetime.now().strftime("%I:%M:%S %p")}")

else:
    print(f"Good Evening! its {datetime.now().strftime("%I:%M:%S %p")}")






# timesstamps = datetime.now().strftime("%I:%M:%S %p")              # %I for 12-hour, %p for AM/PM
# print(timesstamps)

