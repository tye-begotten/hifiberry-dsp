import argparse
import RPi.GPIO as gpio

cmd_description = \
"enables or disables the selfboot mode of the DSP board. \
In selfboot mode, the DSP will start from the program stored in EEPROM. \
If selfboot is disabled, the dsp will start with no program loaded and must be manually configured. \
The default startup behavior is to enable selfboot, so if a bad program gets stored in EEPROM, \
the DSP will never start properly. This is one scenario where disabling selfboot to reprogram can be handy. \
"

SELFBOOT_PIN = 15

parser = argparse.ArgumentParser(description='HiFiBerry DSP toolkit',
                                         formatter_class = argparse.RawTextHelpFormatter,
                                         epilog = cmd_description)

parser.add_argument('command',
                    choices=['enable', 'disable'])
parser.add_argument('parameters', nargs='*',
                    help="see command description below")

args = parser.parse_args()

selfboot_enabled = args.command == 'enable'

gpio.setmode(gpio.BOARD)
print(f"gpio_function(SELFBOOT_PIN) = {gpio.gpio_function(SELFBOOT_PIN)}")
gpio.setup(SELFBOOT_PIN, gpio.OUT)
print(f"gpio set to output")

prev = None
print(f"{'enabling' if selfboot_enabled else 'disabling'} selfboot")
print(f"setting pin to {'HIGH' if selfboot_enabled else 'LOW'}")
while True:
    gpio.output(SELFBOOT_PIN, gpio.HIGH if selfboot_enabled else gpio.LOW)
    val = gpio.input(15)
    if val:
        print("pin is HIGH!")
    elif prev == None or prev != val:
        print("pin is LOW!")
    
gpio.cleanup()