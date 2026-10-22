import cmd 
from pymol import stored
from pymol import stored, CmdException
import os 
cwd=os.getcwd()
cwd= cwd + '/' 

a_data=['LYS 43 A AND LYS 44 A  3.81989','GLU 58 A AND GLU 62 A  4.14473','LYS 159 B AND LYS 160 B  3.82586']

nc=[0]
nc[0]=3

#modelName='4oe9'

#print ifname

#print ldata
#cmd.fetch(modelName, async=0)

cmd.load(cwd + 'inputfile.pdb', 'inputfile')
modelName='inputfile'

ldata=[]
ldata=a_data

def out_atoms():
	
	#print nc[0]
	nr=nc[0]
	#print nr
	#print ldata
	atmsel1 = []
	atmsel2 = []
	sidechain1 = []
	sidechain2 = []
	for i in ldata:
		a= i.split(" ")
		#print a
		resiA = a[1]
		atomNameA = 'CA'
		chainA = a[2]
		resiB = a[5]
		atomNameB = 'CA'
		chainB = a[6]
		residue=[resiA,resiB]
		atoms=[atomNameA,atomNameB]
		chains=[chainA, chainB]
		
		ir=[0,1]
		for r, a, c, x in zip(residue, atoms, chains, ir):
				
			if ( (x % 2)==0):
				atmsel1.append('(%s and resi %s and chain %s and name %s)'%(modelName, r, c, a))
			else:
				atmsel2.append('(%s and resi %s and chain %s and name %s)'%(modelName, r, c, a))
	#print atmsel1
	#print "\n"
		for r, c, x in zip(residue, chains, ir):
			if ( (x % 2)==0):
				sidechain1.append('((%s and resi %s and chain %s))'%(modelName, r, c))
			else:
				sidechain2.append('((%s and resi %s and chain %s))'%(modelName, r, c))

	
	t_n=0
	tk=nr-1
	cmd.hide('lines', '%s'%modelName)
	cmd.show('cartoon', '%s'%modelName)
	cmd.color('green','%s'%modelName)
	cmd.hide('cartoon', 'HETATM and %s'%modelName)
	cmd.show('lines','HETATM and %s'%modelName)
	cmd.color('blue','HETATM and %s'%modelName)
	cmd.color('pink','HETATM and resn HOH and %s'%modelName)


	cmd.select('schain1', ' '.join('%s' % u1 for u1 in sidechain1))
	cmd.select('schain2', ' '.join('%s' % u2 for u2 in sidechain2))
	cmd.hide('cartoon', '(%s) and schain1'%(modelName))
	cmd.show('stick', '(%s) and schain1'%(modelName))
	cmd.color('red', 'schain1 and %s'%modelName)
	cmd.hide('cartoon', '(%s) and schain2'%(modelName))
	cmd.show('stick', '(%s) and schain2'%(modelName))
	cmd.color('red', 'schain2 and %s'%modelName)

	cmd.label('schain1 and name CA','resn + resi')
	cmd.label('schain2 and name CA','resn + resi')
	while t_n<nr:
		cmd.select('atms12', atmsel1[t_n])
		cmd.select('atms22', atmsel2[t_n])
		cmd.distance('pairs', 'atms12','atms22')		
		t_n=t_n+1

	cmd.orient(modelName)
	cmd.deselect()
	cmd.delete('schain1')
	cmd.delete('schain2')
	cmd.delete('atms12')
	cmd.delete('atms22')
	
out_atoms()
