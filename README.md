# Real Ant BT

<a href="https://www.youtube.com/watch?v=fSu-80Ofek4"><img src="images/realant.jpg"></a>


Resources for working with the Real Ant project minus the actual reinforcement
learning. This repository consists of code that allows you to interact with any
number of [Dynamixel AX-12A](https://www.robotis.us/dynamixel-ax-12a/) servos.

## Code Description

### `Ax12` Class

This module allows you to connect to the AX-12A servos then read and write to
the various registers that contain information about the servos' current & goal
position, LED light, moving speed, and much more.

The original class can be [found here](https://github.com/aakieu/ax12_control),
and worked for this usecase with little modification.

### `movement.py`

This module consists of functions for moving the collection of servos on the
ant. These utility functions can be used to move a single servo or a collection
of servos to perform an action like sitting or standing.

**IMPORTANT:** The servo ids should be configured to be numbers between 1-8 and
arranged in a specific order for the various movements to work out of the box.
Look at the image below: ![Ant ID Configuration](/images/id_config.jpg)

### `changeID.py`

This is a short script that allows you to connect a single servo and configure
the ID associated with it.

### `moveAnt.py`

This script simply connects to the ant and sends some tester function calls to
get it to perform the various tasks we have defined.

### `singleServo.py`

Short script to display a TKinter window to control a single AX-12A's speed and
position.

### `app.py` + `templates/index.html`

This is a simple Flask server that serves a webpage on your local network that
allows you to interact with the ant.

**WARNING:** Wait for the ant to stop moving before sending another command.
Otherwise, it will not perform the action as intended and risks the legs
getting tangled.

## Resources

- [Dynamixel
  Wizard](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/):
provides visual interface to configure & manage the Dynamixel servos.

- [Dynamixel SDK
  Docs](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/):
the software development kit to interact with the servos using the language of
your choice (in this case _Python_).

- [Dynamixel AX-12A
  E-Manual](https://emanual.robotis.com/docs/en/dxl/ax/ax-12a/): documentation
about the physical servos, including information about the different values and
their registers.
