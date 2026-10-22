#!/usr/bin/python

f2= open('as2_temp_script.py',"r")
file_1=open('Active_site1', "r")
ar=[]
data=[]
ar=f2.read()
temp= 'Ligand'
##pdbfile name incorporation 
inf_t=[]
inp= open('inputfile.txt',"r")

with inp as ins:
 	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		inf_t=line
inf_t2=inf_t.rstrip('.pdb')
inp.close()
##lig data seperation

input_file ='Active_site2'
f3= open( input_file,"r")
tnol=0
with f3 as ins:
	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		data.append(line)
		tnol=tnol+1
#print tnol
##reading ligands
data_lig=[]
with file_1 as ins:
	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		data_lig.append(line)
#print data_lig, data
nlig=0
temps= 'Ligand'
liglist=[]
tsl=0
lig_res=[]
nofl=0

#metal 
metal_data=[]
f_metal= open ('metal_1',"r")
metal_data_t=f_metal.readlines()
for i in metal_data_t:
	i=i.rstrip('\n')
	if (i!=''):
		metal_data.append(i)

#print data
for i in data:
	nofl=nofl+1
	if (i[:-1]==temps):
		#print i
		nlig+=1
		liglist.append(i)
		if(nofl==1):
			tsl=nofl
		if(nofl!=1 ):
			ts=nofl-tsl
			lig_res.append(ts-1)
		if(nofl>1):
			tsl=nofl
	if(nofl==tnol):
		ts=nofl-tsl
		#print ts, nofl, tsl
		lig_res.append(ts)

#print liglist
#print lig_res
#print nlig
##
data_s=1
data_e=0
for i in range (0, nlig):
	tmp_file=('as2_ligand' + str(i) + '_script.py')
	tmp_file_gl=('as2_ligand' + str(i) + '_gl.py')
	f1= open(tmp_file,"w+")
	f1_gl= open(tmp_file_gl,"w+")
	f1.write('import pymol \nfrom pymol import stored\nfrom pymol import cmd, CmdException\ninput_file=\'')
	f1_gl.write('import pymol\nimport export_to_gl as glmol \nfrom pymol import stored\nfrom pymol import cmd, CmdException\nmodelName=\'inputfile\'\n')

	f1.write(inf_t)
	f1.write("\'\ncmd.load( input_file , \'%s\' )\nmodelName=\'%s\'\n"%(inf_t2, inf_t2))
	
	f1.write('\nprint \"Ligand ')
	f1_gl.write('\nprint \"Ligand ')
	f1.write(str(i))
	f1_gl.write(str(i))
	f1.write('- %s\"\nligands=[]\nligand_1'%(data_lig[i+1]))
	f1_gl.write('- %s\"\nligands=[]\nligand_1'%(data_lig[i+1]))
	f1.write('=\'%s\'\n'%(data_lig[i+1]))
	f1_gl.write('=\'%s\'\n'%(data_lig[i+1]))

	#metal data write
	f1.write('metals=[')
	f1_gl.write('metals=[')
	#f1.write(data)
	t_m=0;
	k_m=len(metal_data)-1
	#print metal_data
	for i_m in metal_data[1:]:
		f1.write('\'')
		f1_gl.write('\'')
		i_m=i_m.rstrip('\n')
		if (i_m!=''):
			f1.write(str(i_m))
			f1_gl.write(str(i_m))
			if (t_m<k_m-1):
				f1.write('\',')
				f1_gl.write('\',')
			t_m=t_m+1
	f1.write('\']\n')
	f1_gl.write('\']\n')

	## lig data
	f1.write('lig_data=[')
	
	f1_gl.write('lig_data=[')
	#k=0
	t=0
	#k=len(data)
	data_no=[]
	data2=[]
	data2=data
	data_e = data_e + lig_res[i]
	if (i > 0):
		data_s=data_s+lig_res[(i-1)]+1
	#print i, data_s, data_e
	for j in data2[data_s:data_e+1]:
		#print data2[data_s]
		#k=(data_e+1-data_s)
		f1.write('\'')
		f1_gl.write('\'')
		f1.write(str(j))
		f1_gl.write(str(j))
		f1.write('\'')
		f1_gl.write('\'')
		#print k
		if (t<(lig_res[i]-1)):
			f1.write(',')
			f1_gl.write(',')
		t=t+1
	data_e=data_e+1
	if (lig_res[i]==0):
		data_e=data_e+1		

	f1.write(']\n')
	f1_gl.write(']\n')

	f1.write('\n')
	f1_gl.write('\n')
	f1.write(ar)
	f1_gl.write(ar)
	f1.write('\nout_atoms()\n')
	f1_gl.write('\ndef t_run():')
	temp_ssn= ('as2_ligand' + str(i) + '_ssn.png')
	temp_ifn= ('as2_ligand' + str(i) + '.html')
	f1_gl.write("\n\tinput_file=\'inputfile.pdb\'\n\tmodelName=\'inputfile\'\n\tcmd.load( input_file , \'inputfile\')\n\tout_atoms()\n\tglmol.dump_rep(modelName,\'%s\',\'%s\')\n\tpymol.cmd.quit()\nt_run()\n"%(temp_ssn,temp_ifn))
	
	f3.close()
	f1.close()
f2.close()
file_1.close()
f1_gl.close()

##########
##GLMOL

