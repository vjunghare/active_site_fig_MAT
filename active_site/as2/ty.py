#!/usr/bin/python

import os

cwd = os.getcwd()
cwd= cwd + '/'
#print cwd
input_file ='Active_site2'
tnol=0
with open(input_file, "r") as ins:
	data = []
 	ins = [line.rstrip('\n') for line in ins]
	for line in ins:
		data.append(line)
		tnol=tnol+1
print tnol
nlig=0
temps= 'Ligand'
liglist=[]
tsl=0
lig_res=[]
nofl=0
#print data
for i in data:
	nofl=nofl+1
	if (i[:-1]==temps):
		print i
		nlig+=1
		liglist.append(i)
		if(nofl==1):
			tsl=nofl
		if(nofl!=1 ):
			ts=nofl-tsl
			lig_res.append(ts-1)
		if(nofl>1):
			tsl=nofl
	if(nofl==tnol):
		ts=nofl-tsl
		print ts, nofl, tsl
		lig_res.append(ts)

print liglist
print lig_res
print nofl
#for i in  t:
#	tp=t[i]
#	u.append(tp)	
#	print tp[3:]
	#f1= open( 'as2_ligand' + k[3:] + '_script.py',"w+")
	#f1.write('lig_data=[')
	#f1.close()
