import pymol 
from pymol import stored
from pymol import cmd, CmdException
input_file='4oe9.pdb'
cmd.load( input_file , '4oe9' )
modelName='4oe9'

print "Ligand 1- CIT 201 A"
ligands=[]
ligand_1='CIT 201 A'
lig_data=['CIT 201 O1 A 103 AND SER 39 HG A 544  3.99678','CIT 201 O1 A 103 AND SER 39 OG A 534  3.89973','CIT 201 C3 A 106 AND ARG 73 HH12 A 1046  3.63191','CIT 201 O7 A 107 AND SER 39 HB2 A 541  3.02667','CIT 201 O7 A 107 AND SER 39 HB3 A 542  3.25921','CIT 201 O7 A 107 AND SER 39 HA A 538  3.88837','CIT 201 O7 A 107 AND SER 39 HA A 539  3.85952','CIT 201 O7 A 107 AND SER 39 HB3 A 543  3.65013','CIT 201 O7 A 107 AND SER 39 CB A 532  3.66716','CIT 201 O7 A 107 AND SER 39 CB A 533  3.73167','CIT 201 O7 A 107 AND ALA 40 H A 552  3.89233','CIT 201 O7 A 107 AND ALA 40 H A 551  3.87817','CIT 201 C5 A 109 AND HIS 69 NE2 A 988  3.40283','CIT 201 C5 A 109 AND HIS 69 HE1 A 994  3.76366','CIT 201 C5 A 109 AND HIS 69 CE1 A 987  3.96658','CIT 201 C5 A 109 AND ALA 40 HB2 A 555  3.82457','CIT 201 O3 A 110 AND HIS 69 CD2 A 986  3.71217','CIT 201 O3 A 110 AND ARG 73 NH1 A 1034  3.81508','CIT 201 O3 A 110 AND ARG 73 HH11 A 1045  3.86872','CIT 201 O3 A 110 AND ARG 73 HG3 A 1041  3.83807','CIT 201 O3 A 110 AND HIS 69 HD2 A 993  3.90526','CIT 201 O4 A 111 AND SER 39 C A 528  3.68034','CIT 201 O4 A 111 AND SER 39 C A 529  3.67892','CIT 201 O4 A 111 AND SER 39 CA A 527  3.55521','CIT 201 O4 A 111 AND SER 39 CA A 526  3.53096','CIT 201 O4 A 111 AND ALA 40 CB A 550  3.63352','CIT 201 O4 A 111 AND ALA 40 N A 546  2.87785','CIT 201 O4 A 111 AND ALA 40 CA A 547  3.83929','CIT 201 O4 A 111 AND ALA 40 HB3 A 556  3.33774','CIT 201 C6 A 112 AND ARG 73 NH2 A 1035  3.78127','CIT 201 C6 A 112 AND ARG 73 HH22 A 1048  3.09808','CIT 201 C6 A 112 AND ARG 73 CZ A 1033  3.96569','CIT 201 O5 A 113 AND ARG 73 HH21 A 1047  3.63631','CIT 201 HO7 A 117 AND SER 39 HB2 A 540  3.60924']
metal_data=['K 202 B']

ldata=[]
ldata=lig_data
nol=(len(ldata))
def out_atoms(modelName):

	        nr=nol
	        atmsel1 = []
	        atmsel2 = []
		atmsel2_1 = []
	        #atms_sel2=[]
	        k=0
		ligand=ligand_1.split(" ")
		ligresi_count=0
		if(nol==0):
			print "This ligand has no interacting residues!"
			cmd.hide('lines', '%s'%modelName)
			cmd.show('cartoon', '%s'%modelName)
			cmd.util.cbc(selection='%s'%modelName,first_color=7,quiet=1,legacy=0,_self=cmd)
			cmd.hide('cartoon', 'HETATM and %s'%modelName)
			cmd.show('lines','HETATM and %s'%modelName)
			cmd.color('blue','HETATM and %s'%modelName)
			cmd.color('brown','HETATM and resn HOH and %s'%modelName)
			cmd.select('ligands','(%s and resn %s and resi %s and chain %s)'%(modelName,ligand[0], ligand[1], ligand[2]))
			count = 0
			for i in metal_data:
		                i=i.split(" ")
		                if((i[0]==ligand[0]) and (i[1]==ligand[1]) and (i[2] == ligand[2])):
		                        count=count+1
		        if(count > 0):
				cmd.set("sphere_scale", value=0.2, selection='ligands')
		                cmd.show('spheres', '(%s) and ligands'%(modelName))
		                
		        else:
		                cmd.show('sticks', '(%s) and ligands'%(modelName))
			#cmd.color('red', 'ligands and %s'%modelName)
			#cmd.spectrum('count','rainbow','ligands and %s'%modelName)
	
			cmd.util.cbag(selection='ligands')
			#cmd.label('ligands','name')
		else:
			for i in ldata:		
				b=[]
				b=i.split(" ")
				#print b	
			       
				if(b[6]!=ligand[0]):
					atmsel1.append('(%s and resn %s and resi %s and chain %s and name %s)'%(modelName,b[0], b[1], b[3], b[2] ))
					atmsel2.append('(%s and resn %s and resi %s and chain %s and name %s)'%(modelName, b[6], b[7], b[9], b[8]))
					atmsel2_1.append('(%s and resn %s and resi %s and chain %s)'%(modelName, b[6], b[7], b[9]))
					ligresi_count=ligresi_count+1
					#atms_sel2.append('%s'%b[8])

			#cmd.bg_color('white')
			cmd.hide('lines', '%s'%modelName)
			cmd.show('cartoon', '%s'%modelName)
			cmd.util.cbc(selection='%s'%modelName,first_color=7,quiet=1,legacy=0,_self=cmd)
			cmd.hide('cartoon', 'HETATM and %s'%modelName)
			cmd.show('lines','HETATM and %s'%modelName)
			cmd.color('blue','HETATM and %s'%modelName)
			cmd.color('brown','HETATM and resn HOH and %s'%modelName)
			cmd.select('atms1', ' '.join('%s' % u1 for u1 in atmsel1))
			cmd.select('atms2', ' '.join('%s' % u2 for u2 in atmsel2))

			cmd.select('atms2_1', ' '.join('%s' % u2 for u2 in atmsel2_1))
			#cmd.hide('cartoon','atms2_1 and %s'%modelName)
			cmd.show('sticks','atms2_1 and %s'%modelName)
			cmd.set("stick_radius", 0.008,'atms2_1')
			#cmd.label('atms2_1','name')
	
			cmd.util.cbao(selection='atms2')
			
			cmd.select('ligands','(%s and resn %s and resi %s and chain %s)'%(modelName,ligand[0], ligand[1], ligand[2]))
		        count = 0
		        for i in metal_data:
		                i=i.split(" ")
		                if((i[0]==ligand[0]) and (i[1]==ligand[1]) and (i[2] == ligand[2])):
		                        count=count+1
		        if(count > 0):
				cmd.set("sphere_scale", value=0.2, selection='ligands')
		                cmd.show('spheres', '(%s) and ligands'%(modelName))
		                
		        else:
		                cmd.show('sticks', '(%s) and ligands'%(modelName))
			#cmd.color('red', 'ligands and %s'%modelName)
			#cmd.spectrum('count','rainbow','ligands and %s'%modelName)
	
			cmd.util.cbag(selection='ligands')

			t_n=0
			nr=ligresi_count
			while t_n<nr:
				cmd.select('atms12', atmsel1[t_n])
				cmd.select('atms22', atmsel2[t_n])
				cmd.distance('pairs', 'atms12','atms22')		
				t_n=t_n+1
			cmd.orient('atms2_1')
			#if (ligresi_count==1):
				#print "No interactive residues!"
			cmd.label('ligands','name')
			#cmd.set('label_color', 'red')
			cmd.label('atms2_1 and name CA','resn + resi')
			#cmd.set('label_color', 'white')
			cmd.deselect()
			cmd.delete('atms1')
			cmd.delete('atms2')
			cmd.delete('atms12')
			cmd.delete('atms22')
			cmd.delete('atms2_1')
			#cmd.delete('ligand')

out_atoms(modelName)
