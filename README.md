# raspi-cputemp

This project creates a python script which reads and record the raspberry pi's CPU temperature on a CSV file.
Also allows to plot the CPU graphic on a GUI interface if you got one. I'm just using CLI so I won't use it here.

## Usage

Run `crontab -e` on terminal and at the end of the file paste 
`@reboot python3 /home/pi/raspi-cputemp/temp_monitor.py &` and reboot the rapsberry pi.
This allows crontab to run the script on every reboot, and record the temperatures.
You can run without crontab too.

## What's new

ver 1.0 - Script only saving temperatures in the CSV file.

ver 2.0 - Removed the matplotlib comments and added the terminal print while saving the values
at the CSV file.


## References

- [Raspberry Pi temperature log][rt]

* * *

> "Thanks for passing by."

  [rt]: https://projects.raspberrypi.org/en/projects/temperature-log/