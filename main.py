def on_pulsed_p2_high():
    global DurationPulseServo1
    DurationPulseServo1 = pins.pulse_in(DigitalPin.P2, PulseValue.HIGH)
pins.on_pulsed(DigitalPin.P2, PulseValue.HIGH, on_pulsed_p2_high)

def on_pulsed_p1_high():
    global DurationPulseServo2
    DurationPulseServo2 = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH)
pins.on_pulsed(DigitalPin.P1, PulseValue.HIGH, on_pulsed_p1_high)

DurationPulseServo2 = 0
DurationPulseServo1 = 0
LedPos = 0
led.enable(False)
strip = neopixel.create(DigitalPin.P16, 220, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
range2 = strip.range(0, 1)
range2.show_color(neopixel.colors(NeoPixelColors.RED))
LedPos += 1
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_UP)

def on_forever():
    global range2, LedPos, strip
    if pins.digital_read_pin(DigitalPin.P15) == 0 and LedPos == 1:
        for index in range(55):
            pins.digital_write_pin(DigitalPin.P15, 1)
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            range2 = strip.range(LedPos, 1)
            range2.show_color(neopixel.colors(NeoPixelColors.RED))
            LedPos += 1
            basic.pause(100)
    if pins.digital_read_pin(DigitalPin.P6) == 1 and (pins.digital_read_pin(DigitalPin.P3) == 0 and pins.digital_read_pin(DigitalPin.P4) == 0) and LedPos == 56:
        basic.pause(200)
        if pins.digital_read_pin(DigitalPin.P6) == 1 and (pins.digital_read_pin(DigitalPin.P3) == 0 and pins.digital_read_pin(DigitalPin.P4) == 0) and LedPos == 56:
            for index2 in range(36):
                strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
                range2 = strip.range(LedPos, 1)
                range2.show_color(neopixel.colors(NeoPixelColors.RED))
                LedPos += 1
                basic.pause(100)
    if DurationPulseServo1 >= 1400 and DurationPulseServo1 <= 1600 and LedPos == 92:
        LedPos += 6
        for index3 in range(25):
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            range2 = strip.range(LedPos, 1)
            range2.show_color(neopixel.colors(NeoPixelColors.RED))
            LedPos += 1
            basic.pause(100)
    if pins.digital_read_pin(DigitalPin.P10) == 1 and (pins.digital_read_pin(DigitalPin.P7) == 0 and pins.digital_read_pin(DigitalPin.P9) == 0) and LedPos == 123:
        basic.pause(200)
        if pins.digital_read_pin(DigitalPin.P10) == 1 and LedPos == 123:
            for index4 in range(39):
                strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
                range2 = strip.range(LedPos, 1)
                range2.show_color(neopixel.colors(NeoPixelColors.RED))
                LedPos += 1
                basic.pause(100)
    if DurationPulseServo2 >= 1400 and DurationPulseServo2 <= 1600 and LedPos == 162:
        for index5 in range(58):
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            range2 = strip.range(LedPos, 1)
            range2.show_color(neopixel.colors(NeoPixelColors.RED))
            LedPos += 1
            basic.pause(100)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(5000)
        pins.digital_write_pin(DigitalPin.P13, 0)
    if pins.digital_read_pin(DigitalPin.P13) == 0:
        pins.digital_write_pin(DigitalPin.P13, 1)
        strip = neopixel.create(DigitalPin.P16, 220, NeoPixelMode.RGB)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        range2 = strip.range(0, 1)
        range2.show_color(neopixel.colors(NeoPixelColors.RED))
        LedPos = 1
basic.forever(on_forever)
