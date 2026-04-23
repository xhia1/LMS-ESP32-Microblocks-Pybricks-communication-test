from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

from micropup import add_command, call, init, MicroPUP


hub = PrimeHub()
init('A')
add_command('numbers', 2, 0)



data = call('numbers')

a = data[0]
b = data[1]

result = a * b
print(a, "x", b, "=", result)

