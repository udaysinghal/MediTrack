# MediTrack: Advanced Disease Surveillance System

## Overview
MediTrack is a web-based disease tracking system built using Flask and MySQL. It enables users to query patient data based on disease and location, providing detailed patient information and consolidated statistics for better analysis.

## Features
- **User-friendly Interface**: Search for disease prevalence in specific cities with detailed patient info.
- **Database Management**: Normalized schemas to ensure data integrity and efficiency.
- **Data Visualization**: View consolidated statistics, including total patients, gender distribution, and age range.
- **Backend-Frontend Integration**: Developed with Flask, MySQL, HTML, and CSS for dynamic content rendering.

## Technologies Used
- **Backend**: Python (Flask), MySQL
- **Frontend**: HTML, CSS, Jinja2
- **Database**: MySQL

## Installation and Setup
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MediTrack
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MySQL database**
   - Create a MySQL database.
   - Import the database schema (`schema.sql`).
   - Update database credentials in `config.py`.

5. **Run the application**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000/`

## Usage
1. Open the application in a browser.
2. Click on **Search for Diseases Topologically**.
3. Enter the disease name and location.
4. View detailed patient records in a tabular format.
5. Click **Consolidated View** for aggregated statistics.

## Project Structure
```
MediTrack/
│── templates/
│   │── index.html
│   │── results.html
│   │── consolidated.html
│── static/
│── app.py
│── config.py
│── requirements.txt
│── schema.sql
│── README.md
```

## Contributing
Feel free to fork the repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

## Contact
For any queries or collaboration, contact **Uday Singhal**.

