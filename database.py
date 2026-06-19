import sqlite3

# Database connection function
def get_connection():
    conn = sqlite3.connect("mira.db")
    conn.row_factory = sqlite3.Row
    return conn

# Table create function - app start ஆகும்போது run ஆகும்
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            email TEXT NOT NULL,
            glucose REAL NOT NULL,
            haemoglobin REAL NOT NULL,
            cholesterol REAL NOT NULL,
            remarks TEXT
        )
    ''')
    conn.commit()
    conn.close()

# CREATE - New patient add பண்ண
def create_patient(full_name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks))
    conn.commit()
    conn.close()

# READ - எல்லா patients-யும் get பண்ண
def get_all_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients')
    rows = cursor.fetchall()
    conn.close()
    return rows

# READ - ஒரு patient மட்டும் get பண்ண
def get_patient_by_id(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
    row = cursor.fetchone()
    conn.close()
    return row

# UPDATE - Patient record update பண்ண
def update_patient(patient_id, full_name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE patients
        SET full_name=?, dob=?, email=?, glucose=?, haemoglobin=?, cholesterol=?, remarks=?
        WHERE id=?
    ''', (full_name, dob, email, glucose, haemoglobin, cholesterol, remarks, patient_id))
    conn.commit()
    conn.close()

# DELETE - Patient record delete பண்ண
def delete_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
    conn.commit()
    conn.close()