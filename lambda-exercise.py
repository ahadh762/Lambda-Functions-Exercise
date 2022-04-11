import csv

file_name = '911_Calls_for_Service_(Last_30_Days).csv'
alpha_min = 10

with open(file_name) as f:
      reader = csv.reader(f, delimiter=",")
      lines = [line for line in reader]
      results = filter(lambda row: row[5] != "0" and row[20] != "", lines)


#create output file
with open('test_output_csv.csv', "w", newline='') as output_file:
    csv_writer = csv.writer(output_file, delimiter=',')
    csv_writer.writerows(results)


#grades_over_90 = filter(lambda x: x > 90, grades)

# with open(file_name) as f:
#     reader = csv.reader(f, delimiter=",")
#     lines = [line for line in reader]
#     for row_data in reader:
#         if any(x.strip() for x in row_data):
#             data_set.append(row_data)