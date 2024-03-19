# The distribution of reported crimes based on Crime Code

# Required Libraries
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Connection to database
db=pymysql.connect (
    database = "crimedata",
    host="localhost",
    user="root",
    password="______"
)
cursor=db.cursor()

# Query for reported crimes based on Crime Code
cursor.execute("select Crm_Cd, count(*) as crime_count from crime_data group by Crm_Cd order by crime_count desc")
crime_code_df=pd.DataFrame(cursor.fetchall(), columns=['Crm_Cd', 'crime_count'])

# For Visualization
plt.figure(figsize=(10,4))
sb.barplot(x='Crm_Cd',y='crime_count', data=crime_code_df, label='Code wise')
plt.title('By Crime Code')
plt.xlabel('Crime Code')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45,ha='right')
plt.legend()
plt.show()

#Connection close

db.close()
