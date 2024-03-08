#Lets sort some names from a file and then write 
#it to another

"""This program reads the names from a file, sorts
them and writes them back to another file"""

input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")

get_names = []

with open(input_file) as f:
    data = f.readlines()
    for line in data:
        get_names.append(line.strip())
print(get_names)

get_temp = sorted(get_names)

with open(output_file,'w') as f:
    for line in get_temp:
        f.write(line + '\n')

print("Sorted names have been written to file")