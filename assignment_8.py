# Working with files in python
file_name = "data.txt"
# wb = open(file_name, "w+")
# wb.write("Hallo Python\n")
# wb.write("Hallo World\n")
# wb.write("Hallo People\n")
# wb.write("Hallo Friends\n")
# wb.seek(0)
# print(wb.read())
# wb.close()
# 1. Write a Python script to create a file named data.txt and write "Hello, Python!" into
# it.
with open(file_name,"w") as file:
    file.write("Hello World !!")
# 2. Read and display the contents of data.txt.
with open(file_name, "r") as file:
    content = file.read()
    print(f"Contents of data.txt is {content}")
# 3. Modify the script to append "Welcome to file handling." to data.txt.
with open(file_name,"a") as file:
    file.write("\nHallo People")

#Display updated Contents
with open(file_name,"r") as file:
    updated_content = file.read()
    print(f"Contents of data.txt is {content} \nUpdated Content of data.txt is {updated_content}")
# 4.Write a function that counts the number of lines in a text file.
def count_lines(file_name):
    with open(file_name, "r") as file:
        line_count = sum(1 for line in file)
        return line_count

file_name = "data.txt"
print(f"The number of lines in '{file_name}' : {count_lines(file_name)}")

# 5. Write a script that reads a file and prints only lines that contain the word "Python".



#-------------Advanced Practice Questions _____________________

# 1. Write a program to read a large file line by line and count the occurrences of each
# word.
# 2. Create a script that removes all blank lines from a file.
# 3. Write a program that reads a CSV file and converts it into a JSON file.
# 4. Implement a log system where errors are appended to an error log file with
# timestamps.
# 5. Write a Python program to merge multiple text files into a single file.
