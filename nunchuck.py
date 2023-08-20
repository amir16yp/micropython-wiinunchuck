from machine import I2C, Pin
import time
import math

# Calibration values
NUNCHUK_ACCEL_X_ZERO = 512
NUNCHUK_ACCEL_Y_ZERO = 512
NUNCHUK_ACCEL_Z_ZERO = 512
NUNCHUK_JOYSTICK_X_ZERO = 127
NUNCHUK_JOYSTICK_Y_ZERO = 128

NUNCHUK_ADDRESS = 0x52

# Initialize I2C
i2c = I2C(1, scl=Pin(15, Pin.IN, Pin.PULL_UP), sda=Pin(14, Pin.IN, Pin.PULL_UP))

def nunchuk_init():
    i2c.writeto(NUNCHUK_ADDRESS, bytearray([0x40, 0x00]))
    time.sleep_ms(10)

def nunchuk_read():
    i2c.writeto(NUNCHUK_ADDRESS, bytearray([0x00]))
    time.sleep_ms(10)
    nunchuk_data = i2c.readfrom(NUNCHUK_ADDRESS, 6)
    return nunchuk_data

def nunchuk_decode_byte(x):
    return x

def nunchuk_buttonZ(data):
    return not bool((data[5] >> 0) & 1)

def nunchuk_buttonC(data):
    return not bool((data[5] >> 1) & 1)

def nunchuk_joystickX_raw(data):
    return data[0]

def nunchuk_joystickY_raw(data):
    return data[1]

def nunchuk_joystickX(data):
    return nunchuk_joystickX_raw(data) - NUNCHUK_JOYSTICK_X_ZERO

def nunchuk_joystickY(data):
    return nunchuk_joystickY_raw(data) - NUNCHUK_JOYSTICK_Y_ZERO

def nunchuk_joystick_angle(data):
    return math.atan2(nunchuk_joystickY(data), nunchuk_joystickX(data))

def nunchuk_accelX_raw(data):
    return (data[2] << 2) | ((data[5] >> 2) & 3)

def nunchuk_accelY_raw(data):
    return (data[3] << 2) | ((data[5] >> 4) & 3)

def nunchuk_accelZ_raw(data):
    return (data[4] << 2) | ((data[5] >> 6) & 3)

def nunchuk_accelX(data):
    return nunchuk_accelX_raw(data) - NUNCHUK_ACCEL_X_ZERO

def nunchuk_accelY(data):
    return nunchuk_accelY_raw(data) - NUNCHUK_ACCEL_Y_ZERO

def nunchuk_accelZ(data):
    return nunchuk_accelZ_raw(data) - NUNCHUK_ACCEL_Z_ZERO

def nunchuk_pitch(data):
    return math.atan2(nunchuk_accelY(data), nunchuk_accelZ(data))

def nunchuk_roll(data):
    return math.atan2(nunchuk_accelX(data), nunchuk_accelZ(data))

# Initialize Nunchuk
nunchuk_init()

while True:
    nunchuk_data = nunchuk_read()

    if nunchuk_buttonZ(nunchuk_data):
        print("Button Z is pressed")
    if nunchuk_buttonC(nunchuk_data):
        print("Button C is pressed")

    print("Joystick X:", nunchuk_joystickX(nunchuk_data))
    print("Joystick Y:", nunchuk_joystickY(nunchuk_data))
    print("Accelerometer X:", nunchuk_accelX(nunchuk_data))
    print("Accelerometer Y:", nunchuk_accelY(nunchuk_data))
    print("Accelerometer Z:", nunchuk_accelZ(nunchuk_data))
    print("Pitch:", nunchuk_pitch(nunchuk_data))
    print("Roll:", nunchuk_roll(nunchuk_data))
    print("Joystick Angle:", nunchuk_joystick_angle(nunchuk_data))
    
    time.sleep(0.5)

