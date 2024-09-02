# STUDENTINFOPORTAL

A student information website with **HTML and Python Flask** as frontend and connecting the web application to the backend PostgreSQL Server

Key Features:
1. Student Search: Users can search for students by name.
2. Score Search: Ability to look up student scores by student ID.
3. Add New Student: Functionality to add new students with their personal information and course scores.
4. Course Information: Displays course details including average scores and passing rates.

Technical Stack:
- Frontend: HTML templates rendered by Flask
- Backend: Python Flask application
- Database: PostgreSQL

Main Components:
1. Flask Routes:
   - '/' : Search students
   - '/search_scores' : Search student scores
   - '/add_student' : Add new students
   - '/courses' : View course information

2. Database Interaction:
   - Uses psycopg2 to connect to PostgreSQL
   - Performs CRUD operations (Create, Read, Update, Delete) on student and score data

3. Data Models:
   - Students table: Stores student personal information
   - Scores table: Stores student scores for different courses

4. HTML Templates:
   - search_student.html
   - search_result.html
   - search_scores.html
   - score_result.html
   - add_student.html
   - course_info.html
<img width="917" alt="add" src="https://github.com/user-attachments/assets/96278962-05c2-493f-bee2-4d10f311f0be">
<img width="959" alt="searstud" src="https://github.com/user-attachments/assets/4f2a55d6-6ca9-463b-94ce-6fc922a1ee47">
<img width="958" alt="sesc" src="https://github.com/user-attachments/assets/c77dd732-899e-439a-b200-976595b7b248">


This web application provides a user-friendly interface for managing student information and academic performance, with Flask serving as the web framework to handle requests and interact with the PostgreSQL database.
