import machine
import time


def toggle(p):
    p.value(not p.value())


def start():
    print("Program started, let's blink this thing!")
    pin = machine.Pin(2, machine.Pin.OUT)

    while True:
        toggle(pin)
        time.sleep_ms(200)
 