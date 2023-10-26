from app import mysql


class course_model:
    @classmethod
    def create_course(cls, code, name, college):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO course (code, name, college) VALUES (%s, %s, %s)", (code, name, college))
            mysql.connection.commit()
            return "Course created successfully"
        except Exception as e:
            return f"Failed to create course: {str(e)}"

    @classmethod
    def get_courses(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM course")
        courses = cur.fetchall()
        return courses

    @classmethod
    def delete_course(cls, code):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM course WHERE code = %s", (code,))
            mysql.connection.commit()
            cur.close()
            return {"success": True, "message": "Course deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}

    @classmethod
    def update_course(cls, course_code, new_code, new_name, new_college):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("UPDATE course SET code = %s, name = %s, college = %s WHERE code = %s", (new_code, new_name, new_college, course_code))
            mysql.connection.commit()
            cur.close()
            return "Course updated successfully"
        except Exception as e:
            return f"Failed to update course: {str(e)}"
    
    @classmethod
    def search_courses_by_code(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM course WHERE code LIKE %s", (f"%{search_query}%",))
        courses = cur.fetchall()
        cur.close()
        return courses

    @classmethod
    def search_courses_by_name(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM course WHERE name LIKE %s", (f"%{search_query}%",))
        courses = cur.fetchall()
        cur.close()
        return courses

    @classmethod
    def search_courses_by_college(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM course WHERE college LIKE %s", (f"%{search_query}%",))
        courses = cur.fetchall()
        cur.close()
        return courses