import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()

mouse_keys = MouseKeys()
keyboard.modules.append(mouse_keys)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.A0, board.A1, board.A2) 
keyboard.row_pins = (board.A3, board.D6, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = (
    (board.D7, board.D0, None, False), 
    (board.D1, board.D2, None, False), 
)

def roblox_pan(move_key):
    return simple_key_sequence([
        KC.MB_RMB.as_press(),
        move_key,
        KC.MB_RMB.as_release(),
    ])

keyboard.keymap = [
    [
        KC.LALT(KC.F4), KC.W, KC.E,
        KC.A, KC.S, KC.D,
        KC.LSHIFT, KC.ENTER, KC.SPACE,
    ]
]

encoder_handler.map = [
    (
        (roblox_pan(KC.MS_UP), roblox_pan(KC.MS_DOWN)), 
    ),
    (
        (roblox_pan(KC.MS_LEFT), roblox_pan(KC.MS_RIGHT)),
    ),
]

if __name__ == '__main__':
    keyboard.go()