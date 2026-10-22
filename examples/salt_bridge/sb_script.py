import cmd 
from pymol import stored
from pymol import stored, CmdException
import os 
cwd=os.getcwd()
cwd= cwd + '/' 

a_data=['ARG 29 NH2 A 373 AND GLU 108 OE2 A 1607  2.79663','ARG 29 NH2 A 373 AND GLU 108 OE1 A 1606  3.58395','ARG 29 NH2 B 2140 AND GLU 108 OE2 B 3347  2.82062','ARG 29 NH2 B 2140 AND GLU 108 OE1 B 3346  3.48592','ARG 114 NH2 B 3445 AND ASP 79 OD1 B 2893  2.6849','ARG 114 NH2 B 3445 AND ASP 79 OD2 B 2894  3.99249']

nc=[0]
nc[0]=6

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
		atomNameA = a[2]
		chainA = a[3]
		resiB = a[7]
		atomNameB = a[8]
		chainB = a[9]
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
	#cmd.bg_color('white')
	cmd.hide('lines', '%s'%modelName)
	cmd.show('cartoon', '%s'%modelName)
	cmd.color('green','%s'%modelName)
	cmd.hide('cartoon', 'HETATM and %s'%modelName)
	cmd.show('lines','HETATM and %s'%modelName)
	cmd.color('blue','HETATM and %s'%modelName)
	cmd.color('brown','HETATM and resn HOH and %s'%modelName)
	
	cmd.select('atms1', ' '.join('%s' % u1 for u1 in atmsel1))
	cmd.select('atms2', ' '.join('%s' % u2 for u2 in atmsel2))
	#cmd.color('yellow', 'atms1 , atms2 and %s'%modelName)
	cmd.select('schain1', ' '.join('%s' % u1 for u1 in sidechain1))
	cmd.select('schain2', ' '.join('%s' % u2 for u2 in sidechain2))
	cmd.show('sticks', '(%s) and schain1'%(modelName))
	cmd.color('red', 'schain1 and %s'%modelName)
	cmd.show('sticks', '(%s) and schain2'%(modelName))
	cmd.color('red', 'schain2 and %s'%modelName)
	cmd.color('yellow', 'atms1 , atms2 and %s'%modelName)
	cmd.label('schain1 and name CA','resn + resi')
	cmd.label('schain2 and name CA','resn + resi')
	while t_n<nr:
		cmd.select('atms12', atmsel1[t_n])
		cmd.select('atms22', atmsel2[t_n])
		cmd.distance('pairs', 'atms12','atms22')		
		t_n=t_n+1
	
	cmd.deselect()
	cmd.delete('atms1')
	cmd.delete('atms2')
	cmd.delete('schain1')
	cmd.delete('schain2')
	cmd.delete('atms12')
	cmd.delete('atms22')
out_atoms()
