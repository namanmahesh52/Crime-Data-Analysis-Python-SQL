# Difference in crime rates between male and female victims

#Required Libraries
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
cursor.execute("select Vict_sex ,count(*) from crime_data Group by Vict_sex")
gender_df=pd.DataFrame(cursor.fetchall(), columns=['Vict_sex', 'count'])

#For Visualization
plt.figure(figsize=(10,4))
sb.barplot(x='Vict_sex',y='count', data=gender_df, label='Genderwise')
plt.title('Difference in crime rates between male and female victims')
plt.xlabel('Victim Gender')
plt.ylabel('Count of Crimes')
plt.legend()
plt.show()

# Connection Close
db.close()
