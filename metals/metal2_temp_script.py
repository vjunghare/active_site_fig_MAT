
ldata=[]
ldata=metal_data
nol=(len(ldata))
def out_atoms(modelName):

	        nr=nol
	        atmsel1 = []
		atmsel2_1 = []
		atmselm = []
	        k=0
		ligand=metals.split("\t")
		ligresi_count=0
	        for i in ldata:		
		        b=[]
		        b=i.split(" ")
		        #print b	
		       
			atmsel1.append('(%s and resn %s and resi %s and chain %s and name %s)'%(modelName,b[7], b[6], b[9], b[8] ))
			atmsel2_1.append('(%s and resn %s and resi %s and chain %s)'%(modelName, b[6], b[7], b[9]))
			ligresi_count=ligresi_count+1
				#atms_sel2.append('%s'%b[8])
		atmselm.append('(%s and resn %s and resi %s and chain %s and name %s)'%(modelName,ligand[0], ligand[1], ligand[2], ligand[0]))
	        #cmd.bg_color('white')
	        cmd.hide('lines', '%s'%modelName)
	        cmd.show('cartoon', '%s'%modelName)
	        cmd.util.cbc(selection='%s'%modelName,first_color=7,quiet=1,legacy=0,_self=cmd)
	        cmd.hide('cartoon', 'HETATM and %s'%modelName)
	        cmd.show('lines','HETATM and %s'%modelName)
	        cmd.color('blue','HETATM and %s'%modelName)
	        cmd.color('brown','HETATM and resn HOH and %s'%modelName)
	        cmd.select('atms1', ' '.join('%s' % u1 for u1 in atmsel1))
		cmd.select('atms2_1', ' '.join('%s' % u2 for u2 in atmsel2_1))
		#cmd.hide('cartoon','atms2_1 and %s'%modelName)
		cmd.show('sticks','atms2_1 and %s'%modelName)
		cmd.set("stick_radius", 0.008,'atms2_1')
	        #cmd.label('atms2_1','name')
	        cmd.util.cbao(selection='atms2')
		cmd.select('metal','(%s and resn %s and resi %s and chain %s)'%(modelName,ligand[0], ligand[1], ligand[2]))
		cmd.set("sphere_scale", value=0.2, selection='metal')
                cmd.show('spheres', '(%s) and metal'%(modelName))
	        #cmd.color('red', 'ligands and %s'%modelName)
	        #cmd.spectrum('count','rainbow','ligands and %s'%modelName)
		
	        cmd.util.cbag(selection='metal')

	        t_n=0
		nr=ligresi_count
	        while t_n<nr:
			cmd.select('atm11', atmselm[0])
		        cmd.select('atms22', atmsel1[t_n])
		        cmd.distance('pairs', 'atm11','atms22')		
		        t_n=t_n+1
	        cmd.orient('atms2_1')
		if (ligresi_count==0):
			print "No interactive residues!"
	        cmd.label('metal','name')
	        #cmd.set('label_color', 'red')
	        cmd.label('atms2_1 and name CA','resn + resi')
	        #cmd.set('label_color', 'white')
	        cmd.deselect()
	        cmd.delete('atms1')
	        cmd.delete('atms12')
	        cmd.delete('atms22')
		cmd.delete('atms2_1')
	        #cmd.delete('ligand')
