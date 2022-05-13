import mysql.connector
import pandas as pd
import numpy as np
from log_util import Logger
logger = Logger().logger
# by syh

# pipeline:
# create a table named "papers", and store all information in date_title_author.

data = pd.read_csv('date_title_author.csv',usecols=[0,1,2,3,4])
arr = np.array(data)
arr_list = arr.tolist()

conn = mysql.connector.connect(host='localhost',user='scraping_sample', passwd='Sc_Python_Web43', database='scraping_sample')
cursor = conn.cursor()
# Create table
cursor.execute('create table if not exists papers (ID varchar(255), Date varchar(255),Title varchar(255),Author1 varchar(255),Author2 varchar(255))')
# Insert data
try:
    #Problem encountered: got error when data contains ' (single quote).
    #Solution at https://stackoverflow.com/questions/1912095/how-to-insert-a-value-that-contains-an-apostrophe-single-quote
    for row in arr_list:
        cursor.execute("insert into papers (ID, Date, Title, Author1, Author2) values ('{0[0]}','{0[1]}','{0[2]}','{0[3]}','{0[4]}')".format(row))
    print('Stored to mysql.')
    
except (KeyError, IndexError, TypeError) as err:
    logger.error("There was an error during articles insertion. The error: {}".format(err))

conn.commit()
cursor.close()
conn.close()







#for row in arr_list:
    #print ('{},{},{},{},{}'.format(row[0],row[1],row[2],row[3],row[4]))