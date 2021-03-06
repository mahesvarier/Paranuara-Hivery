## Installation

The solution is to be ran in a python virtual environment.

### Pre - Requisites

MongoDB 

Python 3 

### Installation

Start `mongod` on standard port (27017), with _unsecured_ access. 

Clone this repo:

    $ git clone https://github.com/mahesvarier/Paranuara-Hivery.git

Navigate into Paranuara-Hivery/static folder:

    cd static

Import the JSON files into MongoDB using (if the OS is   Windows, please copy the files in static in the MongoDB installation folder and run the below commands to import the JSON):

    mongoimport --db Paranuara --collection Companies --file companies.json --jsonArray
    mongoimport --db Paranuara --collection People --file people.json --jsonArray

Navigate to the root folder:

    cd .. 

Install Pipenv library:

    pip install pipenv

Start the virtual environment:

    pipenv shell

Install packages within pipenv:

    pipenv install

On succesfull installation, start the server:

    python app.py

## Features:

The features developed are as per the Read Me file in static folder. Upon running the previous command to start the server, the port in which the server will be displayed. Append the API path below to the URL to fetch the details.

### Feature 1:
Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

    API: /fetch_employees?company_id=<index of company>

    For ex: http://127.0.0.1:5000/fetch_employees?company_id=1

### Feature 2:
Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.

    API: /fetch_friends?person_1=<index of first person>&person_2=<index of second person>

    For ex: http://127.0.0.1:5000/fetch_friends?person_1=1&person_2=2

### Feature 3:
Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

    API: /fetch_person?person_id=<index of the person>

    For ex: http://127.0.0.1:5000/fetch_person?person_id=4

## Running Unit Tests:

In order to run unit tests, run the below command in the project root folder.

### Feature 1:

    python -m unittest tests/test_fetch_employees.py

### Feature 2:

    python -m unittest tests/test_fetch_friends.py

### Feature 3:

    python -m unittest tests/test_fetch_people.py