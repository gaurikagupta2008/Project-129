import csv
data=[]
with open(r"C:\Users\gauri\OneDrive\Desktop\Python\Pro 127_2\web_scraping_1-main\sorted.py","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)
headers=data[0]
dwarf_data=data[1:]



with open("dataset_sorted.csv","a+") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerow(dwarf_data)
with open(r"C:\Users\gauri\OneDrive\Desktop\Python\Pro 127_2\web_scraping_1-main\sorted.py") as input,open("archive_dataset_sorted_1.csv","w",newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
            
