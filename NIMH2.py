#PROBLEM 2
#This program lists each unique data structure identified from the data elements
#in PROBLEM 1. This is done by creating a list of all the data structures, and
#then creating a new list of just their IDs (assuming each data strucuture has
#a unique ID). If the ID is already in the idlist, then it is a repeat and not
#included in the output. If the ID is unique, then the data structure is listed
#and the subjectCount is included in the total.

import requests
import json
import sys

query_phrase = (sys.argv[1])

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=1021', headers={'Accept':'application/json'}, data= query_phrase)

search_results = json.loads(r.text)

data_elements = search_results['datadict']

dslist = []
#sub_count = []
for i in data_elements['results']:
    if i['_score'] >0.33:
        if query_phrase.lower() in i['description'].lower():
            dslist.append(i['dataStructures'])
            #sub_count.append(i['total_data_structures'])
            
idlist = []
sclist = []
count = 1
for struct in dslist:
    for i in struct:
        if int(i['id']) not in idlist:
            idlist.append(int(i['id']))
            sclist.append(int(i['subjectCount']))
            print '~ DATA STRUCTURE', count, '~'
            for k,v in i.iteritems():
                print k, ':', v
            print
            count +=1


#print idlist
#print sclist
#print 'Total non-unique data structures:', sum(sub_count)
print 'TOTAL subjectCount:', sum(sclist)
