
from .Colors import Color, Colored
from .Alias import Alias
from typing import Callable, Optional

def arrangePlugins[ Plugin ]( **plugins:Plugin ) -> list[Plugin]:
    pluginStack:list[Plugin] = []
    for plugin in plugins:
        appendIndex:int = 0
        for index, arranged in enumerate(pluginStack):
            if plugins[plugin][0] < plugins[arranged][0]:
                appendIndex = index
            else:
                appendIndex = index + 1
        pluginStack.insert( appendIndex, plugin )
    return pluginStack


class ConsoleObject:

    def __init__[ zIndex ](
            self, name:str, fore:Color, back:Color,
            text:Color, highlight:Color,
            parser:Optional[Callable] = None,
            **plugins:tuple[zIndex,Callable,Color]
        ) -> None:
        self.highColor: Color = highlight
        self.textColor: Color = text
        self.textAlias: Alias = Alias( name, 15, fore, back )
        self.plugins  : dict  = plugins
        self.parser   : Optional[Callable] = parser
    
    def __call__[ PrintsToConsole ]( self, *parts:str, sep:str = " ", pSep:str = ":" ) -> PrintsToConsole:
        parsedPart:str = sep.join( parts )
        if self.parser != None:
            parsedPart:str = self.parser( parsedPart, textColor = self.textColor, highColor = self.highColor )
        
        pluginStack:list = arrangePlugins( **self.plugins )
        parsedPlugins = pSep.join([
            Colored.coloredForeground( self.plugins[plugin][1](), self.plugins[plugin][2] ) for plugin in pluginStack
        ])

        print( f"{self.textAlias}:{parsedPlugins}: {parsedPart}" )
