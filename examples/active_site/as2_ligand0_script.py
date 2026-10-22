import pymol 
from pymol import stored
from pymol import cmd, CmdException
input_file='4oe9.pdb'
cmd.load( input_file , '4oe9' )
modelName='4oe9'

print "Ligand 0- CIT 201 A"
ligands=[]
ligand_1='CIT 201 A'
metals=['K 202 B']
lig_data=['CIT 201 A','SER 39 A','ARG 73 A','ALA 40 A','HIS 69 A']


ldata=[]
ldata=lig_data
nol=(len(ldata))
nom=len(metals)
def out_atoms():
	if (len(lig_data)==0):
		metal_ck=0
		print "No interacting residues"
		cmd.hide('lines', '%s'%modelName)
		cmd.show('cartoon', '%s'%modelName)
		cmd.color('auto','%s'%modelName)
		cmd.hide('cartoon', 'HETATM and %s'%modelName)
		cmd.show('lines','HETATM and %s'%modelName)
		cmd.color('blue','HETATM and %s'%modelName)
		cmd.color('brown','HETATM and resn HOH and %s'%modelName)
		ligand=ligand_1.split(" ")
		for j in metals:
			j=j.split(" ")
			if ((ligand[0]==j[0])and (ligand[1]==j[1]) and (ligand[2]==j[2])):
				metal_ck=1
		cmd.select('ligands','(%s and resn %s and resi %s and chain %s)'%(modelName,ligand[0], ligand[1], ligand[2]))
		if(metal_ck == 0):
			cmd.show('sticks', '(%s) and ligands'%(modelName))
			cmd.color('red', 'ligands and %s'%modelName)
		else:
			cmd.set("sphere_scale", 0.3, "ligands")
			cmd.show('spheres', '(%s) and ligands'%(modelName))
			cmd.color('red', 'ligands and %s'%modelName)
			cmd.label('ligands and name %s'%ligand[0],'resn + resi')
		cmd.orient('ligands')
		cmd.deselect()
	else:
		nr=nol
		sidechain = []
		sidechain1 = []
		metal_check=0
		temps='Ligand'
		k=0
		for i in ldata:		
			if (i[:-1]==temps):
				k=k+1
			if(i[:-1]!= temps):
				a=i.split(" ")
				#print a
				residue = a[0]
				resin = a[1]
				#print resin
				chains = a[2]
				sidechain1.append('((%s and resn %s and resi %s and chain %s))'%(modelName, residue, resin, chains))
		#print sidechain1
		ligand=ligand_1.split(" ")
		for j in metals:
			j=j.split(" ")
			if ((ligand[0]==j[0])and (ligand[1]==j[1]) and (ligand[2]==j[2])):
				metal_check=1
		#cmd.bg_color('white')
		cmd.hide('lines', '%s'%modelName)
		cmd.show('cartoon', '%s'%modelName)
		cmd.color('auto','%s'%modelName)
		cmd.hide('cartoon', 'HETATM and %s'%modelName)
		cmd.show('lines','HETATM and %s'%modelName)
		cmd.color('blue','HETATM and %s'%modelName)
		cmd.color('brown','HETATM and resn HOH and %s'%modelName)
	
		cmd.select('ligands','(%s and resn %s and resi %s and chain %s)'%(modelName,ligand[0], ligand[1], ligand[2]))
		if(metal_check == 0):
			cmd.show('sticks', '(%s) and ligands'%(modelName))
			cmd.color('red', 'ligands and %s'%modelName)
			
		else:
			cmd.set("sphere_scale", 0.3, "ligands")
			cmd.show('spheres', '(%s) and ligands'%(modelName))
			cmd.color('red', 'ligands and %s'%modelName)
			cmd.label('ligands and name %s'%ligand[0],'resn + resi')

		cmd.select('ligand_int', ' '.join('%s' % u1 for u1 in sidechain1))

		cmd.show('sticks', '(%s) and ligand_int'%(modelName))
		cmd.spectrum("count", 'rainbow', 'ligand_int')
	
		cmd.label('ligand_int and name CA','resn + resi')
		cmd.orient('ligand_int')	
		cmd.deselect()
		#cmd.delete('ligand')


		cmd.deselect()

out_atoms()
