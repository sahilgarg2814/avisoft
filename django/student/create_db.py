import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="cHARIZOD100@"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE students_model")