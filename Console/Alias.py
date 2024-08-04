
from .Colors import Color, Colored
from dataclasses import dataclass
from typing import Optional


class Alias:

    def __init__( 
            self, name:str, width:int,
            fore:Optional[Color] = None,
            back:Optional[Color] = None,
            active:Optional[bool] = True 
        ) -> None:
        self.__is_color_active = active
        self.__uncolored_alias = f"[{ name.title().center( width - 2 ) }]"
        self.__colored_alias   = Colored.coloredText(self.__uncolored_alias, fore, back)

    def __str__( self ) -> str:
        return self.__colored_alias if self.__is_color_active else self.__uncolored_alias
    