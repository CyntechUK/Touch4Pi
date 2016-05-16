# Touch4Pi

Add extra interactivity with your games by adding 4 capacitive touch pads, each lined up with its own RGB LED allowing tactile feedback on presses.

Create a safe combination to unlock your Raspberry Pi, test your memory by creating a Simon style game or play against a computer opponent in a game of Mastermind.

With individual RGB LEDs shining in to the side of frosted acrylic, this allows the ability to create some nice lighting effects.


## Installation

SMBus is required to talk over i2c to the Touch4Pi HAT; Firstly enable i2c and SPI in raspi-config.

    sudo raspi-config

Go down to Advanced Options, SPI, Yes to enable, and Yes for auto start. Back down to Advanced Options and i2c, Yes to enable and Yes for auto start. Finish and reboot.

    sudo apt-get install python-smbus

    git clone https://github.com/CyntechUK/Touch4Pi.git
    cd Touch4Pi
    sudo python test-disco.py

The lights will start flickering randomly. Control + C to exit.

Also available is test-simon.py for a simple Simon game, and test-touch.py for testing the capacitive touch pads. 


A friendlier Python library is current under construction and will be released soon!