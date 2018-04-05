#!/usr/bin/env python
#
# https://github.com/loadrun/knight-starter
#
# Released under the MIT license
# (http://choosealicense.com/licenses/mit/).
#
# For more information see
# https://github.com/loadrun/knight-starter/blob/master/LICENSE
#
# This code that was put together as part of a lesson plan for
# The Mind Project Knight Rover Initiative. It is a simple program to
# demo movement of a Dexter Industries GoPiGo robot we are going to use as
# our Knight Rover starter.

import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()

print("***** START *****")
print("Forward.")
gpg.forward()
time.sleep(1)

print("Stop")
gpg.stop()
time.sleep(1)

print("Back")
gpg.backward()
time.sleep(1)

print("Left")
gpg.left()
time.sleep(1)

print("Right")
gpg.right()
time.sleep(1)

print("Left")
gpg.left()
time.sleep(1)

print("Right")
gpg.right()
time.sleep(1)

print("Stop!")
gpg.stop()
print("***** STOP *****")
