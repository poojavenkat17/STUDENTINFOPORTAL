from flask import Flask, request, render_template
import psycopg2
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="training",
        user="postgres",
        password="p0stgres"
    )

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search_student.html')
    else:
        #------------- Enter SQL code below this line-----------------
        studentname = request.form.get('studentname')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE name ILIKE %s", (f'%{studentname}%',))
        results = cur.fetchall()
        cur.close()
        conn.close()
        #-----------SQL code above this line---------------------
        return render_template('search_result.html', mylist=results)

@app.route('/search_scores', methods=['GET', 'POST'])
def search_scores():
    if request.method == 'GET':
        return render_template('search_scores.html')
    else:
        #------------- Enter SQL code below this line-----------------
        studentid = request.form.get('studentid')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT students.name, scores.studentid, scores.course_code, scores.score
            FROM scores
            JOIN students ON scores.studentid = students.studentid
            WHERE scores.studentid = %s
        """, (studentid,))
        results = cur.fetchall()
        cur.close()
        conn.close()
        #-----------SQL code above this line---------------------
        if len(results) == 0:
            return 'There is no one by that student ID'
        else:
            return render_template('score_result.html', mylist=results)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template('add_student.html')
    else:
        studentname = request.form.get('studentname')
        sid = request.form.get('id')
        address = request.form.get('address')
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        chem101 = request.form.get('chem101')
        math101 = request.form.get('math101')
        phys101 = request.form.get('phys101')
        
        if not studentname or not sid:
            return "Name and StudentID are required"
        else:
            sid = int(sid)
    #--------------------SQL code below----------------------------------------------
            conn = get_db_connection()
            cur = conn.cursor()
            try:
                # Insert into students table
                cur.execute("""
                    INSERT INTO students (name, studentid, address, gender, dob)
                    VALUES (%s, %s, %s, %s, %s)
                """, (studentname, sid, address, gender, dob))
                
                # Insert into scores table
                scores = [
                    (sid, 'CHEM101', float(chem101)),
                    (sid, 'MATH101', float(math101)),
                    (sid, 'PHYS101', float(phys101))
                ]
                cur.executemany("""
                    INSERT INTO scores (studentid, course_code, score)
                    VALUES (%s, %s, %s)
                """, scores)
                
                conn.commit()
            except psycopg2.Error as e:
                conn.rollback()
                return f"An error occurred: {e}"
            finally:
                cur.close()
                conn.close()
    #--------------------End SQL code ------------------------
            return f"The student {studentname} was created....OK"

@app.route('/courses')
def courses():
    #------------Enter SQL code below--------------
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            course_code,
            AVG(score) as average_score,
            COUNT(DISTINCT studentid) as total_students,
            SUM(CASE WHEN score >= 60 THEN 1 ELSE 0 END) as passing_students
        FROM scores
        GROUP BY course_code
    """)
    all_data = cur.fetchall()
    cur.close()
    conn.close()
    #--------------------End SQL code ------------------------
    return render_template('course_info.html', course_details=all_data)

if __name__ == '__main__':
    app.run(debug=True)