#!/usr/bin/python
#print cwd

f1= open('metal1_script.py',"w+")
f2=open('metal1_temp_script.py',"r")
inf_t=[]
inp= open('inputfile.txt',"r")

with inp as ins:
 	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		inf_t=line
inf_t2=inf_t.rstrip('.pdb')
inp.close()
ar=[]
data=[]
ar=f2.read()
f1.write('\nimport cmd \nfrom pymol import stored\nfrom pymol import stored, CmdException')
f1.write('\nimport pymol \nimport export_to_gl as glmol\ninput_file=\'')
f1.write(inf_t)
f1.write("\'\ncmd.load( input_file , \'%s\' )\n"%(inf_t2))
f1.write('\nmodelName=\'%s\'\n'%(inf_t2))
input_file ='metal_1'
f3= open( input_file,"r")
data=f3.readlines()
k=0
#print data[1]
k=len(data)
#print k	
f1.write('lig_data=[')
#f1.write(data)
t=0;

for i in data[1:]:
	f1.write('\'')
	i=i.rstrip('\n')
	#i=i.rstrip('\t')
	f1.write(str(i))
	if (t<k-2):
		f1.write('\',')
	t=t+1
f1.write('\']\n')

f1.write('\n')
f1.write(ar)
f1.write("\nout_atoms()")
f1.close()
f2.close()
f3.close()

#############
#File with glMOL output
#############

f4= open( 'metal1_gl.py',"w+")
f2= open('metal1_temp_script.py',"r")
ar1=[]
data1=[]
ar1=f2.read()
f4.write('#!/usr/bin/python\nimport cmd \nfrom pymol import stored\nfrom pymol import stored, CmdException')
f4.write('\nimport os \nimport export_to_gl as glmol\ncwd=os.getcwd()\ncwd= cwd + \'/\' \n')
f4.write("\ninput_file= 'inputfile.pdb'\n")
f4.write("\ncmd.load( input_file , 'inputfile' )\nmodelName='inputfile'\n")
input_file ='metal_1'
f3= open( input_file,"r")
data1=f3.readlines()
k1=0
for i in data1:
	if (i=='\n'):
		k1=k1+1
	
f4.write('lig_data=[')
t1=0
kl=len(data1)
for i1 in data1[1:]:
	f4.write('\'')
	i1=i1.rstrip('\n')
	f4.write(str(i1))
	if (t1<kl-2):
		f4.write('\',')
	t1=t1+1
f4.write('\']\n')

f4.write('\n')
f4.write(ar1)
sst = 'metal1_glmol_sst.png'
impf = 'metal1_glmol.html'
f4.write('\ndef t_run():')
f4.write("\n\tinput_file=\'inputfile.pdb\'\n\tmodelName=\'inputfile\'\n\tcmd.load( input_file , \'inputfile\')\n\tout_atoms()\n\tglmol.dump_rep(modelName, \'%s\', \'%s\')\n\tpymol.cmd.quit()\nt_run()\n"%(sst,impf))
f4.close()
f3.close()
f2.close()
