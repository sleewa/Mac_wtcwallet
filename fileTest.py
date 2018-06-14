import os

f = open('./Mainform.app/wa.xml', 'w')
os.path.realpath(__file__)
f.write("123")
f.close()