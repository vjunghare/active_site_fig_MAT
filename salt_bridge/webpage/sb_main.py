#!/usr/bin/env python

import os

cwd = os.getcwd()
cwd= cwd + '/'
#print cwd
f1= open(cwd + 'sb_script_l.py',"w+")
f1w= open(cwd + 'sb_script_w.py',"w+")
f2= open(cwd + 'sb_temp_script.py',"r")
inf_t=[]
inp= open(cwd + 'inputfile.txt',"r")

with inp as ins:
 	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		inf_t=line
inf_t2=inf_t.rstrip('.pdb')
inp.close()
print inf_t, inf_t2

ar=[]

data=[]
ar=f2.read()
f1.write('#!/usr/bin/env python\nimport cmd \nfrom pymol import stored\nfrom pymol import cmd, CmdException')
f1w.write('from pymol import stored, cmd, CmdException')
f1.write('\nimport os, pymol \ncwd=os.getcwd()\ncwd= cwd + \'/\' \ninput_file=\'')
f1w.write('\nimport pymol\ninput_file=\'')
f1.write(inf_t)
f1w.write(inf_t)
f1.write("\'\ncmd.load( input_file , \'%s\' )\n"%(inf_t2))
f1w.write("\'\ncmd.load( input_file , \'%s\' )\n"%(inf_t2))

input_file ='detect_saltbridge_1'
f3= open(cwd + input_file,"r")
data=f3.read()
k=0
for i in data:
	if (i=='\n'):
		k=k+1
#print k	
f1.write('a_data=[\'')
f1w.write('a_data=[\'')
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
			f1w.write(str(i))
	
	

f1.write('\']\n')
f1w.write('\']\n')
k=k-1
f1.write('\nnc=[0]\nnc[0]=')
f1w.write('\nnc=[0]\nnc[0]=')

f1.write(str(k))
f1w.write(str(k))

f1.write('\n')
f1w.write('\n')

f1.write('def out_atoms():\n\tmodelName=\'%s\'\n'%(inf_t2))
f1w.write('def out_atoms():\n\tmodelName=\'%s\'\n'%(inf_t2))

f1.write(ar)
f1w.write(ar)

f1.write('out_atoms()')
f1w.write('out_atoms()')

f1.close()
f1w.close()
f2.close()
f3.close()

#############
#File with glMOL output
#############

f4= open(cwd + 'sb_script_gl.py',"w+")
f2= open(cwd + 'sb_temp_script.py',"r")
ar1=[]
data1=[]
ar1=f2.read()
f4.write('#!/usr/bin/env python \nimport __main__\nimport pymol\n')
f4.write('import cmd \nfrom pymol import stored\nfrom pymol import stored, CmdException')


f4.write('\nimport os \nimport sb_export_to_gl as glmol\ndef out_atoms(modelName):\n\tprint modelName\n\tcmd=pymol.cmd\n\tcwd=os.getcwd()\n\tcwd= cwd + \'/\' \n')

input_file ='detect_saltbridge_1'
f3= open(cwd + input_file,"r")
data1=f3.read()
k1=0

for i in data1:
	if (i=='\n'):
		k1=k1+1
	
f4.write('\n\ta_data=[\'')

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
f4.write('\n\tnc=[0]\n\tnc[0]=')
f4.write(str(k1))
f4.write('\n')
f4.write(ar1)
f4.write('\ndef t_run():')
f4.write("\n\t__main__.pymol_argv = [ \'pymol\' ]\n\tpymol.finish_launching()\n\tcmd=pymol.cmd\n\tinput_file=\'inputfile.pdb\'\n\tmodelName=\'inputfile\'\n\tcmd.load( input_file , \'inputfile\')\n\tout_atoms(modelName)\n\tglmol.dump_rep(modelName)\n\tpymol.cmd.quit()\n")
f4.close()
f3.close()
f2.close()
import sb_script_gl as t_script
t_script.t_run()
