#!/usr/bin/python

f1= open('hbb_script.py',"w+")
f2= open('hbb_temp_script.py',"r")
f4= open( 'hbb_script_gl.py',"w+")
f4.write('#!/usr/bin python \nimport pymol\n')
f4.write('import cmd \nfrom pymol import stored\nfrom pymol import stored, CmdException')
 
 
f4.write('\nimport export_to_gl as glmol\ndef out_atoms(modelName):\n\tprint modelName\n')
 
ar=[]

data=[]
ar=f2.read()
f1.write('\nimport cmd \nfrom pymol import stored\nfrom pymol import cmd, CmdException')

f1.write('\nimport pymol \ninput_file=\'placed_h.pdb\'')

f1.write("\ncmd.load( input_file , \'placed_h.pdb\' )\n")

input_file ='HBonds_BB'
f3= open( input_file,"r")
data=f3.read()
k=0
for i in data:
	if (i=='\n'):
		k=k+1
#print k	
f1.write('a_data=[\'')
f4.write('\ta_data=[\'')
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
			f4.write(str(i))
	
	

f1.write('\']\n')
k=k-1
f1.write('\nnc=[0]\nnc[0]=')

f1.write(str(k))

f1.write('\n')

f1.write('def out_atoms():\n\tmodelName=\'placed_h\'\n')

f1.write(ar)

f1.write('out_atoms()')
f4.write('\']\n')
f4.write('\n\tnc=[0]\n\tnc[0]=')
f4.write(str(k))
f4.write('\n')
f4.write(ar)
sst = 'hbb_glmol_sst.png'
impf = 'hbb_glmol.html'
f4.write('\ndef t_run():')
f4.write("\n\tinput_file=\'placed_h.pdb\'\n\tmodelName=\'placed_h\'\n\tcmd.load( input_file , \'placed_h\')\n\tout_atoms(modelName)\n\tglmol.dump_rep(modelName, \'%s\', \'%s\')\n\tpymol.cmd.quit()\nt_run()\n"%(sst,impf))
f1.close()
f2.close()
f3.close()
f4.close()
