#!/usr/bin/env python

# example on XMl parsing and subprocess use

import os,subprocess
import xml.etree.ElementTree as ET

tree = ET.parse('pom.xml') # parsing xml
root = tree.getroot()
registry="EXAMPLE"

ms_name=root[3].text
ms_version=root[4].text


print "This is the name ......."
print "....................................."
print root[3].text    
print "....................................."
print "This is the  version....."
print root[4].text
print "....................................."



print "TAGING/PUSHING docker image........."

subprocess.call(['docker', 'tag', '{0}'.format(ms_name), 'us.gcr.io/{0}/{1}:{2}'.format(registry,ms_name,ms_version)])


