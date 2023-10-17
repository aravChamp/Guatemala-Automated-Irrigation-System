import alarm
import time
import board
import analogio
import digitalio

analog_pin = analogio.AnalogIn(board.A0)

valve = digitalio.DigitalInOut(board.D8)
valve.direction = digitalio.Direction.OUTPUT

smPwr = digitalio.DigitalInOut(board.D3)
smPwr.direction = digitalio.Direction.OUTPUT

	
smPwr.value = True
time.sleep(0.05)
n = analog_pin.value
time.sleep(0.05)
smPwr.value = False
    
if n < 35000:
	valve.value = True
	time.sleep(20)
	valve.value = False
	
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 10)

alarm.exit_and_deep_sleep_until_alarms(time_alarm)
