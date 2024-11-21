pins.onPulsed(DigitalPin.P2, PulseValue.High, function () {
    DurationPulseServo1 = pins.pulseIn(DigitalPin.P2, PulseValue.High)
})
pins.onPulsed(DigitalPin.P1, PulseValue.High, function () {
    DurationPulseServo2 = pins.pulseIn(DigitalPin.P1, PulseValue.High)
})
let DurationPulseServo2 = 0
let DurationPulseServo1 = 0
let LedPos = 0
led.enable(false)
let strip = neopixel.create(DigitalPin.P16, 220, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
let range2 = strip.range(0, 1)
range2.showColor(neopixel.colors(NeoPixelColors.Red))
LedPos += 1
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P15, PinPullMode.PullUp)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P15) == 0 && LedPos == 1) {
        for (let index = 0; index < 55; index++) {
            pins.digitalWritePin(DigitalPin.P15, 1)
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            range2 = strip.range(LedPos, 1)
            range2.showColor(neopixel.colors(NeoPixelColors.Red))
            LedPos += 1
            basic.pause(100)
        }
    }
    if (pins.digitalReadPin(DigitalPin.P6) == 1 && (pins.digitalReadPin(DigitalPin.P3) == 0 && pins.digitalReadPin(DigitalPin.P4) == 0) && LedPos == 56) {
        basic.pause(500)
        if (pins.digitalReadPin(DigitalPin.P6) == 1 && (pins.digitalReadPin(DigitalPin.P3) == 0 && pins.digitalReadPin(DigitalPin.P4) == 0) && LedPos == 56) {
            for (let index = 0; index < 36; index++) {
                strip.showColor(neopixel.colors(NeoPixelColors.Black))
                range2 = strip.range(LedPos, 1)
                range2.showColor(neopixel.colors(NeoPixelColors.Red))
                LedPos += 1
                basic.pause(100)
            }
        }
    }
    if (DurationPulseServo1 >= 1400 && DurationPulseServo1 <= 1600 && LedPos == 92) {
        LedPos += 6
        for (let index = 0; index < 25; index++) {
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            range2 = strip.range(LedPos, 1)
            range2.showColor(neopixel.colors(NeoPixelColors.Red))
            LedPos += 1
            basic.pause(100)
        }
    }
    if (pins.digitalReadPin(DigitalPin.P10) == 1 && (pins.digitalReadPin(DigitalPin.P7) == 0 && pins.digitalReadPin(DigitalPin.P9) == 0) && LedPos == 123) {
        basic.pause(500)
        if (pins.digitalReadPin(DigitalPin.P10) == 1 && LedPos == 123) {
            for (let index = 0; index < 39; index++) {
                strip.showColor(neopixel.colors(NeoPixelColors.Black))
                range2 = strip.range(LedPos, 1)
                range2.showColor(neopixel.colors(NeoPixelColors.Red))
                LedPos += 1
                basic.pause(100)
            }
        }
    }
    if (DurationPulseServo2 >= 1400 && DurationPulseServo2 <= 1600 && LedPos == 162) {
        for (let index = 0; index < 58; index++) {
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            range2 = strip.range(LedPos, 1)
            range2.showColor(neopixel.colors(NeoPixelColors.Red))
            LedPos += 1
            basic.pause(100)
        }
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        basic.pause(5000)
        pins.digitalWritePin(DigitalPin.P13, 0)
    }
    if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        pins.digitalWritePin(DigitalPin.P13, 1)
        strip = neopixel.create(DigitalPin.P16, 220, NeoPixelMode.RGB)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        range2 = strip.range(0, 1)
        range2.showColor(neopixel.colors(NeoPixelColors.Red))
        LedPos = 1
    }
})
