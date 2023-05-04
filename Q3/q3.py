import csv

f = open("202303_Seoul_Subway.csv")
data = csv.reader(f)

head = next(data)

s1=0
s2=0
s3=0
s4=0
s5=0
s6=0
s7=0
s8=0
s9=0

for row in data:
    
    row[4] = int(row[4])
    row[5] = int(row[5])
    passenger = row[4]+row[5]
    
    if(row[1] == "1호선"):
        s1 +=passenger
    if(row[1] == "2호선"):
        s2 +=passenger
    if(row[1] == "3호선"):
        s3 +=passenger
    if(row[1] == "4호선"):
        s4 +=passenger
    if(row[1] == "5호선"):
        s5 +=passenger
    if(row[1] == "6호선"):
        s6 +=passenger
    if(row[1] == "7호선"):
        s7 +=passenger
    if(row[1] == "8호선"):
        s8 +=passenger
    if(row[1] == "9호선"):
        s9 +=passenger
        

sub_dic = {s1:'1',s2:'2',s3:'3',s4:'4',s5:'5',s6:'6',s7:'7',s8:'8',s9:'9'}

k=sub_dic.keys()
k_list = list(k)
k_list.sort()

max_fir = sub_dic.get(k_list[8])
max_sec = sub_dic.get(k_list[7])
min_fir = sub_dic.get(k_list[0])
min_sec = sub_dic.get(k_list[1])

f.close()

if __name__ == '__main__':
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line {} ({})".format(max_fir,k_list[8]))
    print("2nd Busiest Line: Line {} ({})".format(max_sec,k_list[7]))
    print("1st Least used Line: Line {} ({})".format(min_fir,k_list[0]))
    print("2nd Least used Line: Line {} ({})".format(min_sec,k_list[1]))