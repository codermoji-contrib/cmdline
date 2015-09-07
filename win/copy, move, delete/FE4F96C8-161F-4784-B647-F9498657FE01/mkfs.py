# Make sure you set the current working directory properly.
# This script will be run with the folder it is in as the cwd.
# The namespace will be populated with a variable called "fs"
# which is the target folder which must be set up.
import os
path = os.path.join(fs, 'secrets.txt')
with open(path, 'w') as f:
    f.write('blah')

# Generally, the way this would work is that I would copy sources
# into the fs location, and then execute the term cmds on them, and
# then collect the output.

path = os.path.join(fs, 'nested', 'test.txt')
os.makedirs(os.path.dirname(path))
open(path, 'w').write('test')
