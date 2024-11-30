from mysql import connector

my_connection = connector.connect(
    host="localhost", 
    user="root",
    password="secret_password"
)

my_cursor = my_connection.cursor()


try:
    my_cursor.execute("CREATE DATABASE banking")
    print(f"Database banking created successfully!")
except connector.Error as err:
    print(f"Error: {err}")
finally:
    print()
my_cursor.execute("USE banking")


my_cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
tables = ['Bill', 'PatientDiagnosis', 'Staff', 'Patient', 'Doctor']
for table in tables:
    my_cursor.execute(f"DROP TABLE IF EXISTS {table}")
my_cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")


# TASK 1


ddl_statements = [
    """
    CREATE TABLE Doctor (
        dr_code INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Fname VARCHAR(100),
        Gender VARCHAR(10),
        Address VARCHAR(200),
        Designation VARCHAR(50)
    ) ENGINE=INNODB;
    """,
    """
    CREATE TABLE Patient (
        pat_id INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Fname VARCHAR(100),
        Gender VARCHAR(10),
        Address VARCHAR(200),
        Tel VARCHAR(15),
        dr_code INT,
        FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code)
    ) ENGINE=INNODB;
    """,
    """
    CREATE TABLE Staff (
        staff_id INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(100),
        Dept VARCHAR(50),
        Gender VARCHAR(10),
        Address VARCHAR(200),
        Cell VARCHAR(15),
        dr_code INT,
        FOREIGN KEY (dr_code) REFERENCES Doctor(dr_code)
    ) ENGINE=INNODB;
    """,
    """
    CREATE TABLE PatientDiagnosis (
        diag_id INT AUTO_INCREMENT PRIMARY KEY,
        DiagDetails VARCHAR(500),
        Remark VARCHAR(500),
        Other VARCHAR(200),
        Diagdate DATE,
        pat_id INT,
        FOREIGN KEY (pat_id) REFERENCES Patient(pat_id)
    ) ENGINE=INNODB;
    """,
    """
    CREATE TABLE Bill (
        bill_no INT AUTO_INCREMENT PRIMARY KEY,
        PatName VARCHAR(100),
        DrName VARCHAR(100),
        DateTime DATE,
        Amount DECIMAL(10, 2),
        pat_id INT,
        FOREIGN KEY (pat_id) REFERENCES Patient(pat_id)
    ) ENGINE=INNODB;
    """
]


for ddl in ddl_statements:
    my_cursor.execute(ddl)


# TASK 2


add_doctor = "INSERT INTO doctor (name, fname, gender, address, designation) VALUES (%s, %s, %s, %s, %s)"

data_doctor = [
    ('Çakır', 'Aleyna', 'Female', '8764 Cedar St Fairview', 'Dermatologist'),
    ('Türüç', 'Deniz', 'Male', '1330 Pine St Clinton', 'Orthopedic'),
    ('Yılmaz', 'Sevgi', 'Female', '7348 Birch St Salem', 'Surgeon'),
    ('Demirel', 'Volkan', 'Male', '5450 Walnut St Springfield', 'Cardiologist'),
    ('Gönül', 'Eylül', 'Female', '1228 Elm St Riverside', 'Pediatrician'),
    ('Kurt', 'Emre', 'Male', '1485 Oak St Brooklyn', 'Neurologist'),
    ('Çetin', 'Aylin', 'Female', '2334 Pine St Blueberry', 'Endocrinologist'),
    ('Yüksel', 'Selin', 'Female', '3021 Maple St Whitehaven', 'Gastroenterologist'),
    ('Ekin', 'Murat', 'Male', '1600 Birch St Northwood', 'Radiologist'),
    ('Şahin', 'Tarkan', 'Male', '4800 Elm St Kingsland', 'Urologist'),
    ('Toprak', 'Derya', 'Female', '5147 Walnut St Glendale', 'Pulmonologist'),
    ('Aksoy', 'Fatma', 'Female', '1052 Oak St Riverside', 'Ophthalmologist'),
    ('Kılıç', 'Ali', 'Male', '2547 Pine St Maplewood', 'Psychiatrist'),
    ('Güzel', 'Serkan', 'Male', '3138 Maple St Dreamtown', 'Hematologist'),
    ('Acar', 'Merve', 'Female', '4780 Cedar St Redford', 'Rheumatologist')
]

for doc in data_doctor:
    my_cursor.execute(add_doctor,doc)

add_patient = "INSERT INTO Patient (Name, Fname, Gender, Address, Tel, dr_code) VALUES (%s, %s, %s, %s, %s, %s)"

data_patient = [
    ('Teke', 'Melis', 'Female', '789 Oak St', '1234567890', 1),
    ('Hasan', 'Ahmet', 'Male', '321 Pine St', '2345678901', 2),
    ('Teke', 'Elif', 'Female', '789 Oak St', '1234567890', 1),
    ('Songül', 'Can', 'Male', '321 Pine St', '2345678901', 2),
    ('Tekin', 'Deniz', 'Male', '8365 Main St Clinton', '5559998888', 5),
    ('Songül', 'Merve', 'Female', '6732 Walnut St Salem', '5552223344', 5),
    ('Gümüş', 'Ebru', 'Female', '1943 Maple St Riverside', '8002223344', 5),
    ('Soyman', 'Safiye', 'Female', '5039 Oak St Fairview', '5555551234', 8),
    ('Tangöz', 'Sarp', 'Male', '5171 Birch St Madison', '5554445678', 9),
    ('Kırmızı', 'Mehmet', 'Male', '2389 Elm St Clinton', '5557891234', 10),
    ('Akyüz', 'Eylül', 'Female', '7845 Main St Salem', '7008889988', 9),
    ('Yıldırım', 'Emir', 'Male', '2497 Cedar St Springfield', '6003334455', 9),
    ('Yıldız', 'Merve', 'Female', '9253 Pine St Greenville', '7775551122', 10),
    ('Kaya', 'Ayşe', 'Female', '3716 Oak St Harrisburg', '8004445566', 14),
    ('Şener', 'Ali', 'Male', '3021 Birch St Madison', '5551112233', 15),
    ('Tan', 'Mahmud', 'Male', '3021 Bach St Madson', '5554444433', 15)
]


for patient in data_patient:
    my_cursor.execute(add_patient, patient)


add_staff = "INSERT INTO Staff (Name, Dept, Gender, Address, Cell, dr_code) VALUES (%s, %s, %s, %s, %s, %s)"

data_staff = [
    ('Çakır', 'Dermatologist', 'Female', '8764 Cedar St, Fairview', '5601239876', 14),
    ('Türüç', 'Orthopedic', 'Male', '1330 Pine St, Clinton', '5664327890', 3),
    ('Yılmaz', 'Surgeon', 'Female', '7348 Birch St, Salem', '5478236549', 6),
    ('Demirel', 'Cardiologist', 'Male', '5450 Walnut St, Springfield', '5567891234', 7),
    ('Gönül', 'Pediatrician', 'Female', '1228 Elm St, Riverside', '5559988777', 2),
    ('Şen', 'Psychiatrist', 'Male', '3814 Pine St, Salem', '5982324650', 11),
    ('Potuk', 'Janitor', 'Female', '1426 Main St, Madison', '5984556677', None),
    ('Ak', 'Ophthalmologist', 'Male', '5516 Maple St, Fairview', '5448329653', 5),
    ('Erkin', 'Surgeon', 'Female', '7240 Oak St, Clinton', '5996654321', 12),
    ('Muriç', 'Radiologist', 'Male', '2645 Birch St, Harrisburg', '5511223344', 1),
    ('Bayındır', 'Janitor', 'Female', '4803 Elm St, Riverside', '5539988770', None),
    ('Can', 'Dentist', 'Female', '9263 Maple St, Springfield', '5423334444', 4),
    ('Kahveci', 'Pediatrician', 'Male', '5532 Pine St, Madison', '5999887766', 9),
    ('Güler', 'Janitor', 'Male', '1440 Cedar St, Clinton', '5364789012', None),
    ('Yılmaz', 'Janitor', 'Male', '2907 Walnut St, Fairview', '5449327451', None),
    ('Kökçü', 'Ophthalmologist', 'Female', '2630 Oak St, Riverside', '5506758394', 13),
    ('Yılmaz', 'Radiologist', 'Male', '3954 Birch St, Salem', '5988771000', 10),
    ('Ayhan', 'Cardiologist', 'Female', '4672 Maple St, Fairview', '5401112233', 15),
    ('Akgün', 'Dentist', 'Female', '7198 Cedar St, Riverside', '5883322445', 8),
    ('Yıldız', 'Administrator', 'Male', '8287 Oak St, Clinton', '5477112233', None)
]

for staff in data_staff:
    my_cursor.execute(add_staff, staff)

add_patientDiagnosis = "INSERT INTO PatientDiagnosis (DiagDetails, Remark, Diagdate, Other, pat_id) VALUES (%s, %s, %s, %s, %s)"

data_patientDiagnosis = [
    ('Hypertension', 'Patient advised to monitor blood pressure', '2024-11-10', 'No additional concerns', 1),
    ('Eczema', 'Prescribed topical creams', '2024-11-20', 'Follow-up in 2 weeks', 2),
    ('Anxiety', 'Patient recommended therapy and medication', '2024-11-15', 'No additional concerns', 4),
    ('Asthma', 'Patient prescribed inhaler', '2024-11-12', 'Regular follow-up every 3 months', 3),
    ('Back Pain', 'Patient advised bed rest and physiotherapy', '2024-11-08', 'No other concerns', 6),
    ('Diabetes', 'Patient advised to control sugar intake', '2024-11-05', 'Monitoring of blood sugar levels advised', 5),
    ('Migraine', 'Patient prescribed pain relief medication', '2024-11-18', 'Follow-up appointment in a month', 7),
    ('Chronic Fatigue', 'Patient recommended lifestyle changes', '2024-11-22', 'No other concerns', 10),
    ('Cold and Cough', 'Prescribed over-the-counter medication', '2024-11-14', 'Patient to rest', 9),
    ('Pneumonia', 'Patient advised antibiotics and rest', '2024-11-02', 'No additional concerns', 8),
    ('Psoriasis', 'Prescribed topical treatment', '2024-11-23', 'Monitor progress in 2 weeks', 11),
    ('High Cholesterol', 'Patient advised a low-fat diet and exercise', '2024-11-16', 'Follow-up in 3 months', 12),
    ('Gastritis', 'Patient prescribed antacids', '2024-11-19', 'No other concerns', 13),
    ('Depression', 'Patient recommended counseling and medication', '2024-11-03', 'Follow-up in 2 weeks', 14),
    ('Flu', 'Patient prescribed antiviral medication', '2024-11-09', 'Patient advised rest', 15)
]

for diagnosis in data_patientDiagnosis:
    my_cursor.execute(add_patientDiagnosis, diagnosis)


add_bill = "INSERT INTO Bill (PatName, DrName, Datetime, Amount, pat_id) VALUES (%s, %s, %s, %s, %s)"

data_bill = [
    ('Teke', 'Yılmaz', '2024-10-15', 45, 5),
    ('Hasan', 'Yılmaz', '2024-10-20', 88, 2),
    ('Teke', 'Yılmaz', '2024-10-18', 12, 4),
    ('Songül', 'Gönül', '2024-10-12', 15, 3),
    ('Süslü', 'Gönül', '2024-10-25', 23, 6),
    ('Tekin', 'Şen', '2024-10-08', 6, 1),
    ('Songül', 'Şen', '2024-10-05', 77, 7),
    ('Gümüş', 'Yıldız', '2024-10-23', 33, 10),
    ('Soyman', 'Gönül', '2024-10-22', 65, 2),
    ('Tangöz', 'Potuk', '2024-10-18', 68, 8),
    ('Kırmızı', 'Ak', '2024-10-17', 89, 11),
    ('Akyüz', 'Ak', '2024-10-14', 16, 9),
    ('Yıldırım', 'Ak', '2024-10-12', 28, 12),
    ('Yıldız', 'Erkin', '2024-10-09', 49, 13),
    ('Kaya', 'Muriç', '2024-10-26', 55, 14),
    ('Şener', 'Muriç', '2024-10-24', 28, 15),
    ('Teke', 'Yılmaz', '2024-11-15', 32, 5),
    ('Hasan', 'Yılmaz', '2024-11-20', 20, 2),
    ('Teke', 'Yılmaz', '2024-11-18', 14, 4),
    ('Songül', 'Gönül', '2024-11-12', 37, 3),
    ('Süslü', 'Gönül', '2024-11-25', 26, 6),
    ('Tekin', 'Şen', '2024-11-08', 10, 1),
    ('Songül', 'Şen', '2024-11-05', 20, 7),
    ('Gümüş', 'Yıldız', '2024-11-23', 30, 10),
    ('Soyman', 'Gönül', '2024-11-22', 27, 2),
    ('Tangöz', 'Potuk', '2024-11-18', 10, 8),
    ('Kırmızı', 'Ak', '2024-11-17', 15, 11),
    ('Akyüz', 'Ak', '2024-11-14', 16, 9),
    ('Yıldırım', 'Ak', '2024-11-12', 21, 12),
    ('Yıldız', 'Erkin', '2024-11-09', 25, 13),
    ('Kaya', 'Muriç', '2024-11-26', 33, 14),
    ('Şener', 'Muriç', '2024-11-24', 20, 15)
]

for bill in data_bill:
    my_cursor.execute(add_bill, bill)

my_connection.commit()


# TASK 3


my_cursor.execute(
    """
    SELECT doc.name , pat.name 
    FROM doctor doc RIGHT OUTER JOIN patient pat
    ON doc.dr_code = pat.dr_code;
    """
)

print("{:10} {:5} ".format("Doctor",  "Patient"))
for row in my_cursor:
    print(f"{row[0]:10} {row[1]:5}")


# TASK 4


my_cursor.execute(
    """
    SELECT PatName, DrName, SUM(Amount)
    FROM bill
    GROUP BY PatName, DrName
    HAVING SUM(Amount) > 100
    """
)

print("{:10} {:10} {:10}".format("Patient",  "Doctor", "Amount")) 
for row in my_cursor:
    print(f"{row[0]:10} {row[1]:10} {row[2]:10}")


# TASK 5


my_cursor.execute(
    """
    Select doc.name,Count(pat.name)
    From doctor doc LEFT OUTER JOIN patient pat 
    ON doc.dr_code = pat.dr_code
    Group by doc.name
    """
)

print("{:10} {:5} ".format("Doctor",  "Number of patient")) 
for row in my_cursor:
    print(f"{row[0]:10} {row[1]:5}")
