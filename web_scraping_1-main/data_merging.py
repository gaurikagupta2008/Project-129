import csv
import pandas
stars=[]
dwarfs=[]
with open(r"C:\Users\gauri\OneDrive\Desktop\Python\Pro 127_2\bright_stars.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        stars.append(row)
with open(r"C:\Users\gauri\OneDrive\Desktop\Python\Pro 127_2\dwarfs.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        dwarfs.append(row)
h1=stars[0]
h2=dwarfs[0]
p_d1=stars[1:]
p_d2=stars[1:]
h=h1+h2
data_array=[]
for i in p_d1:
    data_array.append(i)
for i2 in p_d2:
    data_array.append(i2)
with open("merged_data_129.csv","w") as f:
    writer=csv.writer(f)
    writer.writerow(h)
    writer.writerow(data_array)