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
        "INSERT IGNORE INTO insurance4A (question,answerA ,answerB ,answerC ,"
        " answerD ,answer ,rotation ,correct ,module) "
        " VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s) "
        )
        val = (question,answerA ,answerB ,answerC , answerD ,answer ,rotation,correct ,module)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")
        if err.errno == err.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"An error occurred: {err}")



def saveWrongQuestions(question,answerA ,answerB ,answerC ,
        answerD ,answer ,rotation,correct ,module):
    try:
        sql = (
        "INSERT IGNORE INTO insurance4B (question,answerA ,answerB ,answerC ,"
        " answerD ,answer ,rotation ,correct ,module) "
        " VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s) "
        )
        val = (question,answerA ,answerB ,answerC , answerD ,answer ,rotation,correct ,module)
       
        cursor.execute(sql, val)
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error saving note: {err}")
        if err.errno == err.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"An error occurred: {err}")


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
        cursor.execute("SELECT * FROM insurance4A where module=2")        
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

def searchDB(con):
    try:
        cursor = conn.cursor(buffered=True)
        query = f"SELECT * FROM insurance4B where module=2 and  question like %s union SELECT * FROM insurance4A where module=2 and  question like %s"

        # Execute the query
        cursor.execute(query, (f"%{con}%",f"%{con}%",))
        
        data = cursor.fetchall()
        return data
    except Exception as e:
        return f"Error fetching records: {str(e)}"  
