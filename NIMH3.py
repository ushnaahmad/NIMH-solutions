#PROBLEM 3
#This problem uses the data dictionary API to list the most recent change for each data
#element identified for the query (depression) from problem 1, as well as the most recent
#change for each unique data structure from problem 2. There are three functions in this
#program; dataelements is essentially problem #1, datastrucuture is problem #2, and lastchange
#is the function that determines and lists the most recent change based on the other two functions.
#The output is the data element (or data strucutre) with all associated fields and the last
#change with all associated fields. 

import requests
import json
import sys

query_phrase = (sys.argv[1])

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=1021', headers={'Accept':'application/json'}, data= query_phrase)

search_results = json.loads(r.text)

data_elements = search_results['datadict']

def dataelements(data):
    n = 1
    for i in data['results']:
        if i['_score'] >0.33:
            if query_phrase.lower() in i['description'].lower():
                print '~ DATA ELEMENT', n, '~'
                print 'Notes:', i['notes']
                print
                for a in i['dataStructures']:
                    print 'Data Structures:'
                    for k,v in a.iteritems():
                        print k,':', v
                    print
                print 'Name:', i['name']
                print 'Description:', i['description']
                print 'ID:', i['id']
                print 'Score:', i['_score']
                print 'Total Data Structures:', i['total_data_structures']

                elementName = i['name']
                #call last change funtion here
                lastchange(elementName, 'dataelement')
                n += 1
                print '__________________________________________________'


def datastruct(data):
    dslist = []
    for i in data['results']:
        if i['_score'] >0.33:
            if query_phrase.lower() in i['description'].lower():
                dslist.append(i['dataStructures'])
            
    idlist = []
    count = 1
    for struct in dslist:
        for i in struct:
            if int(i['id']) not in idlist:
                idlist.append(int(i['id']))
                print '~ DATA STRUCTURE', count, '~'
                for k,v in i.iteritems():
                    print k, ':', v
                
                shortName = i['shortName']
                lastchange(shortName, 'datastructure')
                print
                count +=1
                print '__________________________________________________'

    
def lastchange(name, x):
    rr = requests.get(('https://ndar.nih.gov/api/datadictionary/v2/' +x+ '/'+ name+ '/changes'), headers={'Accept':'application/json'})
    results = json.loads(rr.text)
    try:
        changes = results['list']
        last_change = changes[-1]
        print
        print 'LAST CHANGE:'
        for k,v in last_change.iteritems():
            print k, ':', v
    except KeyError:
        print 'No changes'

#dataelements(data_elements)
datastruct(data_elements)
