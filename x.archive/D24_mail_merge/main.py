# extract data from csv file weather_data.csv and take the number at index 1 convert it to int and put it into a list called temperatures
import csv

temperatures = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
print(temperatures)
