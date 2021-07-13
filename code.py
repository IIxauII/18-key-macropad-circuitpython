"""Example for Pico. Turns on the built-in LED."""
import board
import digitalio
import time

# from adafruit_hid.keycode import Keycode
# from adafruit_hid.keyboard import Keyboard

print("HELLO WORLD!")

# btns are left to right
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

# keyboard = Keyboard(usb_hid.devices)

# led functions

def ledOne(x):
   print(x);
   if x == '1':
      print('led 1')
      led1.value = True
      led2.value = False
      led3.value = False
      led4.value = False
      led5.value = False
      led6.value = False
      led7.value = False
      led8.value = False
   elif x == '2':
      print('led 2')
      led1.value = False
      led2.value = True
      led3.value = False
      led4.value = False
      led5.value = False
      led6.value = False
      led7.value = False
      led8.value = False
   elif x == '3':
      print('led 3')
      led1.value = False
      led2.value = False
      led3.value = True
      led4.value = False
      led5.value = False
      led6.value = False
      led7.value = False
      led8.value = False
   elif x == '4':
      print('led 4')
      led1.value = False
      led2.value = False
      led3.value = False
      led4.value = True
      led5.value = False
      led6.value = False
      led7.value = False
      led8.value = False
   elif x == '5':
      print('led 5')
      led1.value = False
      led2.value = False
      led3.value = False
      led4.value = False
      led5.value = True
      led6.value = False
      led7.value = False
      led8.value = False
   elif x == '6':
      print('led 6')
      led1.value = False
      led2.value = False
      led3.value = False
      led4.value = False
      led5.value = False
      led6.value = True
      led7.value = False
      led8.value = False
   elif x == '7':
      print('led 7')
      led1.value = False
      led2.value = False
      led3.value = False
      led4.value = False
      led5.value = False
      led6.value = False
      led7.value = True
      led8.value = False
   elif x == '8':
      print('led 8')
      led1.value = False
      led2.value = False
      led3.value = False
      led4.value = False
      led5.value = False
      led6.value = False
      led7.value = False
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

def ledLightShow(x):
   sleepTime = 0.1
   if x:
      sleepTime = x
   print('current led sleeptime')
   print(sleepTime)
   led1.value = True
   led2.value = False
   led3.value = False
   led4.value = False
   led5.value = False
   led6.value = False
   led7.value = False
   led8.value = False
   time.sleep(sleepTime)
   led1.value = False
   led2.value = True
   time.sleep(sleepTime)
   led2.value = False
   led3.value = True
   time.sleep(sleepTime)
   led3.value = False
   led4.value = True
   time.sleep(sleepTime)
   led4.value = False
   led5.value = True
   time.sleep(sleepTime)
   led5.value = False
   led6.value = True
   time.sleep(sleepTime)
   led6.value = False
   led7.value = True
   time.sleep(sleepTime)
   led7.value = False
   led8.value = True
   time.sleep(sleepTime)
   led8.value = False

# on boot:
ledLightShow(0.2)

while True:
   if btn1.value:
      print("btn1")
      ledOne('1')
      time.sleep(0.1)
   if btn2.value:
      print("btn2")
      ledOne('2')
      led1.value = False
      time.sleep(0.1)
   if btn3.value:
      print("btn3")
      ledOne('3')
      time.sleep(0.1)
   if btn4.value:
      print("btn4")
      ledOne('4')
      time.sleep(0.1)
   if btn5.value:
      print("btn5")
      ledOne('5')
      time.sleep(0.1)
   if btn6.value:
      print("btn6")
      ledOne('6')
      time.sleep(0.1)
   if btn7.value:
      print("btn7")
      ledOne('7')
      time.sleep(0.1)
   if btn8.value:
      print("btn8")
      ledOne('8')
      time.sleep(0.1)
   if btn9.value:
      print("btn9")
      ledOne('off')
      time.sleep(0.1)
   if btn10.value:
      print("btn10")
      time.sleep(0.1)
   if btn11.value:
      print("btn11")
      time.sleep(0.1)
   if btn12.value:
      print("btn12")
      time.sleep(0.1)
   if btn13.value:
      print("btn13")
      time.sleep(0.1)
   if btn14.value:
      print("btn14")
      time.sleep(0.1)
   if btn15.value:
      print("btn15")
      time.sleep(0.1)
   if btn16.value:
      print("btn16")
      time.sleep(0.1)
   if btn17.value:
      print("btn17")
      time.sleep(0.1)
   if btn18.value:
      print("btn18")
      ledLightShow(0)
      # time.sleep(0.1)
