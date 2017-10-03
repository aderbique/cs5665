import sys
x = 10498
y = 1700225

fn = "file_" + str(x) + "_" + str(y) + ".txt"
out_file = open(fn,"w")

with open("filtered_access.txt") as in_file:
    for line_number, line in enumerate(in_file):
        if line_number < x:
            pass
        elif line_number > y:
            break
        else:
            out_file.write(line)

    out_file.close()
in_file.close()
