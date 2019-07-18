import sys
input_file=sys.argv[1]
output_file=sys.argv[2]
output=open(output_file)
with open(input_file) as file:
    for line in file:
        fields=line.split('\t')
        if(fields[0]!=""):
            output.write(line)
output.close()


        