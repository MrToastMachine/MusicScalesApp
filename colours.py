def hexToRGB(hexVal):
    if hexVal[0] == '#':
        hexVal = hexVal[1:]
    return tuple(int(hexVal[i:i+2], 16) for i in (0, 2, 4))

class Colours():
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    GRAY = (100,100,100)
    BROWN = (50,50,0)

    GOLD = (248,184,0)
    FOREST_GREEN = hexToRGB("#002500")
    MOSS_GREEN = hexToRGB("#929982")
    IMPERIAL_RED = hexToRGB("#FB3640")
    ROYAL_BLUE = hexToRGB("#1D3461")
    MID_BLUE = hexToRGB("#1F487E")

    KEYB_BG_COLOR = MOSS_GREEN
    RNM_BG_COLOR = FOREST_GREEN
    SCALES_BG_COLOR = FOREST_GREEN
    BUTTON_COLOR = WHITE
    BUTTON_COLOR_HIGHLIGHTED = GOLD

    WHITE_KEY_HIGHLIGHT = MID_BLUE
    BLACK_KEY_HIGHLIGHT = ROYAL_BLUE
    NOTE_NUM_COLOR = FOREST_GREEN

    BACKGROUND_COLOR = FOREST_GREEN

    SCALE_NOTES_COLORS = [hexToRGB("#ef4552"),
                          hexToRGB("#f7892a"),
                          hexToRGB("#f7d734"),
                          hexToRGB("#2eb87c"),
                          hexToRGB("#1bc1db"),
                          hexToRGB("#0b4e92"),
                          hexToRGB("#602e83")]

    