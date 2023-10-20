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
        course = cur.fetchall()
        return course

    


