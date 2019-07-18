import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
find=sys.argv[3]
output=open(output_file,"w+")
with open(input_file) as file_object:
    for line in file_object:
        if line.find(find) == -1:
            output.write(line)
output.close()


