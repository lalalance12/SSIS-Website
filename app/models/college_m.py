from app import mysql


class college_model:
    @classmethod
    def create_college(cls, code, name):
        try: 
            cur =mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO College (code, name) VALUES (%s,%s)", (code, name))
            mysql.connection.commit()
            return "College created successfully"
        except Exception as e:
            return f"Failed to create College: {str(e)}"
    
    @classmethod
    def get_colleges(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM college")
        colleges = cur.fetchall()
        return colleges 
    
    @classmethod
    def delete_college(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("DELETE FROM College WHERE code")