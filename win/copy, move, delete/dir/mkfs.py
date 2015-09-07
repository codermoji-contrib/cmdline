# Make sure you set the current working directory properly.
# This script will be run with the folder it is in as the cwd.
# The namespace will be populated with a variable called "fs"
# which is the target folder which must be set up.
import os
from random import choice


tmpl = '__file{}__'
for i in range(3):
    fname = tmpl.format(i)
    path = os.path.join(fs, fname)
    with open(path, 'w') as f:
        f.write('x'*choice(range(5,5000)))
