import mysql.connector
# Configure MySQL connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Good2017!",
    "database": "HackerBank",
}
# Initialize global cursor
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(buffered=True)

def saveQuestions(question,answerA ,answerB ,answerC ,
        answerD ,answer ,rotation,correct ,module):
    try:
        sql = (
        "INSERT IGNORE INTO insuranceB (question,answerA ,answerB ,answerC ,"
        " answerD ,answer ,rotation ,correct ,module) "
        " VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s) "
        )
        val = (question,answerA ,answerB ,answerC , answerD ,answer ,rotation,correct ,module)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")


def getAllQuestion():
    #global cursor  # Use the global cursor   
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT * FROM notes")        
        data = cursor.fetchall()
        return data
    except Exception as e:
        return f"Error fetching records: {str(e)}"
    
def getModule2Question():
    #global cursor  # Use the global cursor   
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute("SELECT * FROM insuranceB where module=2")        
        data = cursor.fetchall()
        return data
    except Exception as e:
        return f"Error fetching records: {str(e)}"   
    

def save_note_to_db(question, answers, rotation):
    try:
        sql = (
        "INSERT IGNORE INTO notes (question, answers, rotation,correct) "
        "VALUES (%s, %s, %s, 1)"
        )
        val = (question, answers, rotation)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")

def save_note_to_db1(question, answers, rotation):
    try:
        sql = (
        "INSERT IGNORE INTO notes (question, answers, rotation,correct) "
        "VALUES (%s, %s, %s, 0)"
        )
        val = (question, question, answers, rotation)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")
