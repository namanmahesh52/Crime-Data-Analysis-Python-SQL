# Location Analysis

# Required Libraries
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#Connection to database
db=pymysql.connect (
    database = "crimedata",
    host="localhost",
    user="root",
    password="______"
)

cursor=db.cursor()

#Query for Location Anlaysis
cursor.execute("select Location , count(*) as crime_count from crime_data Group by Location order by crime_count desc limit 10")
location_df=pd.DataFrame(cursor.fetchall(), columns=['Location', 'crime_count'])

# For Visualization
plt.figure(figsize=(8,5))
sb.barplot(x='Location',y='crime_count', data=location_df, label='Top 10 Locations',color='g')
plt.title('Location Analysis')
plt.xlabel('Location')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()

db.close()