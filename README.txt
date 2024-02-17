ABOUT MY PROJECT:
    This is a simple Flask application designed to handle job applications. 
    It provides two main functionalities:

Job Application Registration:
    Users can register job applications by making a POST request.
    The application stores various details such as applicant's name, date of birth, email, 
    phone number, education, job applied for, experience, and resume URL in a MySQL database 
    named myproject.
    Each new application is assigned a unique application number, which is incremented based on the 
    number of existing applications stored in the database.
    The application ensures that all required fields are provided in the POST request and returns 
    a success message upon successful registration.

Customer Data Retrieval:
    Users can retrieve customer data by making a GET request.
    The application queries the regdata table in the database to fetch the details of the applicant 
    associated with the provided application number.
    If the applicant exists in the database, their details are returned in JSON format.
    
Overall, this project provides a simple functional API for registering job applications 
and retrieving applicant data from a MySQL database using Flask.

note:
    The source code is located in a file named app.py within the backendAPI folder.