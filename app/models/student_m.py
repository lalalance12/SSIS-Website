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