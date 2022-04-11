import csv
from functools import reduce

file_name = '911_Calls_for_Service_(Last_30_Days).csv'

with open(file_name) as f:
      reader = csv.reader(f, delimiter=",")
      lines = [line for line in reader]

# Remove bad data from Zipcodes and Neighborhoods
cleaned_file = list(filter(lambda row: row[5] != "0" and row[20] != "", lines))

# Remove bad data from total_response_time
cleaned_file = list(filter(lambda row: row[17] != "" and row[17] != " " and row[5] != "0" and row[20] != "", lines))

total_response_list = []

for i in range(1,len(cleaned_file)):
    total_response_list.append(float(cleaned_file[i][17]))

total_response = reduce(lambda time1, time2: time1 + time2, total_response_list)
average_total_response = total_response/len(total_response_list)
print(average_total_response)

# Remove bad data from dispatch_time
cleaned_file = list(filter(lambda row: row[15] != "" and row[15] != " " and row[5] != "0" and row[20] != "", lines))

dispatch_time_list = []

for i in range(1,len(cleaned_file)):
    dispatch_time_list.append(float(cleaned_file[i][15]))

dispatch_times = reduce(lambda time1, time2: time1 + time2, dispatch_time_list)
average_dispatch_time = dispatch_times/len(dispatch_time_list)
print(average_dispatch_time)


# Remove bad data from total_time
cleaned_file = list(filter(lambda row: row[19] != "" and row[19] != " " and row[5] != "0" and row[20] != "", lines))

total_time_list = []

for i in range(1,len(cleaned_file)):
    total_time_list.append(float(cleaned_file[i][19]))

total_times = reduce(lambda time1, time2: time1 + time2, total_time_list)
average_total_time = total_times/len(total_time_list)
print(average_total_time)