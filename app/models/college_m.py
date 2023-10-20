from app import mysql


class college_model:
    @classmethod
    def create_college(cls, code, name):
        try: 
            cur =mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO College (code, name) VALUES (%s,%s)", (code, name))
            mysql.connection.commit()
            cur.close()
            return "College created successfully"
        except Exception as e:
            return f"Failed to create College: {str(e)}"
    
    @classmethod
    def get_colleges(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM college")
        colleges = cur.fetchall()
        cur.close()
        return colleges 
    
    @classmethod
    def delete_college(cls, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM college WHERE code = %s", (code,))
            print(f"DELETE FROM college WHERE code = {code}")
            mysql.connection.commit()
            cur.close()
            return "College deleted successfully"
        except Exception as e:
            return f"Failed to delete College: {str(e)}"

    @classmethod
    def update_college(cls, college_code, new_code, new_name):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE College SET code = %s, name = %s WHERE code = %s", (new_code, new_name, college_code))
            mysql.connection.commit()
            cur.close()
            return "College updated successfully"
        except Exception as e:
            return f"Failed to update College: {str(e)}"

    @classmethod
    def get_college_by_code(cls, code):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM college WHERE code = %s", (code,))
        college = cur.fetchone()
        cur.close()
        return college
    
    @classmethod
    def search_colleges(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM college WHERE name LIKE %s OR code LIKE %s", (f"%{search_query}%", f"%{search_query}%"))
        colleges = cur.fetchall()
        cur.close()
        return colleges