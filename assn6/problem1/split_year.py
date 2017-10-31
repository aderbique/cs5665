import os, sys, csv, re

def run(fn):
	file = open(fn)
	if 'lazy' == 'lazy':
		for line in file:
			m = re.search('(\d\d\d\d).*',line)
			line = m.group(0) + m.group(1)
			print(line)
			if m.group(0) == '2014':
				append_file('2014.csv',line)
			elif m.group(0) == '2014':
				append_file('2015.csv',line)
			elif m.group(0) == '2015':
				append_file('2015.csv',line)
			elif m.group(0) == '2016':
				append_file('2016.csv',line)
			elif m.group(0) == '2016':
				append_file('2017.csv',line)
			elif m.group(0) == '2017':
				append_file('2017.csv',line)
			elif m.group(0) == '201607':
				append_file('201607.csv',line)			


def append_file(fn,line):
        append_write = ''
        if os.path.exists(fn):
            append_write = 'a' # append if already exists
            print('append')
        else:
            append_write = 'w'
            print('write')

        with open(fn, append_write) as myfile:
            myfile.write(line)
        myfile.close()


run('OSS-Sessions-By-Day20111101-20171013.csv')