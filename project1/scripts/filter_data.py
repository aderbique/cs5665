import sys, re

fn = "filted_data.txt"
out_file = open(fn,"w")

regex = "weathershare.org/"

with open("access.log") as in_file:
    for line in in_file:
        m = re.search(regex, line)
        if m:
            pass
        else:
            out_file.write(line)
    out_file.close()
in_file.close()
