
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

