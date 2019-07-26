#!/usr/bin/env python

# first export proper variables run export.sh
# then run install on each repo, after updating each one  you have to cd to $HOME/repo
# then now name of docker image and version 
# then run docker comands tag and push 
# You could call a init.sh shell here to run first steps

import os,subprocess
import xml.etree.ElementTree as ET

tree = ET.parse('pom.xml')
root = tree.getroot()
registry="EXAMPLE"

ms_name=root[3].text
ms_version=root[4].text

print "TODO MAKING repo dir,,,,,,,,,,,,,,,,,"
print "toDO CLONING repos.................."
print "This is the MICROSERVICE name ......."
print "....................................."
print root[3].text    
print "....................................."
print "This is the DOCKER IMAGE version....."
print root[4].text
print "....................................."



print "TAGING/PUSHING docker image........."

subprocess.call(['docker', 'tag', '{0}'.format(ms_name), 'us.gcr.io/{0}/{1}:{2}'.format(registry,ms_name,ms_version)])


