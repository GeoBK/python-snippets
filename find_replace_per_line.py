import sys
input_file=sys.argv[0]
output_file=sys.argv[1]
find=sys.argv[2]
replace=sys.argv[3]
output=open(output_file,"w+")
with open(input_file) as file_object:
    for line in file_object:
        replaced_line=line.replace(find,replace)
        output.write(replaced_line)
output.close()


