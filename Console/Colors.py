
from dataclasses import dataclass
from typing import Optional

import os
os.system( "colors" )


@dataclass
class Color:

    r : int
    g : int
    b : int
    a : float

    @classmethod
    def fromRGB( cls, r:int, g:int, b:int, a:Optional[float] = 1 ) -> 'Color':
        return cls( r, g, b, a )
    
    @classmethod
    def fromHEX( cls, hex:str, a:Optional[float] = 1 ) -> 'Color':
        hex:str = hex.lstrip('#')

        if len(hex) == 3:
            r = int(hex[0] * 2, 16)
            g = int(hex[1] * 2, 16)
            b = int(hex[2] * 2, 16)
        else:
            r = int(hex[0:2], 16)
            g = int(hex[2:4], 16)
            b = int(hex[4:6], 16)
        
        if len(hex) == 8:
            a:float = int(hex[6:8], 16) / 255.0
        
        return cls( r, g, b, a )


class Colored:

    FOREGROUND  = "\033[38;2;{r};{g};{b}m"
    BACKGROUND  = "\033[48;2;{r};{g};{b}m"
    END_COLORS  = "\033[0m"

    @staticmethod
    def coloredForeground[ ColoredString ]( text:str, foreColor:Color ) -> ColoredString:
        color_sequence:str = Colored.FOREGROUND.format( r=foreColor.r, g=foreColor.g, b=foreColor.b )
        return f"{color_sequence}{text}{Colored.END_COLORS}"

    @staticmethod
    def coloredBackground[ ColoredString ]( text:str, backColor:Color ) -> ColoredString:
        color_sequence:str = Colored.BACKGROUND.format( r=backColor.r, g=backColor.g, b=backColor.b )
        return f"{color_sequence}{text}{Colored.END_COLORS}"
    
    @staticmethod
    def coloredText[ ColoredString ]( text:str, foreColor:Color, backColor:Color ) -> ColoredString:
        f_color_sequence:str = Colored.FOREGROUND.format( r=foreColor.r, g=foreColor.g, b=foreColor.b )
        b_color_sequence:str = Colored.BACKGROUND.format( r=backColor.r, g=backColor.g, b=backColor.b )
        return f"{f_color_sequence}{b_color_sequence}{text}{Colored.END_COLORS}"
