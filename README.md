# ArduinoTestCode
Anti RTFM

Introduction
This project was born out of frustration while troubleshooting an issue for a friend. While browsing technical forums, the response "Because you don't understand what you are doing" came up. No kidding—that’s exactly why people ask questions in the first place. 
This project aims to simplify the process of setting up and testing an Arduino for sensor reading and then using a Raspberry Pi to save the data to a file for further processing.

About
This repository provides resources for:
Setting up an Arduino to read data from sensors.
Configuring a Raspberry Pi to log the Arduino’s sensor data to a file for analysis or processing.

Installation
No specific installation required for this repository. Ensure you have the following:
Arduino IDE (for programming the Arduino).
Python 3 (for data logging on the Raspberry Pi).
Required hardware:
Arduino board (e.g., Uno, Nano, or similar).
Raspberry Pi (any model with USB support).

Compilation
Arduino sketches should be uploaded to the Arduino board via the Arduino IDE.
Python scripts can be run directly on the Raspberry Pi.

How to Run
Arduino Setup:
Connect the Arduino to your computer.
Write or upload a sketch to read sensor data and send it over the serial connection using Serial.print or Serial.println.
Raspberry Pi Setup:
Connect the Arduino to the Raspberry Pi via USB.
Run the Python script provided in this repository to log the sensor data to a file.

Author
Who7F
