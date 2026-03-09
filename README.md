This repository contains four python files that enable the user to:
  1) generate CLOUDY input files that will calculate heating and cooling rates (among many other parameters) (see makeCloudyInput.py)
  2) read CLOUDY output files, and extract and tabulate heating and cooling rates from them (see readCloudyOutput.py)
  3) plot the heating and cooling curves as a function of temperature (see plotCurves.py)
  4) do all above tasks from the terminal (see execAll.py)

All .py files are designed to be executed from the terminal

These programs require the following python packages:
  1) numpy
  2) Table from astropy.table
  3) matplotlib.pyplot
  4) subprocess

Users should have CLOUDY downloaded and functioning, and should preferrentially use versions c23.01 and up (though these programs should work for older versions)
