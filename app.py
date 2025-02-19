from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you replace this with a strong secret key

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',  # replace with your MySQL username
        password='Uday@09122004',  # replace with your MySQL password
        database='mydatabase'  # replace with your MySQL database name
    )

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/search_disease')
def search_disease():
    return render_template('search_disease.html')

@app.route('/search', methods=['POST'])
def search():
    disease = request.form['disease']
    city = request.form['city']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT Patient.PatientID, Patient.Name, Disease.DiseaseName, City.CityName, Patient.Age, Patient.Gender 
        FROM Patient 
        JOIN City ON Patient.CityID = City.CityID
        JOIN Patient_Disease ON Patient.PatientID = Patient_Disease.PatientID
        JOIN Disease ON Patient_Disease.DiseaseID = Disease.DiseaseID
        WHERE Disease.DiseaseName = %s AND City.CityName = %s
    """
    cursor.execute(query, (disease, city))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('results.html', results=results, disease=disease, city=city)

@app.route('/consolidated_view')
def consolidated_view():
    disease = request.args.get('disease')
    city = request.args.get('city')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    query_total = """
        SELECT COUNT(*) 
        FROM Patient 
        JOIN City ON Patient.CityID = City.CityID
        JOIN Patient_Disease ON Patient.PatientID = Patient_Disease.PatientID
        JOIN Disease ON Patient_Disease.DiseaseID = Disease.DiseaseID
        WHERE Disease.DiseaseName = %s AND City.CityName = %s
    """
    cursor.execute(query_total, (disease, city))
    total_patients = cursor.fetchone()[0]
    
    query_male = """
        SELECT COUNT(*) 
        FROM Patient 
        JOIN City ON Patient.CityID = City.CityID
        JOIN Patient_Disease ON Patient.PatientID = Patient_Disease.PatientID
        JOIN Disease ON Patient_Disease.DiseaseID = Disease.DiseaseID
        WHERE Disease.DiseaseName = %s AND City.CityName = %s AND Patient.Gender = 'Male'
    """
    cursor.execute(query_male, (disease, city))
    male_patients = cursor.fetchone()[0]
    
    query_female = """
        SELECT COUNT(*) 
        FROM Patient 
        JOIN City ON Patient.CityID = City.CityID
        JOIN Patient_Disease ON Patient.PatientID = Patient_Disease.PatientID
        JOIN Disease ON Patient_Disease.DiseaseID = Disease.DiseaseID
        WHERE Disease.DiseaseName = %s AND City.CityName = %s AND Patient.Gender = 'Female'
    """
    cursor.execute(query_female, (disease, city))
    female_patients = cursor.fetchone()[0]
    
    query_age = """
        SELECT MIN(Patient.Age), MAX(Patient.Age) 
        FROM Patient 
        JOIN City ON Patient.CityID = City.CityID
        JOIN Patient_Disease ON Patient.PatientID = Patient_Disease.PatientID
        JOIN Disease ON Patient_Disease.DiseaseID = Disease.DiseaseID
        WHERE Disease.DiseaseName = %s AND City.CityName = %s
    """
    cursor.execute(query_age, (disease, city))
    age_range = cursor.fetchone()
    
    cursor.close()
    conn.close()

    return render_template('consolidated_view.html', total_patients=total_patients, male_patients=male_patients, female_patients=female_patients, age_range=age_range)

if __name__ == '__main__':
    app.run(debug=True)
    
    
# from flask import Flask, request, render_template
# import mysql.connector

# app = Flask(__name__)

# def get_db_connection():
#     return mysql.connector.connect(
#         host='localhost',
#         user='root',  # replace with your MySQL username
#         password='Uday@09122004',  # replace with your MySQL password
#         database='mydatabase'  # replace with your MySQL database name
#     )


# # @app.route('/')
# # def welcome():
# #     return render_template('welcome.html')

# # @app.route('/search_disease')
# # def search_disease():
# #     return render_template('search_disease.html')

# # @app.route('/search', methods=['POST'])
# # def search():
# #     disease = request.form['disease']
# #     city = request.form['city']

# #     conn = get_db_connection()
# #     cursor = conn.cursor(dictionary=True)
# #     query = "SELECT * FROM Patients JOIN PatientDiseases ON Patients.PatientID = PatientDiseases.PatientID JOIN Diseases ON PatientDiseases.DiseaseID = Diseases.DiseaseID WHERE Diseases.Name = %s AND Cities.Name = %s"
# #     cursor.execute(query, (disease, city))
# #     results = cursor.fetchall()
# #     cursor.close()
# #     conn.close()

# #     return render_template('results.html', results=results, disease=disease, city=city)

# # @app.route('/consolidated_view')
# # def consolidated_view():
# #     disease = request.args.get('disease')
# #     city = request.args.get('city')

# #     conn = get_db_connection()
# #     cursor = conn.cursor()
    
# #     query_total = "SELECT COUNT(*) FROM Patients JOIN PatientDiseases ON Patients.PatientID = PatientDiseases.PatientID JOIN Diseases ON PatientDiseases.DiseaseID = Diseases.DiseaseID WHERE Diseases.Name = %s AND Cities.Name = %s"
# #     cursor.execute(query_total, (disease, city))
# #     total_patients = cursor.fetchone()[0]
    
# #     query_male = "SELECT COUNT(*) FROM Patients JOIN PatientDiseases ON Patients.PatientID = PatientDiseases.PatientID JOIN Diseases ON PatientDiseases.DiseaseID = Diseases.DiseaseID WHERE Diseases.Name = %s AND Cities.Name = %s AND Patients.Gender = 'Male'"
# #     cursor.execute(query_male, (disease, city))
# #     male_patients = cursor.fetchone()[0]
    
# #     query_female = "SELECT COUNT(*) FROM Patients JOIN PatientDiseases ON Patients.PatientID = PatientDiseases.PatientID JOIN Diseases ON PatientDiseases.DiseaseID = Diseases.DiseaseID WHERE Diseases.Name = %s AND Cities.Name = %s AND Patients.Gender = 'Female'"
# #     cursor.execute(query_female, (disease, city))
# #     female_patients = cursor.fetchone()[0]
    
# #     query_age = "SELECT MIN(Patients.Age), MAX(Patients.Age) FROM Patients JOIN PatientDiseases ON Patients.PatientID = PatientDiseases.PatientID JOIN Diseases ON PatientDiseases.DiseaseID = Diseases.DiseaseID WHERE Diseases.Name = %s AND Cities.Name = %s"
# #     cursor.execute(query_age, (disease, city))
# #     age_range = cursor.fetchone()
    
# #     cursor.close()
# #     conn.close()

# #     return render_template('consolidated_view.html', total_patients=total_patients, male_patients=male_patients, female_patients=female_patients, age_range=age_range)

# # if __name__ == '__main__':
# #     app.run(debug=True)



# @app.route('/')
# def welcome():
#     return render_template('welcome.html')

# @app.route('/search_disease')
# def search_disease():
#     return render_template('search_disease.html')

# @app.route('/search', methods=['POST'])
# def search():
#     disease = request.form['disease']
#     city = request.form['city']

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = "SELECT * FROM patients WHERE disease = %s AND city = %s"
#     cursor.execute(query, (disease, city))
#     results = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     return render_template('results.html', results=results, disease=disease, city=city)


# # @app.route('/search', methods=['GET', 'POST'])
# # def search():
# #     if request.method == 'POST':
# #         disease = request.form['disease']
# #         city = request.form['city']
        
# #         cursor = mysql.connection.cursor()
        
# #         query = """
# #         SELECT Patient.Name, Patient.Age, Patient.Gender, Disease.DiseaseName, City.CityName
# #         FROM Patient
# #         JOIN Disease ON Patient.DiseaseID = Disease.DiseaseID
# #         JOIN City ON Patient.CityID = City.CityID
# #         WHERE Disease.DiseaseName = %s AND City.CityName = %s
# #         """
        
# #         cursor.execute(query, (disease, city))
# #         results = cursor.fetchall()
        
# #         cursor.close()
        
# #         return render_template('results.html', results=results)
    
# #     return render_template('search.html')

# @app.route('/consolidated_view')
# def consolidated_view():
#     disease = request.args.get('disease')
#     city = request.args.get('city')

#     conn = get_db_connection()
#     cursor = conn.cursor()
    
#     query_total = "SELECT COUNT(*) FROM patients WHERE disease = %s AND city = %s"
#     cursor.execute(query_total, (disease, city))
#     total_patients = cursor.fetchone()[0]
    
#     query_male = "SELECT COUNT(*) FROM patients WHERE disease = %s AND city = %s AND gender = 'Male'"
#     cursor.execute(query_male, (disease, city))
#     male_patients = cursor.fetchone()[0]
    
#     query_female = "SELECT COUNT(*) FROM patients WHERE disease = %s AND city = %s AND gender = 'Female'"
#     cursor.execute(query_female, (disease, city))
#     female_patients = cursor.fetchone()[0]
    
#     query_age = "SELECT MIN(age), MAX(age) FROM patients WHERE disease = %s AND city = %s"
#     cursor.execute(query_age, (disease, city))
#     age_range = cursor.fetchone()
    
#     cursor.close()
#     conn.close()

#     return render_template('consolidated_view.html', total_patients=total_patients, male_patients=male_patients, female_patients=female_patients, age_range=age_range)

# if __name__ == '__main__':
#     app.run(debug=True)
