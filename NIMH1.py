#PROBLEM 1
#This program uses the NIMH Data Archive search API to search information about a query phrase,
#which is entered by the user (ex. depression). The program returns data elements scoring > 0.33
#for the query term and also includes the query term in the description field.
#Data elements meeting the criteria are returned. Each data element contains Notes, Data Strucutres,
#Name, Description, Score, ID, and Total Data Structures count.

import requests
import json
import sys

query_phrase = (sys.argv[1])

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=1021', headers={'Accept':'application/json'}, data= query_phrase)

search_results = json.loads(r.text)

data_elements = search_results['datadict']

n = 1
for i in data_elements['results']:
    if i['_score'] >0.33:
        if query_phrase.lower() in i['description'].lower():
            print '~DATA ELEMENT', n, '~'
            print 'Notes:', i['notes']
            print
            for a in i['dataStructures']:
                print 'Data Structures:'
                for k,v in a.iteritems():
                    print k,':', v
                print
            print 'Name:', i['name']
            print 'Description:', i['description']
            print 'ID:', i['id'] #all IDs are "" 
            print 'Score:', i['_score']
            print 'Total Data Structures:', i['total_data_structures']
            n += 1
            print '__________________________________________________'
