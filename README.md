# polybarModules


## OpenMeteoBar
0. Uses OpenMeteo to display current wind speed, temperature. Also includes a dynamically changing specialIcon that reflects rain and snow.
1. Polybar config.ini
```
[module/openmeteobar]
type = custom/script
interval = 480
exec = /your/path/to/openMeteoBar.py
```
2. Edit the openMeteoBar.py file and fill out your coordinates in the line 16 and 17.
3. Add openmeteobar into your modules config.

## TimeUntilClass
0. Displays the time (in minutes and seconds) until the end of class. Also displays the time until the end of the break.
1. Polybar config.ini
```
[module/timeuntilclass]
type = custom/script
interval = 0.75
exec = /your/path/to/timeuntilclass.py
```
2. Edit the timeUntilClass.py file to reflest the starting and ending of your classes.
3. Add timeuntilclass into your modules config.

## ZTMBusTracker
0. Displays the time (in minutes and seconds) till the arrival of a ZTM bus.
1. Polybar config.ini
```
[module/ztmbustracker]
type = custom/script
interval = 0.75
exec = /your/path/to/ztmbustracker.py
```
2. Edit the ZTMBusTracker.py file to reflect your bus's timetable (take them from [here](https://www.ztm.poznan.pl/pl/rozklad-jazdy)). This might work for trams, but it's untested.
3. Add ztmbustracker into your modules config.
