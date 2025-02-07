"""
From given string,
Extract
PICS

Expected Output:
----------
wpaper.gif
----------
"""
print("input Data:")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
start_index = input_data.find("[")
End_index = input_data.find(":")
print(input_data[start_index,End_index])

print("#"*40, end="\n\n")
############################