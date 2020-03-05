# JSON example
# Disk pledges fuer ATLAS aus Germany
#
f=open('wlcg.json') # von https://wlcg-rebus.cern.ch/apps/pledges/resources/
import json
infos=json.load(f)
#infos[1]
#{u'PledgeType': u'Disk', u'Federation': u'CH-CERN', u'Country': u'Switzerland', u'PledgeUnit': u'Tbytes', u'ALICE': 14500, u'Tier': u'Tier 0', u'LHCb': 5500, u'ATLAS': 14000, u'CMS': 15000}
sumdisk=0
for info in infos:
   if info['PledgeType']=='Disk' and info['Country']=='Germany' and  info['ATLAS'] != '':
      print(info)
      sumdisk += int(info['ATLAS'])
      
print('Summe Disk ATLAS Germany ', sumdisk)


