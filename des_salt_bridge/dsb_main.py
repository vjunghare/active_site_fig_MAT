#!/usr/bin python

import os

cwd = os.getcwd()
cwd= cwd + '/'
#print cwd
f1= open(cwd + 'dsb_script.py',"w+")
f2= open(cwd + 'dsb_temp_script.py',"r")
ar=[]
data=[]
ar=f2.read()
f1.write('import cmd \nfrom pymol import stored\nfrom pymol import stored, CmdException')
f1.write('\nimport os \ncwd=os.getcwd()\ncwd= cwd + \'/\' \n')
f1.write("\n")
input_file ='detect_saltbridge_2'
f3= open(cwd + input_file,"r")
data=f3.read()
k=0
for i in data:
	if (i=='\n'):
		k=k+1
#print k	
f1.write('a_data=[\'')
#f1.write(data)
t=0;
for i in data:
	if (i=='\n'):
		t=t+1
		#f1.write('\'')
	if(t==k):
		break

	if (t>0):
		if (t>1 and i=='\n'):
			i='\',\''
		if (i=='\t'):
			i=' '
		if (i!= '\n'):
			f1.write(str(i))
	
	

f1.write('\']\n')
k=k-1
f1.write('\nnc=[0]\nnc[0]=')
f1.write(str(k))
f1.write('\n')
f1.write(ar)
f1.close()
f2.close()
f3.close()

#############
#File with glMOL output
#############

f4= open(cwd + 'dsb_script_gl.py',"w+")
f2= open(cwd + 'dsb_temp_script.py',"r")
ar1=[]
data1=[]
ar1=f2.read()
f4.write('import cmd \nfrom pymol import stored\nfrom pymol import stored, CmdException')
f4.write('\nimport os \nimport dsb_export_to_gl as glmol\ncwd=os.getcwd()\ncwd= cwd + \'/\' \n')
f4.write("\n")
input_file ='detect_saltbridge_2'
f3= open(cwd + input_file,"r")
data1=f3.read()
k1=0
for i in data1:
	if (i=='\n'):
		k1=k1+1
	
f4.write('a_data=[\'')

t1=0;
for i in data1:
	if (i=='\n'):
		t1=t1+1
		
	if(t1==k1):
		break

	if (t1>0):
		if (t1>1 and i=='\n'):
			i='\',\''
		if (i=='\t'):
			i=' '
		if (i!= '\n'):
			f4.write(str(i))

	
k1=k1-1
f4.write('\']\n')
f4.write('\nnc=[0]\nnc[0]=')
f4.write(str(k1))
f4.write('\n')
f4.write(ar1)
f4.write('\nglmol.dump_rep(modelName)\npymol.cmd.quit()')
f4.close()
f3.close()
f2.close()
