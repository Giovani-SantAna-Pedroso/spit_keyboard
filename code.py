import board

from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, KEY_GENERATORS
from kmk.scanners import DiodeOrientation
from kmk.modules.tapdance import TapDance
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.extensions.media_keys import MediaKeys
from storage import getmount

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

##########################################
#  __  __           _       _            #
# |  \/  | ___   __| |_   _| | ___  ___  #
# | |\/| |/ _ \ / _` | | | | |/ _ \/ __| #
# | |  | | (_) | (_| | |_| | |  __/\__ \ #
# |_|  |_|\___/ \__,_|\__,_|_|\___||___/ #
#                                        #
##########################################

# Holdtap config
holdtap = HoldTap()
holdtap.tap_time = 200
keyboard.modules.append(holdtap)

# Layers 
layers = Layers()
keyboard.modules.append(layers)


# Split config
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
device_name = str(getmount('/').label)

# config row
# form the orange keyboard
if "_O_" in device_name:
    keyboard.row_pins = (board.GP16, board.GP17, board.GP18, board.GP19)             # Rows

# col
if side == SplitSide.RIGHT:

    split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT
                  , data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
    keyboard.col_pins = (board.GP15,board.GP14, board.GP13, board.GP12, board.GP11) # Cols

else: 
    split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT
                  , data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
    keyboard.col_pins = (board.GP15,board.GP14, board.GP13, board.GP12, board.GP11) # Col

keyboard.modules.append(split)

# Tap dance 
tapdance = TapDance()
tapdance.tap_time =200
keyboard.modules.append(tapdance)

# Macros 
macros = Macros()
keyboard .modules.append(macros)

# Media Keys 
keyboard.extensions.append(MediaKeys())


##############################################
#                                            #
# | |/ /___ _   _ _ __ ___   __ _ _ __  ___  #
# | ' // _ \ | | | '_ ` _ \ / _` | '_ \/ __| #
# | . \  __/ |_| | | | | | | (_| | |_) \__ \ #
# |_|\_\___|\__, |_| |_| |_|\__,_| .__/|___/ #
#           |___/                |_|         # 
#                                            #
##############################################

____ = KC.TRNS
XXXX = KC.NO
# Fix ABNT 2, these are just some quick fixes for some keys that are not in the correct layout
KC_QUO = KC.GRAVE
KC_ASC = KC.LBRC
KC_LBRC = KC.RBRC
KC_RBRC = KC.BSLS
KC_GRAVE = KC.QUOTE
KC_SLASH =KC.RALT(KC.Q) 
KC_QUESTION =KC.RALT(KC.W) 
KC_SCLN = KC.SLASH





CTR_Z=KC.MACRO(Press(KC.RCTRL), Tap(KC.Z), Release(KC.RCTRL))
CTR_C=KC.MACRO(Press(KC.RCTRL), Tap(KC.C), Release(KC.RCTRL))
CTR_V=KC.MACRO(Press(KC.RCTRL), Tap(KC.V), Release(KC.RCTRL))

TAB_L1 = KC.MO(1) 

# Keymap

if "_O_" in device_name:

    
    keyboard.keymap = [
            # Default - 0 - ok
            [
                # Row 1
                KC.TD(KC.Q, KC.ESC), KC.W, KC.E, KC.R, KC.T,# ok
                KC.P, KC.O, KC.I, KC.U, KC.Y, # ok

                # Row 2
                KC.TD(KC.A, KC.CAPS), KC.S, KC.D, KC.F, KC.G,# ok
                KC.CCEDILLA, KC.L, KC.K, KC.J, KC.H, # ok

                # Row 3
                KC.HT(KC.Z, KC.LGUI), KC.HT(KC.X, KC.LALT), KC.HT(KC.C, KC.LCTRL), KC.HT(KC.V, KC.LSHIFT), KC.B, # ok 
                KC.HT(KC.SEMICOLON, KC.RGUI), KC.HT(KC.DOT, KC.RALT), KC.HT(KC.COMM, KC.RCTRL), KC.HT(KC.M, KC.RSHIFT), KC.N, # ok

                # Tumb cluster
                XXXX, XXXX, KC.SPC, KC.BSPC, KC.LT(1, KC.TAB), # ok
                XXXX, XXXX, XXXX, KC.SPC, KC.LT(2,KC.ENT), 
           ],
            
            # Num n Symblos - 1 
           [
                KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, # ok
                KC.N0, KC.N9, KC.N8, KC.N7, KC.N6, # ok

                KC.QUOTE, KC.NUBS, XXXX, XXXX, XXXX,
                KC.RBRC, KC.LBRC, KC.EQL, KC.MINS, XXXX,

            
                KC.HT(KC.NON_US_BACKSLASH  , KC.LGUI), KC.HT(CTR_Z, KC.LALT),  KC.HT(CTR_C, KC.LCTRL), KC.HT(CTR_V, KC.LSHIFT), XXXX,
                KC.HT(XXXX, KC.LGUI), KC.HT(KC.SLASH, KC.RALT), KC.HT(KC.TILDE, KC.RCTRL), KC.HT(KC.GRAVE, KC.RSHIFT),XXXX,

            
                XXXX, XXXX, KC.SPC, KC.BSPC, KC.TAB,
                XXXX, XXXX, XXXX, KC.SPC, KC.ENT, 
            ], 


            # Functions - 2
            [
                KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,
                KC.F10, KC.F9, KC.F8, KC.F7,KC.F6,

                KC.CAPS, XXXX, KC.DEL, KC.ESC, XXXX,

                KC.F11, KC.RIGHT, KC.UP, KC.DOWN, KC.LEFT,

                XXXX, XXXX, XXXX, XXXX, XXXX,
                KC.F12,KC.PRINT_SCREEN , XXXX, XXXX, XXXX,

                XXXX, XXXX, KC.AUDIO_MUTE, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP,
                XXXX, XXXX, XXXX, XXXX, XXXX, 
            ]
    ]
else: 
# Keymap
    keyboard.keymap = [
            # Default - 0 - OK
            [
                # Row 1
                KC.TD(KC.Q, KC.ESC), KC.W, KC.E, KC.R, KC.T,
                KC.Y, KC.U, KC.I, KC.O, KC.P,

                # Row 2
                KC.TD(KC.A, KC.CAPS), KC.S, KC.D, KC.F, KC.G,
                KC.H, KC.J, KC.K, KC.L, KC_CES,

                # Row 3
                Z_WI, KC.HT(KC.X, KC.LALT), KC.HT(KC.C, KC.LCTRL), V_SH, KC.B, 
                KC.N, KC.HT(KC.M, KC.RSHIFT), KC.HT(KC.COMM, KC.RCTRL), KC.HT(KC.DOT, KC.RALT), KC.HT(KC_SCLN, KC.RGUI),

                # Tumb cluster
                # XXXX, XXXX, KC.SPC, KC.BSPC, KC.TAB,
                XXXX, XXXX, KC.SPC, KC.BSPC, KC.LT(1, KC.TAB),
                # XXXX, XXXX, KC.SPC, KC.BSPC, KC.MT(KC.TAB,KC.MO(1)),
                KC.LT(2, KC.ENT), KC.SPC, XXXX, XXXX, XXXX, 
            ],
            
            # Num n Symblos - 1 - OK
            [

                KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
                KC.N6, KC.N7, KC.N8, KC.N9, KC.N0,

                KC_QUO, XXXX, XXXX, XXXX, XXXX,
                XXXX,  KC.MINS, KC.EQL, KC.LBRC, KC.RBRC,
                
                KC.HT(KC_RBRC, KC.LGUI), KC.HT(CTR_Z, KC.LALT),  KC.HT(CTR_C, KC.LCTRL), KC.HT(CTR_V, KC.LSHIFT), XXXX,
                # XXXX, KC.HT(KC_ASC, KC.RSHIFT),  KC.HT(XXXX, KC.RCTRL), KC.HT(KC.X, KC.RALT), KC.HT(KC_RBRC, KC.LGUI),
                XXXX, KC.HT(KC_ASC, KC.RSHIFT),  KC.HT(KC.TILDE, KC.RCTRL), KC.HT(KC_SLASH, KC.RALT), KC.HT(KC_RBRC, KC.LGUI),

                


                XXXX, XXXX, KC.SPC, KC.BSPC, KC.TAB,
                KC.ENT, KC.SPC, XXXX, XXXX, XXXX, 
            ], 


            # Functions - 2
            [
                KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,
                KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,

                KC.CAPS, XXXX, KC.DEL, KC.ESC, XXXX,
                KC.LEFT,  KC.DOWN, KC.UP, KC.RIGHT, KC.F11,

                XXXX, XXXX, XXXX, XXXX, XXXX,
                XXXX, KC_ASC, XXXX, XXXX, KC.F12,

                XXXX, XXXX, KC.AUDIO_MUTE, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP,
                XXXX, XXXX, XXXX, XXXX, XXXX, 
            ]

    ]


print("strating thte keyboard")
if __name__ == '__main__':
    keyboard.go()




