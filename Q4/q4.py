import csv

f = open("202303_Seoul_Subway.csv")
data = csv.reader(f)

head = next(data)

s1_max=0
s1_max_s=""
s1_min=9999999
s1_min_s=""

s2_max=0
s2_max_s=""
s2_min=9999999
s2_min_s=""

s3_max=0
s3_max_s=""
s3_min=9999999
s3_min_s=""

s4_max=0
s4_max_s=""
s4_min=9999999
s4_min_s=""

for row in data:
    
    row[4] = int(row[4])
    row[5] = int(row[5])
    passenger = row[4]+row[5]
    
    
    
    if (row[1]=="1호선"):
        if(s1_max<passenger):
            s1_max=passenger
            s1_max_s=row[3]
        if(s1_min>passenger):
            s1_min=passenger
            s1_min_s=row[3]
            
    if (row[1]=="2호선"):
        if(s2_max<passenger):
            s2_max=passenger
            s2_max_s=row[3]
        if(s2_min>passenger):
            s2_min=passenger
            s2_min_s=row[3]
            
    if (row[1]=="3호선"):
        if(s3_max<passenger):
            s3_max=passenger
            s3_max_s=row[3]
        if(s3_min>passenger):
            s3_min=passenger
            s3_min_s=row[3]
            
    if (row[1]=="4호선"):
        if(s4_max<passenger):
            s4_max=passenger
            s4_max_s=row[3]
        if(s4_min>passenger):
            s4_min=passenger
            s4_min_s=row[3]  
            
f.close()


if __name__ == '__main__':
    print("*** Subway Report for Seoul on March 2023 ***")
    print("Line 1:")
    print("Busiest Station: {} ({})".format(s1_max_s, s1_max))
    print("Least used Station: {} ({})".format(s1_min_s, s1_min))
    print("Line 2:")
    print("Busiest Station: {} ({})".format(s2_max_s, s2_max))
    print("Least used Station: {} ({})".format(s2_min_s, s2_min))
    print("Line 3:")
    print("Busiest Station: {} ({})".format(s3_max_s, s3_max))
    print("Least used Station: {} ({})".format(s3_min_s, s3_min))
    print("Line 4:")
    print("Busiest Station: {} ({})".format(s4_max_s, s4_max))
    print("Least used Station: {} ({})".format(s4_min_s, s4_min))
   