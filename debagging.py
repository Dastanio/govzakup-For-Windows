import os
from GetPdfLink import info
nameads = info[1][:100]
nameads = nameads.replace('"', '')

os.mkdir(nameads)
with open(os.path.join(nameads, 'file.txt'), 'w') as f:
  f.write('ss')



