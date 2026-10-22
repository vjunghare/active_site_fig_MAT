#!/usr/bin/python
#print cwd

f1= open('as1_script.py',"w+")
f2=open('as1_temp_script.py',"r")
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
input_file ='Active_site1'
f3= open( input_file,"r")
data=f3.readlines()
k=0
#print data[1]

#print k	
f1.write('lig_data=[')
#f1.write(data)
t=0;
k=len(data)
for i in data:
	f1.write('\'')
	i=i.rstrip('\n')
	f1.write(str(i))
	if (t<k-1):
		f1.write('\',')
	t=t+1
f1.write('\']\n')
metal_data=[]
f_metal= open ('metal_1',"r")
metal_data_t=f_metal.readlines()
for i in metal_data_t:
	i=i.rstrip('\n')
	if (i!=''):
		metal_data.append(i)
f1.write('metals=[')
#f1.write(data)
t_m=0;
k_m=len(metal_data)-1
print metal_data
for i in metal_data[1:]:
	f1.write('\'')
	i=i.rstrip('\n')
	if (i!=''):
		f1.write(str(i))
		if (t_m<k_m-1):
			f1.write('\',')
		t_m=t_m+1
f1.write('\']\n')


f1.write('\n')
f1.write(ar)
f1.write("\nout_atoms()")
f1.close()
f2.close()
f3.close()
f_metal.close()

#############
#File with glMOL output
#############

f4= open( 'as1_script_gl.py',"w+")
f2= open('as1_temp_script.py',"r")
ar1=[]
data1=[]
ar1=f2.read()
f4.write('#!/usr/bin/python\nimport cmd, pymol \nfrom pymol import stored\nfrom pymol import stored, CmdException')
f4.write('\nimport os \nimport export_to_gl as glmol\n \n')
f4.write("\ninput_file= 'inputfile.pdb'\n")
f4.write("\ncmd.load( input_file , 'inputfile' )\nmodelName='inputfile'\n")
input_file ='Active_site1'
f3= open( input_file,"r")
data1=f3.read()
k1=0
for i in data1:
	if (i=='\n'):
		k1=k1+1
	
f4.write('lig_data=[')
t=0
k=len(data)
for i in data:
	f4.write('\'')
	i=i.rstrip('\n')
	f4.write(str(i))
	if (t<k-1):
		f4.write('\',')
	t=t+1
f4.write('\']\n')

metal_data2=[]
f_metal2= open ('metal_1',"r")
metal_data_t2=f_metal2.readlines()
for i2 in metal_data_t2:
	i2=i2.rstrip('\n')
	if (i2!=''):
		metal_data2.append(i2)
f4.write('metals=[')
#f1.write(data)
t_m=0;
k_m=len(metal_data2)-1
for i in metal_data2[1:]:
	f4.write('\'')
	i=i.rstrip('\n')
	f4.write(str(i))
	if (t_m<k_m-1):
		f4.write('\',')
	t_m=t_m+1
f4.write('\']\n')


#f4.write(str(k1))
f4.write('\n')
f4.write(ar1)
sst = 'as1_glmol_sst.png'
impf = 'as1_glmol.html'
f4.write('\ndef t_run():')
f4.write("\n\tinput_file=\'inputfile.pdb\'\n\tmodelName=\'inputfile\'\n\tcmd.load( input_file , \'inputfile\')\n\tout_atoms()\n\tglmol.dump_rep(modelName, \'%s\', \'%s\')\n\tpymol.cmd.quit()\nt_run()\n"%(sst,impf))
f4.close()
f3.close()
f_metal2.close()
f2.close()
