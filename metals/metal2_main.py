#!/usr/bin/python

f2= open('metal2_temp_script.py',"r")
file_1=open('metal_1', "r")
ar=[]
data=[]
ar=f2.read()
#print ar
##pdbfile name incorporation 
inf_t=[]
inp= open('inputfile.txt',"r")

with inp as ins:
 	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		inf_t=line
inf_t2=inf_t.rstrip('.pdb')
inp.close()
## Intereaction Data from 

input_file ='metal_2'
f3= open( input_file,"r")
tnol=0
with f3 as ins:
	ins = [line.rstrip('\n') for line in ins]
	ins = [line.replace("\t"," ") for line in ins]
	for line in ins:
		data.append(line)
		tnol=tnol+1
print data[2]
##reading ligands
data_metal=[]
nmetal=0
with file_1 as ins:
	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		line = line.rstrip(" ")
		data_metal.append(line)
		nmetal=nmetal+1
print data_metal
print nmetal
##

for i in range (0, (nmetal-1)):
	#print i, (nmetal-1)
	tmp_file=('metal_2_' + str(i) + '_script.py')
	tmp_file_gl=('metal_2_' + str(i) + '_gl.py')
	f1= open(tmp_file,"w+")
	f1_gl= open(tmp_file_gl,"w+")
	f1.write('import pymol \nfrom pymol import stored\nfrom pymol import cmd, CmdException')
	f1_gl.write('import pymol \nfrom pymol import stored\nfrom pymol import cmd, CmdException\nimport export_to_gl as glmol\n')
	f1.write('\ninput_file=\'')
	f1_gl.write('\ninput_file=\'inputfile.pdb\'')
	f1.write(inf_t)
	f1.write("\'\ncmd.load( input_file , \'%s\' )\nmodelName=\'%s\'\n"%(inf_t2, inf_t2))
	f1_gl.write("\ncmd.load( input_file , \'inputfile\' )\nmodelName=\'inputfile\'\n")
	f1.write('\nprint \"Ligand ')
	f1.write(str(i+1))
	f1_gl.write('\nprint \"Metal ')
	f1.write('- %s\"\nligand=[]\nmetals'%(data_metal[i+1]))
	f1_gl.write('- %s\"\nligand=[]\nmetals'%(data_metal[i+1]))
	f1.write('=\'%s\'\n'%(data_metal[i+1]))
	f1_gl.write('=\'%s\'\n'%(data_metal[i+1]))
	f1.write('metal_data=[')
	f1_gl.write('metal_data=[')
	k=0
	k2=0
	for j in data[1:]:
		a1=[]
		a1=j.split(" ")
		#print a1
		#print a[0]
		#a_t1=a1[0] +' ' + a1[1] + ' ' + a1[3]
		#print a_t1
		temp_data_metal=[]
		temp_data_metal= data_metal[i+1].split("\t")
		#print i, temp_data_metal
		if((a1[0] == temp_data_metal[0]) and (a1[1] == temp_data_metal[1]) and (a1[3] == temp_data_metal[2])):
			k=k+1
	for j1 in data[1:]:
		a12=[]
		a12=j1.split(" ")
		#print a1
		#print a[0]
		#a_t1=a1[0] +' ' + a1[1] + ' ' + a1[3]
		#print a_t1
		temp_data_metal1=[]
		temp_data_metal1= data_metal[i+1].split("\t")
		#print temp_data_metal
		if((a12[0] == temp_data_metal1[0]) and (a12[1] == temp_data_metal1[1]) and (a12[3] == temp_data_metal1[2])):
			f1.write('\'')
			f1_gl.write('\'')
			f1.write(str(j1))
			f1_gl.write(str(j1))
			f1.write('\'')
			f1_gl.write('\'')
			if (k2<k-1):
				f1.write(',')
				f1_gl.write(',')
		k2=k2+1
		#print k
	#print lig_atm		

	f1.write(']\n')
	f1_gl.write(']\n')
	f1_gl.write('\n')
	f1.write(ar)
	f1_gl.write(ar)
	f1.write('\nout_atoms(modelName)\n')
	f1_gl.write('\n')
	f3.close()
	f1.close()
	f1_gl.write('\ndef t_run():')
	temp_ssn= ('as3_ligand' + str(i) + '_ssn.png')
	temp_ifn= ('as3_ligand' + str(i) + '.html')
	f1_gl.write("\n\tinput_file=\'inputfile.pdb\'\n\tmodelName=\'inputfile\'\n\tcmd.load( input_file , \'inputfile\')\n\tout_atoms(modelName)\n\tglmol.dump_rep(modelName,\'%s\',\'%s\')\n\tpymol.cmd.quit()\nt_run()\n"%(temp_ssn,temp_ifn))
	f1_gl.close()
f2.close()
file_1.close()


