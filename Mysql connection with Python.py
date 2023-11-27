#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql')


# In[2]:


pip install mysql-connector-python


# In[3]:


import mysql.connector


# In[4]:


from mysql.connector import Error


# In[5]:


import pandas as pd


# In[8]:


def create_connection(host_name,user_name,password):
  connection = None
  try:
    connection = mysql.connector.connect(host=host_name, user=user_name,passwd=password)
    print("Mysql connection has been established")
  except Error as err:
    print(f"Error: '{err}'")
  
  return connection

password = 'Your database connection password'

main_connection = create_connection("localhost","root",password)


# In[10]:


def createDatabase_query(main_connection, query):
    cursor = main_connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

        
database_name='python_conn'
database_query =f'create database {database_name}'

createDatabase_query(main_connection, database_query)


# In[11]:


def database_connection(host_name,user_name,password,db_name):
  connection = None
  try:
    connection = mysql.connector.connect(host=host_name, user=user_name,passwd=password,database=db_name)
    print("Mysql database has been established")
  except Error as err:
    print(f"Error: '{err}'")
  
  return connection

connection = database_connection("localhost","root",password,database_name)


# In[12]:


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed.")
    except Error as err:
        print(f"Error: '{err}'")


# In[20]:


insert_query="""
create table Data(
pid int auto_increment primary key,
pname varchar(255) not null,
address varchar(255) default null,
email varchar(255) unique key,
age int,
height decimal(10,2),
enroll_date timestamp not null,
course_starting_date date not null);"""

execute_query(connection, insert_query)


# In[22]:


insert_data_query ="""
insert into Data values
(1,'Mike','340A','mike12@gmail.com',26,5.83,'2023-10-25','2023-10-25'),
(2,'Shinoda','341A','shinoda12@gmail.com',28,5.93,'2023-10-25','2023-10-24'),
(3,'Xiomi','340A','xiomi@gmail.com',27,5.93,'2023-10-23 11:32:08','2023-10-24');
"""
execute_query(connection, insert_data_query)


# In[24]:


def read_data_query_execute(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
        
read_data_query='select * from Data'
results = read_data_query_execute(connection, read_data_query)


# In[29]:


for i in list(results):
    print(i)


# In[32]:


read_pattern_data_query="select * from Data where pname like '%i' "

pattern_results = read_data_query_execute(connection, read_pattern_data_query)
for i in list(pattern_results):
    print(i)


# In[ ]:




