
from Console import Console

from typing import Any, Optional
import sqlite3
import os


DatabaseFolder: os.path = "Temp\\Database"
if not os.path.exists( DatabaseFolder ):
    Console.Warning( f"*Database folder* is currently *Absent* from Temp folder." )
    os.makedirs( DatabaseFolder )
    Console.Log( f"Made folder for Database files." )


class DatabaseCommands:
    createTableCommand:str = "CREATE TABLE IF NOT EXISTS {tableName} ( {tableBody} )"
    dropTableCommand  :str = "DROP TABLE IF EXISTS {tableName}"
    insertEntryCommand:str = "INSERT INTO {tableName} ({columnNames}) VALUES ({entryValues})"
    deleteEntryCommand:str = "DELETE FROM {tableName} WHERE {deletionConditions}"
    selectEntryCommand:str = "SELECT {columnNames} FROM {tableName} WHERE {selectionConditions}"