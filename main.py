from machine import Pin, PWM
import time
import machine

SERVOX_CENTER = 3050
SERVOY_CENTER = 3500

level_shifter = Pin(14, Pin.OUT)
level_shifter.value(1)

servoy = machine.PWM(machine.Pin(12))
servoy.freq(50)
servox = machine.PWM(machine.Pin(11))
servox.freq(50)

servoy_degree_interval = 50
servox_degree_interval = 50

while True:
  servox.duty_u16(SERVOX_CENTER)
  servoy.duty_u16(SERVOY_CENTER)
  # time.sleep(1)
  # servox.duty_u16(SERVOX_CENTER + servox_degree_interval * 1)
  # servoy.duty_u16(SERVOY_CENTER + servoy_degree_interval * 1)
  # time.sleep(1)
  # servox.duty_u16(SERVOX_CENTER - servox_degree_interval * 1)
  # servoy.duty_u16(SERVOY_CENTER - servoy_degree_interval * 1)
  # time.sleep(1)