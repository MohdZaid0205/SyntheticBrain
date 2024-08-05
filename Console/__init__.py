
from .Alias import Alias
from .Colors import Color, Colored
from .ConsoleObject import ConsoleObject

from .Parser import *
from .Plugins import *

RED     = Color.fromHEX('#ff5555')
WHITE   = Color.fromHEX('#f8f8f2')
BLUE    = Color.fromHEX('#6272a4')
GREEN   = Color.fromHEX('#50fa7b')
YELLOW  = Color.fromHEX('#f1fa8c')
GRAY    = Color.fromHEX('#44475a')
BLACK   = Color.fromHEX('#282a36')
VIOLET  = Color.fromHEX('#bd93f9')
ORANGE  = Color.fromHEX('#ffb86c')

commonPlugins:dict = {
    "timePlugin": ( 20, getCurrentTime, GRAY ),
}

class Console:
    Log: ConsoleObject = ConsoleObject(
        name = "Log", fore = WHITE, back=GRAY,
        text = GRAY, highlight = WHITE, parser=highlightParser,
        **commonPlugins
    )
    Warning: ConsoleObject = ConsoleObject(
        name = "Warning", fore = BLACK, back=ORANGE,
        text = GRAY, highlight = ORANGE, parser=highlightParser,
        **commonPlugins
    )
    Error: ConsoleObject = ConsoleObject(
        name = "Error", fore = BLACK, back=RED,
        text = GRAY, highlight = RED, parser=highlightParser,
        **commonPlugins
    )
    Output: ConsoleObject = ConsoleObject(
        name = "Output", fore = BLACK, back=BLUE,
        text = GRAY, highlight = BLUE, parser=highlightParser,
        **commonPlugins
    )
    Message: ConsoleObject = ConsoleObject(
        name = "Message", fore = BLACK, back=GREEN,
        text = GRAY, highlight = GREEN, parser=highlightParser,
        **commonPlugins
    )
