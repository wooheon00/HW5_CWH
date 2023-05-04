import csv

f = open("2022_Seoul_Temp.csv")
data = csv.reader(f)

head = next(data)

highest_diff = -10000
h_date = ""
lowest_diff = 10000
l_date = ""
for row in data:
    
    if row[2] == "" or row[3] == "" or row[4] == "":
        continue
    
    row[3] = float(row[3])
    row[4] = float(row[4])
    
    diff = (row[4]-row[3])
    
    if (highest_diff < diff):
        highest_diff = diff
        h_date = row[0]
        
    if (lowest_diff > diff):
        lowest_diff = diff
        l_date = row[0]

f.close()

if __name__ == '__main__':
    print("*** Annual Temperature Report for Seoul in 2022")
    print("Day with the Largest Temperature Variation: {}".format(h_date))
    print("Maximum Temperature Difference: {} Celsius".format(highest_diff))
    print("Day with the Smallest Temperature Variation: {}".format(l_date))
    print("Minimum Temperature Difference: {0:.1f} Celsius".format(lowest_diff))
    