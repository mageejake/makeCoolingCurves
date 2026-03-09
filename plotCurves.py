import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # table path input
    tpath = str(input('table file path (w/ file extension): '))

    # read in table data
    tab = Table.read(tpath, format='ascii')
    temp = tab['log(T)']
    cool = tab['log(cool/n^2)']
    heat = tab['log(heat/n^2)']

    plt.plot(temp, cool, c='b', label='cooling')
    plt.plot(temp, heat, c='r', label='heating')
    plt.ylabel(r'log(cool/$n_H^2$)')
    plt.xlabel('log(T) [K]')
    plt.legend()
    plt.show()