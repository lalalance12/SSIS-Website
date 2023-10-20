from app import mysql

class student_model:
    @classmethod
    def create_student(cls, id, firstname, lastname, course, year, gender):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO student (id, firstname, lastname, course, year, gender) VALUES (%s,%s,%s,%s,%s,%s )",(id, firstname, lastname, course, year, gender))
            mysql.connection.commit()
            return "Student created successfully"
        except Exception as e:
            return f"Failed to create student"
    
    @classmethod
    def get_students(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student")
        course = cur.fetchall()
        return course
    
    @classmethod
    def delete_student(cls, student_id):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM student WHERE id = %s", (student_id,))
            mysql.connection.commit()
            cur.close()
            return {"success": True, "message": "Student deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}
        

    @classmethod
    def update_student(cls, student_id, new_id, new_firstname, new_lastname, new_course, new_year, new_gender):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE student SET id = %s, firstname = %s, lastname = %s, course = %s, year = %s, gender = %s WHERE id = %s",(new_id, new_firstname, new_lastname, new_course, new_year, new_gender, student_id))
            mysql.connection.commit()
            cur.close()
            return "Student updated successfully"
        except Exception as e:
            return f"Failed to update student: {str(e)}"
        
    @classmethod
    def search_students(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR course LIKE %s OR year LIKE %s OR gender LIKE %s", (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"))
        students = cur.fetchall()
        cur.close()
        return students