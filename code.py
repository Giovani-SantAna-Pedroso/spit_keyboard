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
holdtap.tap_time = 120
keyboard.modules.append(holdtap)

# Layers 
layers = Layers()
keyboard.modules.append(layers)

# Split config
side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
if side == SplitSide.RIGHT:

    split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT
                  , data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
    keyboard.col_pins = (board.GP15,board.GP14, board.GP13, board.GP12, board.GP11) # Cols
    keyboard.row_pins = (board.GP19, board.GP18, board.GP17, board.GP16)             # Rows
else: 
    split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT
                  , data_pin=board.GP0, data_pin2=board.GP1, use_pio=True, uart_flip = True)
    keyboard.col_pins = (board.GP15,board.GP14, board.GP13, board.GP12, board.GP11) # Cols
    keyboard.row_pins = (board.GP19, board.GP18, board.GP17, board.GP16)             # Rows
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
KC_CES = KC.SCOLON
KC_QUO = KC.GRAVE
KC_ASC = KC.LBRC
KC_LBRC = KC.RBRC
KC_RBRC = KC.BSLS
KC_GRAVE = KC.QUOTE
KC_SLASH =KC.RALT(KC.Q) 
KC_QUESTION =KC.RALT(KC.W) 
KC_SCLN = KC.SLASH

V_SH = KC.HT(KC.V, KC.LSHIFT)
C_CR = KC.HT(KC.C, KC.LCTRL)
X_AL = KC.HT(KC.X, KC.LALT)
Z_WI = KC.HT(KC.Z, KC.LGUI)

M_SH = KC.HT(KC.M, KC.RSHIFT)
CO_AL = KC.HT(KC.COMM, KC.RALT)
DO_CR = KC.HT(KC.DOT, KC.RCTRL)
SE_WI = KC.HT(KC.A, KC.RGUI)


CTR_Z=KC.MACRO(Press(KC.RCTRL), Tap(KC.Z), Release(KC.RCTRL))
CTR_C=KC.MACRO(Press(KC.RCTRL), Tap(KC.C), Release(KC.RCTRL))
CTR_V=KC.MACRO(Press(KC.RCTRL), Tap(KC.V), Release(KC.RCTRL))

TAB_L1 = KC.MO(1) 

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
            Z_WI, X_AL, C_CR, V_SH, KC.B, 
            KC.N, M_SH, KC.HT(KC.COMM, KC.RCTRL), KC.HT(KC.DOT, KC.RALT), KC.HT(KC_SCLN, KC.RGUI),

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
            XXXX,  KC.MINS, KC.EQL, KC_GRAVE, KC_LBRC,

            
            KC.HT(KC_RBRC, KC.LGUI), KC.HT(CTR_Z, KC.LALT),  KC.HT(CTR_C, KC.LCTRL), KC.HT(CTR_V, KC.LSHIFT), XXXX,
            # XXXX, KC.HT(KC_ASC, KC.RSHIFT),  KC.HT(XXXX, KC.RCTRL), KC.HT(KC.X, KC.RALT), KC.HT(KC_RBRC, KC.LGUI),
            XXXX, KC.HT(KC_ASC, KC.RSHIFT),  KC.HT(KC_QUESTION, KC.RCTRL), KC.HT(KC_SLASH, KC.RALT), KC.HT(KC_RBRC, KC.LGUI),


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


