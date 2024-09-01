import psycopg2


conn = psycopg2.connect(
                        host="localhost",
                        database="training",
                        user="postgres",
                        password="admin")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS scores")
cur.execute("DROP TABLE IF EXISTS students")

#------------------Create the students table---------------------------------------------------------
cur.execute("""CREATE TABLE IF NOT EXISTS students(
                                 name TEXT NOT NULL,
                                 studentid INTEGER PRIMARY KEY NOT NULL,
                                 address TEXT,
                                 gender TEXT,
                                 dob TEXT)
                                 
          """)
conn.commit()


manyusers = [
                ('John Brown',111,'Austin, TX','male','01-01-1985'),
                ('John Green',222, 'Long Island, NY','male','07-02-1985'),
                ('Helga Schwarz', 333, 'Berlin, DE', 'female', '01-03-1986'),
                ('Ken Buru', 444, 'Tokyo, JP', 'male', '08-04-1990'),
                ('Maria Giallo', 555, 'Rome, IT', 'female', '10-17-1983')
            ]
sql_string = "INSERT INTO students(name, studentid, address, gender, dob) VALUES(%s,%s,%s,%s,%s)"
cur.executemany(sql_string, manyusers)
conn.commit()


#------------------Create the scores table---------------------------------------------------------
cur.execute("""CREATE TABLE scores(
                                 studentid INTEGER NOT NULL,
                                 course_code TEXT NOT NULL,
                                 score REAL NOT NULL,
                                 FOREIGN KEY(studentid) REFERENCES students(studentid))
         """)
conn.commit()



manyscores = [
                (111, 'CHEM101', 75.2),
                (111, 'PHYS101', 40.5),
                (111, 'MATH101', 90.2),
                (222, 'MATH101', 65.5),
                (222, 'PHYS101', 75.2),
                (333, 'MATH101', 80.5),
                (333, 'CHEM101', 90.1),
                (444, 'MATH101', 55.1),
                (555, 'CHEM101', 65.7),
                (555, 'PHYS101', 43.2)
]
cur.executemany("INSERT INTO scores VALUES (%s, %s, %s)", manyscores)
conn.commit()
conn.close()



print("Two tables created: students and scores")
print("Seed data inserted into the tables")
print("Script ran successfully")
 











