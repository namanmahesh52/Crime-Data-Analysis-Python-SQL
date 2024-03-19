select Lat, Lon from crime_data where Lat is not null and Lon is not null 

select Vict_Age,count(*) from crime_data where Vict_Age is not null
group by Vict_Age

select Vict_sex ,count(*) from crime_data Group by Vict_sex

select Location , count(*) as crime_count from crime_data Group by Location order by crime_count desc limit 10

select Crm_Cd, count(*) as crime_count from crime_data group by Crm_Cd order by crime_count desc

select Date_Rptd, DATE_OCC from crime_data
where Date_Rptd > DATE_OCC

select * from netflix11.netflix
