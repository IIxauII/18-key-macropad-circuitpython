import board
import usb_hid
import digitalio
import time
import tasko
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# GLOBAL VARS
# time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
# background light states: disabled, off, on, blinkAll, lightShow, lightFillAndEmpty
backlightEffect = 'disabled'

# btns are left to right -> top to bottom
# if usb output is on the left side
# row 1
btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP2
btn4_pin = board.GP3
btn5_pin = board.GP4
btn6_pin = board.GP5

# row 2
btn7_pin = board.GP6
btn8_pin = board.GP7
btn9_pin = board.GP8
btn10_pin = board.GP9
btn11_pin = board.GP10
btn12_pin = board.GP11

# row 3
btn13_pin = board.GP12
btn14_pin = board.GP13
btn15_pin = board.GP14
btn16_pin = board.GP15
btn17_pin = board.GP28
btn18_pin = board.GP27

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13 = digitalio.DigitalInOut(btn13_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14 = digitalio.DigitalInOut(btn14_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN

btn15 = digitalio.DigitalInOut(btn15_pin)
btn15.direction = digitalio.Direction.INPUT
btn15.pull = digitalio.Pull.DOWN

btn16 = digitalio.DigitalInOut(btn16_pin)
btn16.direction = digitalio.Direction.INPUT
btn16.pull = digitalio.Pull.DOWN

btn17 = digitalio.DigitalInOut(btn17_pin)
btn17.direction = digitalio.Direction.INPUT
btn17.pull = digitalio.Pull.DOWN

btn18 = digitalio.DigitalInOut(btn18_pin)
btn18.direction = digitalio.Direction.INPUT
btn18.pull = digitalio.Pull.DOWN

# LED pinouts

# pinouts to leds connections

# ------
# -1111-
# ------

# ---2--
# ------
# --2---

# --3---
# ------
# ---3--

# ------
# 4----4
# ------

# ----5-
# ------
# -5----

# -6----
# ------
# ----6-

# -----7
# ------
# 7-----

# 8-----
# ------
# -----8

# pico onboard led, not visible
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led1 = digitalio.DigitalInOut(board.GP26)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.GP22)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.GP21)
led3.direction = digitalio.Direction.OUTPUT

led4 = digitalio.DigitalInOut(board.GP20)
led4.direction = digitalio.Direction.OUTPUT

led5 = digitalio.DigitalInOut(board.GP19)
led5.direction = digitalio.Direction.OUTPUT

led6 = digitalio.DigitalInOut(board.GP18)
led6.direction = digitalio.Direction.OUTPUT

led7 = digitalio.DigitalInOut(board.GP17)
led7.direction = digitalio.Direction.OUTPUT

led8 = digitalio.DigitalInOut(board.GP16)
led8.direction = digitalio.Direction.OUTPUT

# led functions

def ledOne(x):
    if x == '1':
        print('led 1')
        led1.value = True
    elif x == '2':
        print('led 2')
        led2.value = True
    elif x == '3':
        print('led 3')
        led3.value = True
    elif x == '4':
        print('led 4')
        led4.value = True
    elif x == '5':
        print('led 5')
        led5.value = True
    elif x == '6':
        print('led 6')
        led6.value = True
    elif x == '7':
        print('led 7')
        led7.value = True
    elif x == '8':
        print('led 8')
        led8.value = True
    else:
        print('turning leds off')
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False


async def ledLightShow(x):
    sleepTime = 0.1
    if x:
        sleepTime = x
    led1.value = True
    led2.value = False
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = False
    led7.value = False
    led8.value = False
    await tasko.sleep(sleepTime)
    led1.value = False
    led2.value = True
    await tasko.sleep(sleepTime)
    led2.value = False
    led3.value = True
    await tasko.sleep(sleepTime)
    led3.value = False
    led4.value = True
    await tasko.sleep(sleepTime)
    led4.value = False
    led5.value = True
    await tasko.sleep(sleepTime)
    led5.value = False
    led6.value = True
    await tasko.sleep(sleepTime)
    led6.value = False
    led7.value = True
    await tasko.sleep(sleepTime)
    led7.value = False
    led8.value = True
    await tasko.sleep(sleepTime)
    led8.value = False


async def ledLightFillAndEmpty(x):
    sleepTime = 0.1
    if x:
        sleepTime = x

    # fill

    led1.value = False
    led2.value = False
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = False
    led7.value = False
    led8.value = True
    await tasko.sleep(sleepTime)
    led7.value = True
    await tasko.sleep(sleepTime)
    led6.value = True
    await tasko.sleep(sleepTime)
    led5.value = True
    await tasko.sleep(sleepTime)
    led4.value = True
    await tasko.sleep(sleepTime)
    led3.value = True
    await tasko.sleep(sleepTime)
    led2.value = True
    await tasko.sleep(sleepTime)
    led1.value = True
    await tasko.sleep(sleepTime)

    # empty

    await tasko.sleep(sleepTime)
    led1.value = False
    await tasko.sleep(sleepTime)
    led2.value = False
    await tasko.sleep(sleepTime)
    led3.value = False
    await tasko.sleep(sleepTime)
    led4.value = False
    await tasko.sleep(sleepTime)
    led5.value = False
    await tasko.sleep(sleepTime)
    led6.value = False
    await tasko.sleep(sleepTime)
    led7.value = False
    await tasko.sleep(sleepTime)
    led8.value = False
    await tasko.sleep(sleepTime)


def ledAllOn():
    led1.value = True
    led2.value = True
    led3.value = True
    led4.value = True
    led5.value = True
    led6.value = True
    led7.value = True
    led8.value = True


def ledAllOff():
    led1.value = False
    led2.value = False
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = False
    led7.value = False
    led8.value = False


def ledLeftRight():
    led1.value = False
    led2.value = False
    led3.value = False
    led4.value = True
    led5.value = False
    led6.value = False
    led7.value = True
    led8.value = True

def ledBlinkError():
    for x in range(4):
        ledAllOff()
        time.sleep(0.1)
        ledAllOn()
        time.sleep(0.1)


async def ledBlinkAll():
    ledAllOff()
    await tasko.sleep(0.25)
    ledAllOn()
    await tasko.sleep(0.25)


async def ledBlinkOne():
    led1.value = True
    led2.value = False
    led3.value = False
    led4.value = False
    led5.value = False
    led6.value = False
    led7.value = False
    led8.value = False
    await tasko.sleep(0.25)
    led1.value = False
    await tasko.sleep(0.25)


async def ledBacklightHandler():
    global backlightEffect
    if backlightEffect == 'disabled':
        # lets just do nothing
        pass
    elif backlightEffect == 'off':
        # turn off all lighting
        ledAllOff()
    elif backlightEffect == 'on':
        ledAllOn()
    elif backlightEffect == 'blinkAll':
        await ledBlinkAll()
    elif backlightEffect == 'lightShow':
        await ledLightShow(0.25)
    elif backlightEffect == 'lightFillAndEmpty':
        await ledLightFillAndEmpty(0.25)
    else:
        # relax
        await tasko.sleep(0.1)
        print(backlightEffect)
        pass

# This function checks if a multi keypress is registered
# It returns a boolean, which helps to decide if single keypress actions are necessary to be executed or can be skipped
# It immediatly executes the multipress action


async def multiButtonActions():
    global backlightEffect
    if btn13.value and btn1.value:
        print('btn13 and btn1')
        backlightEffect = 'disabled'
        return True
    if btn13.value and btn2.value:
        print('btn13 and btn2')
        backlightEffect = 'off'
        return True
    if btn13.value and btn3.value:
        print('btn13 and btn3')
        backlightEffect = 'on'
        return True
    if btn13.value and btn4.value:
        print('btn13 and btn4')
        backlightEffect = 'blinkAll'
        return True
    if btn13.value and btn5.value:
        print('btn13 and btn5')
        backlightEffect = 'lightShow'
        return True
    if btn13.value and btn6.value:
        print('btn13 and btn6')
        backlightEffect = 'lightFillAndEmpty'
        return True
    else:
        return False


async def singleButtonActions():
    if btn1.value:
        print("btn1")
        ledOne('1')
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.ENTER)
    if btn2.value:
        print("btn2")
        ledOne('2')
    if btn3.value:
        print("btn3")
        ledOne('3')
    if btn4.value:
        print("btn4")
        ledOne('4')
    if btn5.value:
        print("btn5")
        ledOne('5')
    if btn6.value:
        print("btn6")
        ledOne('6')
    if btn7.value:
        print("btn7")
        ledOne('7')
    if btn8.value:
        print("btn8")
        ledOne('8')
    if btn9.value:
        print("btn9")
        ledOne('off')
    if btn10.value:
        print("btn10")
    if btn11.value:
        print("btn11")
    if btn12.value:
        print("btn12")
    if btn13.value:
        print("btn13 - i am function key")
    if btn14.value:
        print("btn14")
    if btn15.value:
        print("btn15")
        ledLeftRight()
    if btn16.value:
        print("btn16")
        ledAllOn()
    if btn17.value:
        print("btn17")
        ledAllOff()
    if btn18.value:
        print("btn18")
        ledLightShow(0)

    # returning if a single btn is being pressed or not
    if btn1.value or btn2.value or btn3.value or btn4.value or btn5.value or btn6.value or btn7.value or btn8.value or btn9.value or btn10.value or btn11.value or btn12.value or btn13.value or btn14.value or btn15.value or btn16.value or btn17.value or btn18.value:
        return True
    else:
        return False

# BOOT ACTIONS
# welcome effect on boot:
def corePostBoot():
    # the light show is async, therefor commented out until sync boot up animation is ready
    # ledLightShow(0.2)
    # ledAllOn()
    # time.sleep(1)
    # ledAllOff()
    # ledBlinkError()
    for x in range(3):
        ledAllOn()
        time.sleep(0.05)
        ledAllOff()
        time.sleep(0.05)
    for x in range(3):
        ledAllOn()
        time.sleep(0.1)
        ledAllOff()
        time.sleep(0.1)
    for x in range(2):
        ledAllOn()
        time.sleep(0.15)
        ledAllOff()
        time.sleep(0.15)
    for x in range(1):
        ledAllOn()
        time.sleep(0.2)
        ledAllOff()
        time.sleep(0.2)
    ledAllOn()
   


""" # core keyboard lifetime loop
while True:
   if multiButtonActions():
      # hell yeah we doing multi button actions right now, siiiick?!?!
      # print('is multi button action!')
      await tasko.sleep(0.1)
   elif singleButtonActions():
      await tasko.sleep(0.1)
   else:
      # core background effect loop
      ledBacklightHandler() """


async def coreKeyboard():
    if await multiButtonActions():
        # hell yeah we doing multi button actions right now, siiiick?!?!
        # print('is multi button action!')
        await tasko.sleep(0.1)
    elif await singleButtonActions():
        await tasko.sleep(0.1)

# testing how often tasko schedule is being run (hz in ms basically)
testStartTime = time.monotonic()
async def testHzTimePassedBetween():
    global testStartTime
    elapsedTime = time.monotonic() - testStartTime
    print("do_something took %f seconds" % elapsedTime)
    testStartTime = time.monotonic()

# ---------- Tasko wiring begins here ---------- #
# Schedule the workflows at whatever frequency makes sense
tasko.schedule(hz=100,  coroutine_function=coreKeyboard)
tasko.schedule(hz=10,  coroutine_function=ledBacklightHandler)
# tasko.schedule(hz=1, coroutine_function=testHzTimePassedBetween)

# display boot animation
corePostBoot()

test = Keycode
# Type 'abc' followed by Enter (a newline).
layout.write('abc\n')

# run tasko tasks while true
tasko.run()
