"""
From given string,
Extract
IP

Expected Output:
----------
123.123.123.123
----------
"""
print("input Data:")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
############################

print("type of input Data:")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#"*40, end="\n\n")
############################

print("Extract IP: 1-WAY: PARTIAL")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
############################

print("Extract IP: 2-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
index_of_1st_space = input_data.find(" ")
ip = input_data[0:index_of_1st_space]
print(ip)

print("#"*40, end="\n\n")
############################

print("Extract IP: 3-WAY")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split() # Default -> split by space
print("Splited Values:", sp, end="\n\n")

ip = sp[0]
print("IP:", ip)

print("#"*40, end="\n\n")
############################