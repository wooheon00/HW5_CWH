import csv

f = open("q1.csv")
data = csv.reader(f)

head = next(data)

average_sum = 0
highest_sum = 0
lowest_sum = 0
count = 0 

for row in data:
    
    if row[2] == "" or row[3] == "" or row[4] == "":
        continue
        

    row[2] = float(row[2])
    row[3] = float(row[3])
    row[4] = float(row[4])
    
    average_sum += row[2]
    highest_sum += row[3]
    lowest_sum += row[4]
    
    count += 1

if __name__ == '__main__':
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:.2f} Celsius".format(average_sum/count))
    print("Average Minimum Temperature: {0:.2f} Celsius".format(highest_sum/count))
    print("Average Maximum Temperature: {0:.2f} Celsius".format(lowest_sum/count))

f.close()