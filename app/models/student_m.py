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
    def search_students_by_id(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE id LIKE %s", (f"%{search_query}%",))
        students = cur.fetchall()
        cur.close()
        return students

    @classmethod
    def search_students_by_firstname(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE firstname LIKE %s", (f"%{search_query}%",))
        students = cur.fetchall()
        cur.close()
        return students

    @classmethod
    def search_students_by_lastname(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE lastname LIKE %s", (f"%{search_query}%",))
        students = cur.fetchall()
        cur.close()
        return students

    @classmethod
    def search_students_by_course(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE course LIKE %s", (f"%{search_query}%",))
        students = cur.fetchall()
        cur.close()
        return students

    @classmethod
    def search_students_by_year(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE year LIKE %s", (f"%{search_query}%",))
        students = cur.fetchall()
        cur.close()
        return students

    @classmethod
    def search_students_by_gender(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT * FROM student WHERE gender LIKE %s", (f"%{search_query}%",))
        students = cur.fetchall()
        cur.close()
        return students