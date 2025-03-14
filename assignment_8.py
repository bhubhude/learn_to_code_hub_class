# Write a Python script to create a file named data.txt and write "Hello, Python!" into  it.

with open("file.txt", "w") as file:
    file.write("Hello, Python")
# 2. Read and display the contents of data.txt.
with open("file.txt","r") as file:
    content = file.read()
    print(f"Contents of the file.txt are: {content}")
# # 3. Modify the script to append "Welcome to file handling." to data.txt.
with open("file.txt","a") as file:
    file.write("\nWelcome to file handling")

#      Display updated contents
with open("file.txt","r") as file:
    updated_contents = file.read()
    print(f"Updated contents are: {updated_contents}")

# 4. Write a function that counts the number of lines in a text file.
def count_number_of_lines(file_name):
    with open(file_name,"r") as file:
        line_count = sum(1 for line in file)
    return line_count


file_name = "file.txt"
print(f"The number of lines in a text file {count_number_of_lines(file_name)}")

# 5. Write a script that reads a file and prints only lines that contain the word "Python".
def print_line_with_python(file_name):
    with open(file_name,"r") as file:
        for line in file:
            if "Python" in line:
                print(line.strip())


print_line_with_python("file.txt")

# ----------------------------Advanced Practice Questions-------------

# 1. Write a program to read a large file line by line and count the occurrences of each word.
from  collections import Counter
def word_count_occurrences(file_name):
    with open(file_name, "r") as file:
        text = file.read()
        words = text.split()
        word_count = Counter(words)
    return word_count

words_counts = word_count_occurrences("file.txt")
print(words_counts)

# 2. Create a script that removes all blank lines from a file.
def removes_all_blank_lines(input_file, output_file):
    with open(input_file,"r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            if line.strip():
                outfile.write(line)


removes_all_blank_lines("file.txt", "blank_data.txt")

# Display blank_data
with open("blank_data.txt", "r") as file:
    blank_data = file.read()
    print(blank_data)

# 3. Write a program that reads a CSV file and converts it into a JSON file.

import json
import csv



file_csv = [
    ["Name","Surname","Age","Gender",],
    ['Admire','Ncube',39,"Male"],
    ['Shamina','Ndlovu',30,'Female'],
    ['Lawrence','Ndlovu',29,'Male'],
    ['Tebogo','Dube',27,'Female'],
    ['Innocentia','Nkomo',15,'Female']
]
csv_data = "file.csv"
with open(csv_data,"w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(file_csv)

print(f"Csv file {csv_data} has been created successful")
try:
    with open("file.csv", "r") as file:
        read_csv = csv.reader(file)
        for row in read_csv:
            print(row)
#
#     # Convert csv to json file
    with open("file.csv",'r') as csv_fil:
        csv_reader = csv.DictReader(csv_fil)
        data = list(csv_reader)

    with open("file.json", "w") as json_file:
        json.dump(data,json_file)

except FileNotFoundError:
    print("CSV file was not found")
except csv.Error as e:
    print(f"An error occurred while was reading CSV file {e}")
except json.JSONDecodeError as e:
    print(f"An error occurred while  reading json file {e}")

with open("file.json", "r") as file_j:
    data1 = json.load(file_j)
    for obj in data1:
        print(obj)



# 4. Implement a log system where errors are appended to an error log file with timestamps.
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('error.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def divide(x,y):
    try:
        results = x / y
        return results
    except ZeroDivisionError as e:
        print(f"You cannot divide number by zero: {e}")
        logger.error(str(e))
        return  None
    except Exception as e:
        logger.error(str(e))
        return None


result = divide(10, 0)
if result is not None:
    print(f"Result equal to {result:.2f}")
else:
    print("An error occurred")



# 5. Write a Python program to merge multiple text files into a single file.
def merge_multiple_text_files(output_file, *input_files):
    try:
        with open(output_file, "w") as outfile:
            for file_name in input_files:
                with open(file_name, "r") as infile:
                    outfile.write(infile.read() + "\n")
        return f"File has successfully merged {output_file}"
    except Exception as e:
        return f"Error {str(e)}"


result = merge_multiple_text_files("file2.txt","data_2.txt","data.txt","blank_data.txt")
print(result)
with open("file2.txt", "r") as file:
    contents = file.read()
    print(contents)




