# raspi-cputemp

This project creates a python script which reads and record the raspberry pi's CPU temperature on a CSV file.
Also allows to plot the CPU graphic on a GUI interface.

## Usage

After made a copy of `temp_monitor.py` to `/home/pi` we're going to set up *crontab*.
Run `crontab -e` on terminal and at the end of the file paste 
`@reboot python3 /home/pi/temp_monitor.py` and reboot the rapsberry pi.
Make sure you have matplotlib installed and uncomment `plt.pause` line commenting `sleep`.


## References

- [Raspberry Pi temperature log][rt]

* * *

> "Thanks for passing by."

  [rt]: https://projects.raspberrypi.org/en/projects/temperature-log/