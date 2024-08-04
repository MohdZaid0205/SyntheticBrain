
from .Colors import Color, Colored

def highlightParser( text:str, textColor:Color, highColor:Color ) -> str:
    parts:list[str] = text.split("*")
    colored:str = ""
    for index, part in enumerate(parts):
        if index % 2 == 0:
            colored += Colored.coloredForeground( part, textColor )
        else:
            colored += Colored.coloredForeground( part, highColor )
    return colored
