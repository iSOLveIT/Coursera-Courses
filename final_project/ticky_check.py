#!/usr/bin/env python3

import sys
import re
import os
import operator
import csv


error = {}
per_user = {}

dir_path = os.path.abspath('.')
log_file_path = dir_path + '/' + sys.argv[1]

with open(log_file_path) as log_file:
    data = log_file.readlines()
    for datum in data:
        line = datum.strip()
        if "INFO" in line:
            pattern = r"ticky: INFO: ([\w ]*) (\[#[\d]+\]) (\([\w]+\))"
            result = re.search(pattern, line)
            if result is None:
                continue
            content = result.groups()
            username = content[2].strip('()')

            user_data = per_user.get(username, {"INFO": 0, "ERROR": 0})
            user_data['INFO'] = user_data.get('INFO', 0) + 1
            per_user[username] = user_data

        elif "ERROR" in line:
            pattern = r"ticky: ERROR: ([\w ]*) (\([\w]+\))"
            result = re.search(pattern, line)
            if result is None:
                continue
            content = result.groups()
            username = content[1].strip('()')
            error_key = content[0]
            error[error_key] = error.get(error_key, 0) + 1

            user_data = per_user.get(username, {"INFO": 0, "ERROR": 0})
            user_data['ERROR'] = user_data.get('ERROR', 0) + 1
            per_user[username] = user_data

        continue

sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
sorted_error.insert(0, ("Error", "Count"))
sorted_per_user = [(i[0], i[1].get("INFO"), i[1].get("ERROR")) for i in sorted(per_user.items())]
sorted_per_user.insert(0,  ("Username", "INFO", "ERROR"))


def write_csv(sorted_dictionary, csv_file_name):
    csv_file_path = dir_path + '/'+ csv_file_name
    with open(csv_file_path, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(sorted_dictionary)


write_csv(sorted_error, 'error_message.csv')
write_csv(sorted_per_user, 'user_statistics.csv')

