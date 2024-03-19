# Victim Demographics
# Distribution of Victim Ages in crime

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

#Query for Agewise crime
cursor.execute("select Vict_Age from crime_data where Vict_Age is not null")
Vict_Age_df=pd.DataFrame(cursor.fetchall(), columns=['Vict_Age'])

# Foe Visualization
plt.figure(figsize=(9,5))
sb.histplot(Vict_Age_df['Vict_Age'],label='Agewise',kde=True)
plt.title('Distribution of Victim Ages in crime')
plt.xlabel('Victim Age')
plt.ylabel('Number of Crime')
plt.legend()
plt.show()

# Connection Close
db.close()
