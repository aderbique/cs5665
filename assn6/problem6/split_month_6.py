import os, sys, csv, re

def run(fn):
	file = open(fn)
	if 'lazy' == 'lazy':
		for line in file:
			m = re.search('(\d\d\d\d\d\d)\d\d(.*)',line)
			#line = m.group(0) + m.group(1)
			#print(line)
			
			if m == None:
			  pass
			elif m.group(0) == '201401':
				append_file('201401.csv',line)
			elif m.group(0) == '201402':
				append_file('201402.csv',line)
			elif m.group(0) == '201403':
				append_file('201403.csv',line)
			elif m.group(0) == '201404':
				append_file('201404.csv',line)
			elif m.group(0) == '201405':
				append_file('201405.csv',line)
			elif m.group(0) == '201406':
				append_file('201406.csv',line)
			elif m.group(0) == '201407':
				append_file('201407.csv',line)
			elif m.group(0) == '201408':
				append_file('201408.csv',line)
			elif m.group(0) == '201409':
				append_file('201409.csv',line)
			elif m.group(0) == '201410':
				append_file('201410.csv',line)
			elif m.group(0) == '201411':
				append_file('201411.csv',line)
			elif m.group(0) == '201412':
				append_file('201412.csv',line)

			elif m.group(0) == '201501':
				append_file('201501.csv',line)
			elif m.group(0) == '201502':
				append_file('201502.csv',line)
			elif m.group(0) == '201503':
				append_file('201503.csv',line)
			elif m.group(0) == '201504':
				append_file('201504.csv',line)
			elif m.group(0) == '201505':
				append_file('201505.csv',line)
			elif m.group(0) == '201506':
				append_file('201506.csv',line)
			elif m.group(0) == '201507':
				append_file('201507.csv',line)
			elif m.group(0) == '201508':
				append_file('201508.csv',line)
			elif m.group(0) == '201509':
				append_file('201509.csv',line)
			elif m.group(0) == '201510':
				append_file('201510.csv',line)
			elif m.group(0) == '201511':
				append_file('201511.csv',line)
			elif m.group(0) == '201512':
				append_file('201512.csv',line)
				
			elif m.group(0) == '201601':
				append_file('201601.csv',line)
			elif m.group(0) == '201602':
				append_file('201602.csv',line)
			elif m.group(0) == '201603':
				append_file('201603.csv',line)
			elif m.group(0) == '201604':
				append_file('201604.csv',line)
			elif m.group(0) == '201605':
				append_file('201605.csv',line)
			elif m.group(0) == '201606':
				append_file('201606.csv',line)
			elif m.group(0) == '201607':
				append_file('201607.csv',line)
			elif m.group(0) == '201608':
				append_file('201608.csv',line)
			elif m.group(0) == '201609':
				append_file('201609.csv',line)
			elif m.group(0) == '201610':
				append_file('201610.csv',line)
			elif m.group(0) == '201611':
				append_file('201611.csv',line)
			elif m.group(0) == '201612':
				append_file('201612.csv',line)
			
			elif m.group(0) == '201701':
				append_file('201701.csv',line)
			elif m.group(0) == '201702':
				append_file('201702.csv',line)
			elif m.group(0) == '201703':
				append_file('201703.csv',line)
			elif m.group(0) == '201704':
				append_file('201704.csv',line)
			elif m.group(0) == '201705':
				append_file('201705.csv',line)
			elif m.group(0) == '201706':
				append_file('201706.csv',line)
			elif m.group(0) == '201707':
				append_file('201707.csv',line)
			elif m.group(0) == '201708':
				append_file('201708.csv',line)
			elif m.group(0) == '201709':
				append_file('201709.csv',line)
			elif m.group(0) == '201710':
				append_file('201710.csv',line)
			elif m.group(0) == '201711':
				append_file('201711.csv',line)
			elif m.group(0) == '201712':
				append_file('201712.csv',line)
				
			print m.group(0)


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