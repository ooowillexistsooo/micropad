import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.oled import Oled, OledDisplayMode

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP4,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

i2c = busio.I2C(scl=board.GP5, sda=board.GP6)

keyboard.extensions.append(
    Oled(
        i2c,
        width=128,
        height=32,
        display_mode=OledDisplayMode.KEYBOARD,
    )
)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D],
]

if __name__ == '__main__':
    keyboard.go()