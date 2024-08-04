
from dataclasses import dataclass
from typing import Optional

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
