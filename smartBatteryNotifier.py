import psutil
from plyer import notification
import time
import winsound

minimum = 85;
maximum = 95;

while(True):
    battery = psutil.sensors_battery();
    percent = battery.percent;
    charging = battery.power_plugged;
            
    if ((percent>=maximum) and (charging==True)):
            notification.notify(
            title="BATTERY_FULLY_CHARGED",
            message=str(percent)+"% Battery remaining "+"\n[PLEASE_UNPLUG_THE_CHARGER]",
            timeout=1
            )
            freq = 600;
            dur = 2000;
            winsound.Beep(freq,dur);

    if ((percent<=minimum) and (charging==False)):
        notification.notify(
        title="BATTERY_BELOW_SAFE_LEVEL",
        message=str(percent)+"% Battery remaining "+"\n[PLEASE_PLUG_THE_CHARGER]",
        timeout=1
        )
        freq = 600;
        dur = 2000;
        winsound.Beep(freq,dur);
        
    time.sleep(5);
     
    continue
