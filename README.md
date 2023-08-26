# micropython-wiinunchuck

Interact with a Wii Nunchuck in MicroPython

## Setup

To use a legitimate (non-clone) Wii Nunchuck with this library, follow these steps:

1. Cut and strip the wire of the Nunchuck.
2. Connect the **Red** wire to the **3v3** (3.3V) output pin.
3. Connect the **White** wire to **GND** (Ground).
4. Connect the **Yellow** wire to the I2C **SCL** pin (default in the script: pin 15).
5. Connect the **Green** wire to the I2C **SDA** pin (default in the script: pin 14).

You can modify the pin values as needed. To get started, you can run the script directly or import it and use the required functions. It's recommended to read through the code for better understanding.
## Usage

To use the `micropython-wiinunchuck` library in your MicroPython project, follow these steps:

1. Connect your Wii Nunchuck to your MicroPython device following the setup instructions in the previous sections.

2. Copy and paste the provided code into your MicroPython project file, or save it as a new file.

3. Make sure you have the necessary dependencies in your project. The code uses the `machine` module for I2C communication and `math` module for some calculations.

4. Run the code on your MicroPython device.

The provided code initializes the Nunchuck, reads its data, and demonstrates various functions to retrieve information such as button states, joystick positions, and accelerometer data. Here's a breakdown of what the code does:

- Initializes the I2C communication and provides calibration values for the Nunchuck's components.
- Defines functions to read different aspects of Nunchuck data, such as button presses, joystick positions, and accelerometer readings.
- Initializes the Nunchuck device using the `nunchuk_init()` function.
- Enters an infinite loop to continuously read Nunchuck data.
- Prints out information about button presses, joystick positions, accelerometer readings, pitch, roll, and joystick angle.
- Includes a short delay using `time.sleep(0.5)` to control the loop frequency.

Feel free to modify the code to suit your project's needs. For instance, you might want to integrate the code into your existing project structure or use the data retrieved from the Nunchuck for specific actions in your application.

Remember to refer to your MicroPython device's documentation on how to execute scripts and interact with I2C devices.

## License

This project is licensed under the [Unlicense](https://github.com/amir16yp/micropython-wiinunchuck/blob/main/LICENSE).

