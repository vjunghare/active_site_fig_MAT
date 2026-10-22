
import cmd 
from pymol import stored
from pymol import stored, CmdException
import pymol 
import export_to_gl as glmol
input_file='5Y1Z.pdb'
cmd.load( input_file , '5Y1Z' )

modelName='5Y1Z'
lig_data=['ZN	501	C','ZN	502	C','ZN	503	C','ZN	501	D','ZN	502	D','ZN	503	D']


ldata=[]
ldata=lig_data
nol=(len(ldata))
def out_atoms():	
	nr=nol
	#print nr
	ligands = []
	k=len(ldata)
	for i in ldata:
		#print i
		a= i.split("\t")
		residue = a[1]
		chains = a[2]
		ligands.append('((%s and resi %s and chain %s))'%(modelName, residue, chains))
	print ligands
	#cmd.bg_color('white')    ##to color the backgroud white
	cmd.hide('lines', '%s'%modelName)
	cmd.show('cartoon', '%s'%modelName)
	cmd.util.cbc(selection='%s'%modelName,first_color=7,quiet=1,legacy=0,_self=cmd)
	cmd.hide('cartoon', 'HETATM and %s'%modelName)
	cmd.show('lines','HETATM and %s'%modelName)
	cmd.color('blue','HETATM and %s'%modelName)
	cmd.color('brown','HETATM and resn HOH and %s'%modelName)
	cmd.select('metal_ligand', ' '.join('%s' % u1 for u1 in ligands))
	cmd.set("sphere_scale", 0.7, 'metal_ligand')
	cmd.show('spheres','metal_ligand and %s'%modelName)
	cmd.util.cbag(selection='metal_ligand')
	for t in ldata:
		b= t.split("\t")
		cmd.label('metal_ligand and name %s'%b[0],'resn')
	cmd.center('metal_ligand')
	cmd.deselect()


out_atoms()