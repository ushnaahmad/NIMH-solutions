
<html>
    <div style = "display: inline-block; width=150px; height=75px;">
            <h2 style="text-align: center">NIMH Data Archive</h2>
        </div>
    <div>
        <div style="display: inline-block; width=150px; height=75px;">
            <img src="https://ndar.nih.gov/images/ndar/circuit_brain_red.png" alt="NIMH data archive image"/>            
        </div>        
	</div>
    <h2>Background</h2>
    <ul>
    <li>Joint initiative supported by NIMH, NICHD, NINDS, and NIEHS</li>
    <li>Contains data from a collection of repositories including the National Database for Autism Research (NDAR),  the RDoC Database (RDoCdb), the National Database for Clinical Trials related to Mental Illness (NDCT), and the NIH Pediatric MRI Repository (PedsMRI).</li>
    <li>Free data are available to the research community through a not too difficult application process</li>
    <li>Begun in late 2006, first data was received in 2008, significant data became available in 2012.</li>
    <li>Data submission every 6 months for NIMH awardees</li>
    </ul>
    
 <h2>Contact Us</h2>
<p>Email: NDAHelp@mail.nih.gov</p>
<p>Phone: 301-443-3265</p>

</html>    

<html>
    <h2>Some Numbers</h2>
    <div>
    <table align="left">
        <tr>
            <th>Data Type</th>
            <th>Subjects</th>
        </tr>
        <tr>
            <td>Clinical/Phenotype</td>
            <td>171,116</td>
        </tr>
                <tr>
            <td>EEG</td>
            <td>3,383</td>
        </tr>
        <tr>
            <td>Eye Tracking</td>
            <td>2,468</td>
        </tr>
        <tr>
            <td>fMRI</td>
            <td>8,256</td>
        </tr>
        <tr>
            <td>Genomics</td>
            <td>32,847</td>
        </tr>
        <tr>
            <td>Structural Imaging</td>
            <td>14,833</td>
        </tr>
    </table>
    </div>
    <div>

</html>  



<html>
<h2>New Projects</h2>
    <h3>Adolescent Brain Cognitive Development (ABCD) Study</h3>
    <ul>
    <li>Recruit 10,000 healthy children, ages 9 to 10 across the United States, and follow them into early adulthood.</li>
    <li>Use advanced brain imaging to observe brain growth with unprecedented precision.</li>
    <li>Examine how biology and environment interact and relate to developmental outcomes such as physical health, mental health, and life achievements including academic success</li>
    <li><a href="http://abcd-study.org/">Read more here...</a></li>
    </ul>
    <h3>Connectome Coordination Facility (CCF)</h3>
    <ul>
    <li>The CCF houses and distributes data for a series of studies focused on the connections within the human brain.</li>
    <li>The CCF currently supports 19 NIH-funded human connectome studies</li>
    <li>All data releases from the CCF studies will be made availble through the NIMH Data Archive </li>
    <li><a href="http://www.humanconnectome.org/about/project/">Read more here...</a></li></ul>
</html>

<html>
        
        <h2>NDA Search</h2>
        
      
    
        
        <p> A search tool available on the data archive <a href = "https://data-archive.nimh.nih.gov"> home page.</a> You can search by various categories, such as
    
           <ul><li>Content</li>
               <li>NDA Studies</li>
               <li/>Publications</li>
               <li>Collections</li>
               <li>Data Structures</li>
               <li>Data Elements</li>
               <li>Experiments</li>
               <li>Concepts</li></ul>
   
         You can also search by site.
           
           <ul><li>NDA</li>
               <li/>NDAR</li>
               <li>NDCT</li>
               <li>RDoCdb</li>
               <li>ABCD</li></ul>
    </p>
    
</html>

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Packaging Data</h2>
        <p>The next few slides will assume you have already queried your search and are ready for accessing the data files. </p>
        <p>For instructions and guidance on how to filter your cart and create a package to download, please refer to our <a href = "https://data-archive.nimh.nih.gov/training/training-modules"> training modules</a> on the NDA website.    
    
           <ul><li><a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.query.tools"> Query Tools </a></li>
   
           <li><a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.filter.cart" > Filter Cart </a></li>
           
           <li><a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.creating.package"> Create Package </a></ul></p>
    </div>
    
</html>

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Using Download Manager</h2>
            <p>Once a package has been created, data can be downloaded using the Download Manager tool. This tool is availabe to download at: https://ndar.nih.gov/DownloadManager.html (Note: not yet compatible with Java version 9).</p>    <p> For more information on how to use this tool, refer to the <a href = "https://data-archive.nimh.nih.gov/training/module?trainingModuleId=training.access&slideId=slide.download.manager"> download manager training module </a>
    
      </div>
    
</html>


```python
import csv

reader =csv.reader(open('image03.txt',"r"), delimiter = '\t')

dm = []
for row in reader:
    for element in row:
        if element.startswith('s3'):
            #print (element)
            dm.append(element)
```


```python
#Download Manager as a Webservice

import requests
import xml.etree.ElementTree as ET
from getpass import getpass

url = 'https://ndar.nih.gov/DataManager/dataManager'
username = input('Enter your NIMH Data Archives username:')
password = getpass('Enter your NIMH Data Archives password:')
package = input('Enter package ID:') #ex: 108728, 108335, 108772

payload = ('<?xml version="1.0" ?>\n'+
           '<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">\n' +
           '<S:Body> <ns3:QueryPackageFileElement\n' +
               'xmlns:ns4="http://dataManagerService"\n' +
               'xmlns:ns3="http://gov/nih/ndar/ws/datamanager/server/bean/jaxb"\n'+
               'xmlns:ns2="http://dataManager/transfer/model">\n' +
                   '<packageId>' + package +'</packageId>\n' +
                   '<associated>true</associated>\n' +
               '</ns3:QueryPackageFileElement>\n' +
           '</S:Body>\n' +
           '</S:Envelope>')


headers = {
    'Content-Type': "text/xml"
    }

r = requests.request("POST", url, data=payload, headers=headers)

root = ET.fromstring(r.text)

path = root.findall(".//path")

ws = []
for element in path:
    file = 's3:/'+ element.text
    print(file)
    ws.append(file)

```

<html>
    <h2>Using a miNDAR Package to Drive Exploration and Analysis</h2>
     <p>miNDAR is short for mini-NDAR, which is a remote database (Oracle) that you have control over and can push data to. This service requires authentication to ensure you are the miNDAR owner.</p>
    <ol><li>Connecting to the miNDAR containing the data you are interested in downloading</li>
    <li>Querying/Exploring data in the miNDAR</li>
    <li>Generating credentials for accessing s3 Objects</li>
    <li>Using credentials and s3 Object references from the miNDAR to retreive data</li></ol>
    
<h3>1. Connecting to the miNDAR containing the data you are interested in downloading</h3>
Once packaged, data can be pushed to a miNDAR in the form of where they will be availalbe as database tables and s3 object references. When data has finished loading into a miNDAR, you will receive an email with the connection information.
    <li>requires a Oracle client</li>
    <li>the following example uses Oracle Instant Client v12.2 and the python library cx_Oracle</li>
  
</html>


```python
import cx_Oracle
hostname = 'mindarvpc.cqahbwk3l1mb.us-east-1.rds.amazonaws.com'
port = 1521
sid = 'ORCL'

import getpass
username = input('Enter your miNDAR username:')#'username_package_id'
password = getpass.getpass('Enter your miNDAR password:')
dsnStr = cx_Oracle.makedsn(hostname, port, sid )
db = cx_Oracle.connect(user=username, password=password, dsn=dsnStr)

```

    Enter your miNDAR username:ahmadus_108728
    Enter your miNDAR password:········


<html>
    
<h3>2. Querying/Exploring Data in the miNDAR</h3>
After negotiating a successful connection we can query the miNDAR directly using SQL. We can retreive these results and store them as objects in R, Python, and many other programming languages.
Here we will query the table CONCEPT_BY_GUID, which is available in all miNDAR packages.
<li>in this example we store the results in a pandas dataframe (requries pandas)</li>
</html>


```python
#here we can retrieve the s3 URLs for image_file and data_file assoicated with each subject from the image03 table. 
#there is also an S3_LINKS table that lists all the s3 URLs available. 

import pandas as pd
import pandas.io.sql as psql

query = """SELECT subjectkey, image_file, data_file2
            FROM IMAGE03
            WHERE data_file2 IS NOT NULL"""
            
c = db.cursor()
c.execute(query)
data_files = pd.DataFrame(c.fetchall())
data_files.columns = [rec[0] for rec in c.description]

print(data_files)

miNDAR = []
for file in data_files['IMAGE_FILE']:
    miNDAR.append(file)

```

<html>
    
    <h3> 3. Generating credentials for accessing s3 Objects</h3>
    
Here we will generate credentials using our NIMH Data Archives username and password, which will allow us to authenticate and retreive data from AWS s3 Object storage for any shared objects.

<h4>There are a few ways you can generate tokens to access AWS s3 object storage</h4>
<li>You can generate credentails using the Download Manager GUI</li>
<li>We will use a python package for generating tokens, which is available on our GitHub.</li>



<h2>Generate FederatedToken</h2>
<ol><li>pip install git+https://github.com/NDAR/nda_aws_token_generator.git#egg=nda-aws-token-generator&subdirectory=python</li>
    <li>cd ~/nda_aws_token_generator/python/</li>
    <li>sudo python setup.py install</li></ol>



    </html>


```python
from getpass import getpass

url = 'https://ndar.nih.gov/DataManager/dataManager'
username = input('Enter your NIMH Data Archives username:')
password = getpass('Enter your NIMH Data Archives password:')

from nda_aws_token_generator import *
generator = NDATokenGenerator(url)
token = generator.generate_token(username, password)

print('aws_access_key_id=%s\n'
      'aws_secret_access_key=%s\n'
      'security_token=%s\n'
      'expiration=%s\n' 
      %(token.access_key,
        token.secret_key,
        token.session,
        token.expiration)
      )
```

    Enter your NIMH Data Archives username:ahmadus
    Enter your NIMH Data Archives password:········
    aws_access_key_id=ASIAIHO3YY6GIEHOVCOQ
    aws_secret_access_key=joJkGvuw4/h38SwsPANbA9AUrW9vlRsZm/G/Iq3v
    security_token=FQoDYXdzEN3//////////wEaDAZOHF25l8mN3sZWmCLUAbbyBzPbB/hrKK20w9wSt6JbGCc0pqu4/I+TatqQtkmEs1FP2DmrYFPDVAe99PYKOL2lqa9qA+rDPHk2PkLVzBDkhsBc001dRQsHjBrbmu8hqJrGIVB5RGqML9K/41SLqpHLnXEzSxGICG/V+S/v37yaykXSq+QWvOn/kXcOOSJhtWiI5zYMrVDQkW9VpySrvdwp9IorMJKCrtgt2CHlTqEExWAk3gyEg/VDhZlFnkKeHZl2Dm9fY9P1ivpWPnJCLTVhBGpPEtff3K5BB7WdbNpaL8w5KKX56tEF
    expiration=2017-12-21T02:40:21-05:00
    


<html>
    <h3>4. Using credentials and s3 Object references from the miNDAR to retreive data</h3>

Here we will combine our s3 credentials and the data we retrieved from the miNDAR, using the image_file and  data_file2 column that has our s3 Object references to retreive some Variant Call data about a subject.
    <li>We will use boto to interface with s3 objects</li>


```python
# Pull image out of S3

file = input("Enter S3 URL:")
#s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz

import boto.s3.connection
from urllib.parse import urlparse

cf = boto.s3.connection.OrdinaryCallingFormat()
conn = boto.connect_s3( token.access_key,
                        token.secret_key,
                        security_token=token.session,
                        calling_format=cf)

bucket = urlparse(file).netloc
key = urlparse(file).path
bucket_object = conn.get_bucket(bucket)
s3_object = boto.s3.key.Key(bucket_object)
s3_object.key = key
name = key.split('/')
name = name[-1]
byte_data = s3_object.get_contents_to_filename(name) #edit this file name to actually match s3
```

    Enter S3 URL:s3://NDAR_Central_2/submission_11013/002000001590/scanVisit__0020__0002/MRI__0001/B0_phase1/Native/Original__0001/DICOM.tar.gz


<html>
<p>The downloaded file can now be viewed and analyzed.  <b>It should be noted that the boto package provides functionality to read the object into memory as a 'string', which could be passed to other functions, and boto also supports streaming the content.</b></p>
</html>


```python
#lists = [dm, ws, miNDAR]
#will save only first five files in the list
count = 1
for file in dm:
    bucket = urlparse(file).netloc
    key = urlparse(file).path
    bucket_object = conn.get_bucket(bucket)
    s3_object = boto.s3.key.Key(bucket_object)
    s3_object.key = key
    name = key.split('/')
    name = name[-1]
    byte_data = s3_object.get_contents_to_filename(name) #edit this file name to actually match s3
    print(name)
    count += 1
    if count > 5:
        break

```

    NDARAB369MB6_image03_1373498869756.zip
    NDARAB369MB6_image03_1373498869756.jpg
    NDARAB369MB6_image03_1373497889885.zip
    NDARAB369MB6_image03_1373497889885.jpg
    NDARAB369MB6_image03_1373646986954.zip


<html>
<h2>New Functionality</h2>
<ul>
<li>Scratch Space provided</li>
<li>Computational Credits</li>
<li>Data Submission via Web Services</li>
</ul>
</html>


<html>
<div>
    <h3>Available APIs <a href="https://data-archive.nimh.nih.gov/API">https://data-archive.nimh.nih.gov/API</a></h3>
    <ul>
    
    <li>Data Dictionary <a href="https://ndar.nih.gov/swagger">https://ndar.nih.gov/api/datadictionary</a></li>
        
    <li>Search <a href="https://ndar.nih.gov/api/search">https://ndar.nih.gov/api/search</a></li>
    
    <li>Collection <a href="https://ndar.nih.gov/api/collection">https://ndar.nih.gov/api/collection</a></li>
    
    <li>GUID <a href="https://ndar.nih.gov/api/guid">https://ndar.nih.gov/api/guid</a></li>
    
    <li>Experiment <a href="https://ndar.nih.gov/swagger">https://ndar.nih.gov/api/experiment</a></li>

    <li>miNDAR <a href="https://ndar.nih.gov/api/mindar">https://ndar.nih.gov/api/mindar</a></li>
    
    
    </ul>
    
    </div>
 </html>

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>GUID Webservice</h2>
        <p>Provides the capability to programmatically access all submitted accross projects data for a specifc subject.</p>
        <p>This service requires authentication and will only return data that is accessible to your user, based on your privleges and permisisons on the data.</p>
    </div>
    <p>
    <a href="https://ndar.nih.gov/api/guid">Swagger User Interface</a>
    </p>
</html>


```python
import requests
import json
from getpass import getpass
#NDAR_INVRT663MBL
#NDAR_INVEP756TR3
#NDARBV344JLX

username = input("What is your NDA username:")
password = getpass("What is your NDA password:")
guid = input("What GUID would you like to access data from:")
#r = requests.get("https://ndar.nih.gov/api/guid/{}/data?short_name=image03".format(guid), 
#                 auth=requests.auth.HTTPBasicAuth(username, password),
#                 headers={'Accept': 'application/json'})

r = requests.get("https://stage.nimhda.org/api/guid/{}/data?short_name=image03".format(guid), 
                 auth=requests.auth.HTTPBasicAuth(username, password),
                 headers={'Accept': 'application/json'})

guid_data = json.loads(r.text)
print(guid_data)
```


```python
# Extract experiment IDs from response

experiments = []
ages = []
for age in guid_data['age']:
    age_value = age['value']
    for row in age['dataStructureRow']:
        for element in row['dataElement']:
            if element['name']=='EXPERIMENT_ID':
                if element['value'] not in experiments:
                    experiments.append(element['value'])

for experiment in experiments:
    print('experiment: {}'.format(experiment))
```


```python
# In previous 2 slides, have identified some fMRI, EEG, or Eye Tracking data; show how to retreive experimental details.

query = input("Enter your experiment ID:")
r = requests.get("https://ndar.nih.gov/api/experiment/{}".format(query),
                 headers={'Accept':'application/json'})

experiment = json.loads(r.text)
print(experiment)
```


```python
# Pull out image files from response
image_files = []
ages = []
for age in guid_data['age']:
    age_value = age['value']
    for row in age['dataStructureRow']:
        for link in row['links']['link']:
            if link['rel']=='data_file':
                image_files.append(link['href'])
                ages.append(age_value)
guid_list = []
for i,image in enumerate(image_files):
    print("age:{}, url:{}".format(ages[i],image))
    guid_list.append(image)
    
```

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Search Webservice</h2>
        <p>Provides the capability for programmatic search across all NDA sites (NDAR, pediatricMRI, ABCD, Clinical Trials, Human Connectome Project, etc.) enabling users to identify projects with data of potential interest.</p>
        <p>Search content includes experimental information, project descriptions, investigators, grant numbers, page-content, and all data elements that make up the 1000s of measures defined in the data dictionary.</p>
    </div>
    
    <p>
        <a href="https://ndar.nih.gov/api/search">Swagger User Interface</a>
    </p>
</html>

<html>
<div>
<h2>Full Search</h2>
<p>Search resource that allows for querying a word or phrase and identifying matching content, studies, collections, experiments, and data elements.</p>
</div>
<h2>Data Element Search</h2>
<p>Search resource that allows for specifying attributes of a data element and querying the entire dictionary for matching elements.</p>
<div>
<table style="float:left; margin-right:10px;">
<thead><tr><td>Attribute</td><td>Type</td></tr></thead>
<tbody>
  <tr><td>name</td><td>string</td></tr>
  <tr><td>description</td><td>string</td></tr>
  <tr><td>valueRanges</td><td>string</td></tr>
  <tr><td>notes</td><td>string</td></tr>
  <tr><td>type</td><td>string</td></tr>
  <tr><td>allQuery</td><td>string</td></tr>
</tbody>
</table>
</div>
</html>


```python
# Data Element Full Search

import requests
import json

query_phrase = input("Enter a description phrase:") #example: ABCD, depression, autism

r = requests.post('https://ndar.nih.gov/api/search/nda_sw_removal/dataelement/full?size=10', 
                  headers={'Accept':'application/json'}, data= query_phrase)

search_results = json.loads(r.text)

data_elements = search_results['datadict']
print ('Total data structures:', data_elements['total'])
print()

for i in data_elements['results']: #filter the data structures
    if i['_score'] > 0.33:
        if query_phrase.lower() in i['description'].lower():
            print ('Name:', i['name'])
            print ('id:', i['id'])
            print ('Notes:', i['notes'])
            print ('Description:', i['description'])
            print ('Score:', i['_score'])
            print ('Data Structures:')
            for k in i['dataStructures']:
                print(k)
            print ('Total Data Structures:', i['total_data_structures'])
            print()

```


```python
# Data Element Search

description = input("Enter a description to query:")
query = {'description': description}
r = requests.post("https://stage.nimhda.org/api/search/nda_sw_removal/dataElementSearch?size=20", 
                  data=json.dumps(query),
                  headers={'content-type':'application/json'})
element_results = json.loads(r.text)
for result in element_results['dataElements']: 
    print("score:{}\nname:{}\ndescription:{}\n".format(result['score'], result['name'], result['description']))
```


```python
# Here is a programmatic example searching by collection
import requests
import json


class collectionLink():

    def __init__(self, title, id):
            self.id = id
            self.title = title
            self._repr_html_()

    def _repr_html_(self):
        collection_link = 'https://ndar.nih.gov/edit_collection.html?id={}'.format(self.id)
        html = ['<a href="{}">{}</a>'.format(collection_link, self.title)]
        return ''.join(html)

    
query = input("Enter your query phrase:")
r = requests.post("https://ndar.nih.gov/api/search/nda_sw_removal/collection/full", query)
collections = json.loads(r.text)
print("\n")
for result in collections['collection']['results']:
    display(collectionLink(result['title'],result['id'])) 
```

<html>
    <div style = "display: inline-block; width=150px; height=75px;">
        <h2>Data Dictionary Webservice</h2>
        <p>Provides the capability for programmatic interrogation of all available datastructures/measures, by name, type, source, and category.  The service also provides element-level detail.</p>
        <p>Additionally, a history of changes can be retreived for both data sturcture and data elements.</p>
    </div>
    <p>
        <a href="https://ndar.nih.gov/swagger">Swagger User Interface</a>
    </p>
</html>


```python
# Progromatically retrieve data from the dictionary service
# Example data structure shortname: image03

import requests
import json
shortname = input('Enter a Data Structure shortname:')
r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/datastructure/{}'
                 .format(shortname),
                  headers={'Accept':'application/json'})
structure = json.loads(r.text)

# Get Data Structure change history

r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/datastructure/{}/changes'
                 .format(shortname),
                  headers={'Accept':'application/json'})

changes = json.loads(r.text)
```


```python
# Show data structure elements that are required, or potentially required (conditional)

for element in structure['dataElements']:
    if element['required'] in ['Required','Conditional']:
        print('elementInfo: {}\n'.format(element))
```


```python
# Show element name for all data elements with type as 'file'

for element in structure['dataElements']:
    if element['type'] == 'File':
        print('elementName: {}'.format(element['name']))
```


```python
# Get data element info and changes
from IPython.display import display

class changeHistoryTable():
    
    def __init__(self, list):
        self.list = list
        self.headers = ['id','changeDescription','changedDate','elementName','newValue','oldValue','shortName']
        self._repr_html_()
    
    def _repr_html_(self):

        html = ["<table width=100%>"]
        html.append("<thead><tr>")
        for header in self.headers:
            html.append("<td>{}</td>".format(header))
        html.append("</tr></thead><tbody>")      

        for row in self.list:
            html.append("<tr>")
            for header in self.headers:
                html.append("<td>{}</td>".format(row[header]))
            html.append("</tr>")
        html.append("</tbody></table>")
        return ''.join(html)

change_list = []
        
for element in structure['dataElements']: #search data elements in a data structure
    if element['type'] == 'File':
        r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/dataelement/{}' 
                 .format(element['name']),
                  headers={'Accept':'application/json'})
        elementInfo = json.loads(r.text) #information about the data element
        
        r = requests.get('https://ndar.nih.gov/api/datadictionary/v2/dataelement/{}/changes'
                .format(element['name']),
                headers={'Accept':'application/json'})
        changes = json.loads(r.text) #information about the data element changes
        try:
            change_list.extend(changes['list'])
        except KeyError:
            print('No changes for elementName {}'.format(element['name']))

display(changeHistoryTable(change_list))
```


```python
# Data Element Data Structure Search
# Returns a list of data structures for data element alphabetically
# Example data elements: gender, subjectkey

dataelement = input("Enter a data element name:")

r = requests.get('https://ndar.nih.gov/api/search/nda_sw_removal/dataElementDataStructures?name={}'.format(dataelement), 
                  headers={'Accept':'application/json'})

element = json.loads(r.text)

for data in element['dataElements']:
    for structure in data['dataStructures']:
        print("id:{}\ncategory:{}\nshortName:{}\nsubjectCount:{}\n".format(structure['id'], structure['category'], structure['shortName'], structure['subjectCount']))
```
