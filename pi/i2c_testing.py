import smbus
import time
bus = smbus.SMBus(1)

address = 0x04

def writenum(value):
    bus.write_byte(address,value)
    return -1

def readnum():
    number=bus.read_byte(address)
    return number

while True:
    var = input("number")
    if not var:
        continue

    writenum(var)
    print(var)


