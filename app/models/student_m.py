from app import mysql
from flask import flash

class student_model:
    @classmethod
    def create_student(cls, id, firstname, lastname, course, year, gender):
        try:
            cur = mysql.new_cursor(dictionary=True)

            # Check if the ID is already taken
            cur.execute("SELECT id FROM student WHERE id = %s", (id,))
            existing_id = cur.fetchone()
            if existing_id:
                flash("ID is already taken.", "error")
                return "Failed to create student"

            # Insert the new student record
            cur.execute("INSERT INTO student (id, firstname, lastname, course, year, gender) VALUES (%s, %s, %s, %s, %s, %s)",
                        (id, firstname, lastname, course, year, gender))
            mysql.connection.commit()
            return "Student created successfully"
        except Exception as e:
            flash("Failed to create student.", "error")
            return "Failed to create student"
    
    @classmethod
    def get_students(cls):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT s.*, col.name AS college_name, col.code AS college_code FROM student s JOIN course c ON s.course = c.code INNER JOIN college col ON c.college = col.code")
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
    
    @classmethod
    def search_students_by_college(cls, search_query):
        cur = mysql.new_cursor(dictionary=True)
        cur.execute("SELECT s.*, col.name AS college_name, col.code AS college_code FROM student s JOIN course c ON s.course = c.code INNER JOIN college col ON c.college = col.code WHERE c.college = %s", (search_query,))
        students = cur.fetchall()
        cur.close()
        return students
    
    @classmethod
    def update_student(cls, student_id, new_id, new_firstname, new_lastname, new_course, new_year, new_gender):
        try:
            cur = mysql.new_cursor(dictionary=True)

            # Check if the new ID is already taken (excluding the current student's ID)
            cur.execute("SELECT id FROM student WHERE id = %s AND id != %s", (new_id, student_id))
            existing_id = cur.fetchone()
            if existing_id:
                flash("ID is already taken.", "error")
                return "Failed to update student"

            # Update the student record
            cur.execute("UPDATE student SET id=%s, firstname=%s, lastname=%s, course=%s, year=%s, gender=%s WHERE id=%s",
                        (new_id, new_firstname, new_lastname, new_course, new_year, new_gender, student_id))
            mysql.connection.commit()
            return "Student updated successfully"
        except Exception as e:
            return "Failed to update student"

    @classmethod
    def delete_student(cls, student_id):
        try:
            cur = mysql.new_cursor(dictionary=True)
            cur.execute("DELETE FROM student WHERE id = %s", (student_id,))
            mysql.connection.commit()
            cur.close()
            return {"success": True, "message": "Course deleted successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}