# polybarModules


## OpenMeteoBar
0. Uses OpenMeteo to display current wind speed, temperature. Also includes a dynamically changing specialIcon that reflects rain and snow.
1. Polybar config.ini
```
[module/openmeteobar]
type = custom/script
interval = 480
exec = /your/path/to/openmeteobar.py
```
2. Edit the file and fill out your coordinates
