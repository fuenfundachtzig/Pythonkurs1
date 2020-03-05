


def CountSurvived(pdict, cl, sex):
	nums=list(pdict['survived'].keys())
	ca=0
	cs=0
	for i in nums:
		if pdict['class'][i]==cl and pdict['sex'][i]==sex :
			ca += 1
			if pdict['survived'][i]==1 :
				cs += 1
	return cs, ca
	
	
import json
f=open('titanic.json')
pd=json.load(f)

cl=['First','Second','Third']
sx=['male','female']

for c in cl:
	for s in sx:
		ns,na=CountSurvived( pd, c, s)
		print((c,s, ns, na, float(ns)/na ))
 
