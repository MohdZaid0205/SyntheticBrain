
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


class DatabaseConnection:

    def __init__( self, databaseName:str ) -> None:
        try:
            Console.Log( f"Making Database connection with {databaseName}.db" )
            self.databaseName = databaseName
            self.connection   = sqlite3.connect( f"{DatabaseFolder}\\{databaseName}.db" )
            self.cursor       = self.connection.cursor()
            Console.Log( f"Success in making connection with {databaseName}.db")
        except Exception as anExc:
            Console.Error( f"*Failed to make connection* with *{databaseName}.db* due to *{anExc=}*" )
    
    def Execute( self, command:str ) -> None:
        self.cursor.execute( command )
        self.connection.commit()
    def Fetch( self, command:str, fetchall:bool = False, fetchmany:Optional[int] = 0 ) -> Any:
        self.cursor.execute( command )
        if fetchall:
            return self.cursor.fetchall()
        elif fetchmany:
            return self.cursor.fetchmany( fetchmany )
        return self.cursor.fetchone()
    
    def createTable( self, tableName:str, **tableParams:str ) -> None:
        try:
            Console.Log( f"Creating table {tableName} in {self.databaseName}" )
            tableBody = ",".join( [f"{param} {tableParams[param]}" for param in tableParams] )
            executableCommand = DatabaseCommands.createTableCommand.format( tableName=tableName, tableBody=tableBody )
            Console.Log( f"Table Creation Command : {executableCommand}" )
            self.Execute( executableCommand )
            Console.Log( f"Table {tableName} Successfully created" )
        except Exception as anExc:
            Console.Error( f"*Failed to make table:{tableName}* due to *{anExc=}*" )

    def dropTable( self, tableName:str ) -> None:
        try:
            Console.Log( f"Attempting to Drop table:{tableName}" )
            executableCommand = DatabaseCommands.dropTableCommand.format( tableName=tableName )
            Console.Log( f"Table Deletion Command : {executableCommand}" )
            self.Execute( executableCommand )
            Console.Log( f"Table {tableName} Successfully dropped" )
        except Exception as anExc:
            Console.Error( f"*Failed to drop table:{tableName}* due to *{anExc=}*" )

    def makeEntry( self, tableName:str, **entryParams ) -> None:
        try:
            Console.Log( f"Attempting to make an Entry in table:{tableName}" )
            columnNames = ",".join(entryParams.keys())
            entryValues = ",".join([f"'{v}'" if isinstance(v, str) else str(v) for v in entryParams.values()])
            executableCommand = DatabaseCommands.insertEntryCommand.format( tableName=tableName, columnNames=columnNames, entryValues=entryValues )
            Console.Log( f"Entry Insertion Command : {executableCommand}" )
            self.Execute( executableCommand )
            Console.Log( f"Entry into:{tableName} Successfully made" )
        except Exception as anExc:
            Console.Error( f"*Failed to make entry* in:*{tableName}* due to *{anExc=}*" )

    def deleteEntry( self, tableName:str, where:str ) -> None:
        try:
            Console.Log( f"Attempting to remove an Entry from table:{tableName}" )
            executableCommand = DatabaseCommands.deleteEntryCommand.format( tableName=tableName, deletionConditions=where )
            Console.Log(f"Entry Deletion Command : {executableCommand}")
            self.Execute( executableCommand )
            Console.Log(f"Entry from:{tableName} Successfully deleted")
        except Exception as anExc:
            Console.Error(f"*Failed to delete entry* from:*{tableName}* due to *{anExc}*")

    def selectEntry( self, tableName:str, columns:str, where:str ) -> str:
        try:
            Console.Log( f"Attempting to retrieve an Entry from table:{tableName}" )
            executableCommand = DatabaseCommands.selectEntryCommand.format( tableName=tableName, columnNames=columns, selectionConditions=where )
            Console.Log(f"Entry selection Command : {executableCommand}")
            result =  self.Fetch( executableCommand )
            Console.Log(f"Entry from:{tableName} Successfully retrieved")
            return result
        except Exception as anExc:
            Console.Error(f"*Failed to retrieve entry* from:*{tableName}* due to *{anExc}*")
