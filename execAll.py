import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt
import subprocess as sp

# make .in file
sp.run(['python', 'makeCloudyInput.py'])

# run CLOUDY
cloudyPath = str(input('path to CLOUDY executable: '))
cloudyExec = str(input('CLOUDY exec name (cloudy.exe if not changed by user): '))
inFilePath = str(input('path to .in file (w/o file extension): '))

print()
print('running CLOUDY')
sp.run([cloudyPath+'./'+cloudyExec, inFilePath])
print()

# read .out file
sp.run(['python', 'readCloudyOutput.py'])
print()
print('table generated')
print()

# plot curves
sp.run(['python', 'plotCurves.py'])