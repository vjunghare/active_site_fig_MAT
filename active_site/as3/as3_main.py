#!/usr/bin/python

f2= open('as3_temp_script.py',"r")
file_1=open('Active_site1', "r")
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

input_file ='Active_site3'
f3= open( input_file,"r")
tnol=0
with f3 as ins:
	ins = [line.rstrip('\n') for line in ins]
	ins = [line.replace("\t"," ") for line in ins]
	for line in ins:
		data.append(line)
		tnol=tnol+1
#print tnol
##reading ligands
data_lig=[]
nlig=0
with file_1 as ins:
	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		line = line.rstrip(' ')
		data_lig.append(line)
		nlig=nlig+1
print data_lig[4]
print nlig
##

for i in range (0, (nlig-1)):
	print i, (nlig-1)
	tmp_file=('as3_ligand' + str(i) + '_script.py')
	tmp_file_gl=('as3_ligand' + str(i) + '_gl.py')
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
	f1_gl.write('\nprint \"Ligand ')
	f1.write('- %s\"\nligands=[]\nligand_1'%(data_lig[i+1]))
	f1_gl.write('- %s\"\nligands=[]\nligand_1'%(data_lig[i+1]))
	f1.write('=\'%s\'\n'%(data_lig[i+1]))
	f1_gl.write('=\'%s\'\n'%(data_lig[i+1]))
	f1.write('lig_data=[')
	f1_gl.write('lig_data=[')
	k=0
	for j in data:
		a1=[]
		a1=j.split(" ")
		#print "check"
		#print a[0]
		a_t1=a1[0] + ' ' + a1[1] + ' ' + a1[3]
		#print a_t1, 
		temp_data_lig=data_lig[i+1]
		#print temp_data_lig
		if(a_t1 == temp_data_lig):
			k=k+1
			#print a_t1, data_lig[i+1]
	k2=0
	lig_atm = ''
	for j in data:
		a=[]
		a=j.split(" ")
		#print "check"
		#print a[2]
		a_t=a[0] + ' ' + a[1] + ' ' + a[3]
		#if (i==3):
			#print a_t
		lig_atm_count=0
		
		if(a_t==data_lig[i+1]):
			if (lig_atm_count<1):
				lig_atm=a[2]
			k2=k2+1
			f1.write('\'')
			f1_gl.write('\'')
			f1.write(str(j))
			f1_gl.write(str(j))
			f1.write('\'')
			f1_gl.write('\'')
			if (k2<k):
				f1.write(',')
				f1_gl.write(',')
		#print k
	#print lig_atm		

	f1.write(']\n')
	f1_gl.write(']\n')

	f_metal= open("metal_1","r")
	metal_data=[]
	n_metal_data=0
	with f_metal as ins:
		ins = [line.rstrip('\n') for line in ins]
		for line in ins:
			line = line.rstrip(' ')
			if(line != ''):
				metal_data.append(line)
			n_metal_data=n_metal_data+1
	
	print metal_data, n_metal_data
	f1.write("metal_data=[")
	f1_gl.write("metal_data=[")
	line_count=0
	if (len(metal_data) == 1):
		f1.write("]")
		f1_gl.write("]")
	else:
		for i1 in metal_data[1:]:
			f1.write("\'%s\'"%i1)
			f1_gl.write("\'%s\'"%i1)
			if(line_count < (n_metal_data-2)):
				f1.write(',')
				f1_gl.write(',')
			line_count=line_count+1
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


