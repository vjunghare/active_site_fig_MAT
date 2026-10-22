#!/usr/bin/python
import cmd, pymol 
from pymol import stored
from pymol import stored, CmdException
import os 
import export_to_gl as glmol
 

input_file= 'inputfile.pdb'

cmd.load( input_file , 'inputfile' )
modelName='inputfile'
lig_data=['[Ligands]4','CIT 201 A','CIT 202 A','CIT 201 B','K 202 B']
metals=['K 202 B']


ldata=[]
m_ldata=[]
ldata=lig_data
m_ldata=metals
nol_m=len(m_ldata)
nol=(len(ldata))
def out_atoms():	
	nr=nol
	#print nr
	ligands = []
	metal_ligands = []
	k=0
	for i in ldata[1:nol]:
		#print i
		a= i.split(" ")
		residue = a[1]
		chains = a[2]
		ligands.append('((%s and resi %s and chain %s))'%(modelName, residue, chains))
	for i_m in m_ldata:
		b= i.split(" ")
		metal_ligands.append('((%s and resi %s and chain %s))'%(modelName, b[1], b[2]))
	#print ligands	
	#cmd.bg_color('white')    ##to color the backgroud white
	cmd.hide('lines', '%s'%modelName)
	cmd.show('cartoon', '%s'%modelName)
	cmd.util.cbc(selection='%s'%modelName,first_color=7,quiet=1,legacy=0,_self=cmd)
	cmd.hide('cartoon', 'HETATM and %s'%modelName)
	cmd.show('lines','HETATM and %s'%modelName)
	cmd.color('blue','HETATM and %s'%modelName)
	cmd.color('brown','HETATM and resn HOH and %s'%modelName)
	cmd.select('ligand', ' '.join('%s' % u1 for u1 in ligands))
	cmd.show('sticks', '(%s) and ligand'%(modelName))
	cmd.util.cbag(selection='ligand')
	cmd.select('metal_ligand', ' '.join('%s' % u1 for u1 in metal_ligands))
	cmd.set("sphere_scale", 0.4, 'metal_ligand')
	cmd.show('sphere','metal_ligand and %s'%modelName)
	cmd.orient(modelName)
	cmd.deselect()


def t_run():
	input_file='inputfile.pdb'
	modelName='inputfile'
	cmd.load( input_file , 'inputfile')
	out_atoms()
	glmol.dump_rep(modelName, 'as1_glmol_sst.png', 'as1_glmol.html')
	pymol.cmd.quit()
t_run()
