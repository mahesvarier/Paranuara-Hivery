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

    cd Paranuara-Hivery/static

Import the JSON files into MongoDB using:

    mongoimport --db Paranuara --collection Companies --file companies.json --jsonArray
    mongoimport --db Paranuara --collection People --file people.json --jsonArray

Install Pipenv library:

    pip install pipenv

Start the virtual environment:

    pipenv shell

Install packages within pipenv:

    pipenv install

On succesfull installation, start the server:

    python app.py
