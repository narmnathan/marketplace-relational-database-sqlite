import sqlite3
import pandas as pd

# goal: hosting online marketplace. csv includes
# various data on user, account_info, and mailing
# separate into relational databases

# create dataframes from csv
df = pd.read_csv('test_data.csv')

# login: stores id, email, password
# mailing: stores id, name, phone, mailing address
# card: stores id, name, card_number, cvv, expiration_date
login = df[['name', 'email', 'password']]
mailing = df[['name', 'phone', 'mailing_address']]
card = df[['name', 'card_number', 'cvv', 'expiration_date']]

# creating sql database and tables
db = sqlite3.connect('marketplace.db')
cursor = db.cursor()

# creating tables -- no longer needed after first-time use
def create():
    login_query = """
    CREATE TABLE login (
    name char PRIMARY KEY,
    email varchar,
    password varchar
    )
    """
    mailing_query = """
    CREATE TABLE mailing (
    name char PRIMARY KEY,
    phone varchar,
    mailing_address varchar 
    )
    """
    card_query = """
    CREATE TABLE card (
    name char PRIMARY KEY,
    card_number varchar,
    cvv varchar,
    expiration_date varchar
    )
    """
    cursor.execute(login_query)
    cursor.execute(mailing_query)
    cursor.execute(card_query)
    print("Database tables created")

# filling in tables with dataframes -- no longer needed after first-time use
def fill():
    login.to_sql(name='login', con=db, if_exists='append', index=False, method=None)
    mailing.to_sql(name='mailing', con=db, if_exists='append', index=False, method=None)
    card.to_sql(name='card', con=db, if_exists='append', index=False, method=None)
    print("Database tables filled")
    
# clearing database tables -- testing purposes
def clear():
    query1 = """
        DROP TABLE login;
        """
    query2 = """
        DROP TABLE mailing;
        """
    query3 = """
        DROP TABLE card;
        """
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    print("Database tables cleared")

# to-do:
# xeus-sqlite connect jupyter notebook & display sql table data & manipulation