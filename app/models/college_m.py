from app import mysql


class college_model:
    @classmethod
    def create_college(cls, name, code):
        try: 
            cur =mysql.new_cursor(dictionary=True)
            cur.execute("INSERT INTO College (code, name) VALUES (%s,%s)", (code, name))
            mysql.connection.commit()
            return "College created successfully"
        except Exception as e:
            return f"Failed to create College: {str(e)}"
