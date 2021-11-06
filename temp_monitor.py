from gpiozero import CPUTemperature
from time import sleep, strftime

cpu = CPUTemperature()


def write_temp(temp):
    with open("/home/pi/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))


def main():
    while True:
        temp = cpu.temperature
        write_temp(temp)
        print(temp)
        sleep(1)


try:
    main()
except KeyboardInterrupt:
    print('\nThanks!\n')
