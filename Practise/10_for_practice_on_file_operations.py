"""
Get data from log_report_1.json file

then

write json file data to log_report_5.txt

Expected content in log_report_5.txt:
----------
    IP                  DATE            URL
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
----------
"""

print("Get data from log_report_1.json file")
print("-"*20)
# -------------

my_json_file_handle = open("log_report_1.json", "r")

import json
json_file_content = json.load(my_json_file_handle)

my_json_file_handle.close()

print("json_file_content:", json_file_content, end="\n\n")
print("type of json_file_content:", type(json_file_content), end="\n\n")

print("#"*40, end="\n\n")
############################