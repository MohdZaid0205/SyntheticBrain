
from .Colors import Color, Colored
from .Alias import Alias
from typing import Callable, Optional

def arrangePlugins[ Plugin ]( **plugins:Plugin ) -> list[Plugin]:
    pluginStack:list[Plugin] = []
    for plugin in plugins:
        appendIndex:int = 0
        for index, arranged in enumerate(pluginStack):
            if plugin[0] < arranged[0]:
                appendIndex = index - 1
            else:
                appendIndex = index + 1
        pluginStack.append( plugin, appendIndex )
    return pluginStack


class ConsoleObject:

    def __init__[ zIndex ](
            self, name:str, fore:Color, back:Color,
            text:Color, highlight:Color,
            **plugins:tuple[zIndex,Callable,Color]
        ) -> None:
        self.highColor: Color = highlight
        self.textColor: Color = text
        self.textAlias: Alias = Alias( name, 15, fore, back )
        self.plugins  : dict  = plugins
    
    def __call__[ PrintsToConsole ]( self, *parts:str, parser:Callable = None ) -> PrintsToConsole:
        if parser != None:
            parsedPart:str = parser( *parts, textColor = self.textColor, highColor = self.highColor )
        else:
            parsedPart:str = " ".join( parts )
        
        pluginStack:list = arrangePlugins( self.plugins )
        parsedPlugins = ":".join([
            Colored.coloredForeground( self.plugins[plugin](), self.plugins[plugin] ) for plugin in pluginStack
        ])

        print( f"{self.textAlias}:{parsedPlugins} => {parsedPart}" )
