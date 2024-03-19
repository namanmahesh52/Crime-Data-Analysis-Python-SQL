# Spatial Analysis
# Geographical hotspots for reported crimes

#Required Libraries
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

#Query for Spartial Analysis

cursor.execute("select Lat, Lon from crime_data where Lat is not null and Lon is not null")
spl_data=pd.DataFrame(cursor.fetchall(),columns=['Lat', 'Lon'])

#For Visualization
plt.figure(figsize=(9,5))
sb.scatterplot(x='Lat', y='Lon',data=spl_data, label='Crime Hotspots',color='purple')
plt.title('Geographical Hotspots for Reported Crimes')
plt.grid()
plt.legend()
plt.show()

#Closeing connection
db.close()
