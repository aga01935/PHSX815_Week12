#! /usr/bin/env python

# imports of external packages to use in our code
import sys
#import math
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(".")
from Random import Random
if __name__ == "__main__":
    def parabola(par,x):
        value = (par[0])*x*x
        return value
    def exponential(par,x):
        val = (1./float(par[0])) * math.exp(-float(x)/float(par[0]))
    npar = 1
    Nexp = 1
    Nmeas = 1
    seed = 5555
    print (sys.argv[0])

    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-Nmeas' in sys.argv:
        p = sys.argv.index('-Nmeas')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nmeas = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne


    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("options:")
        print ("-seed <number >        provide any four digit seed for random number, default is 5555" )
        print ("-Nmes <number>         number of measurements to make, default is 1")
        print ("-Nexp <number>         number of experiment to perform, default is 1")
        print ("-output <string>       name of output file to produce, default is 1")
        print
        sys.exit(1)


# simulating the experiment:
    avg_list = []
    random = Random(seed)
    print ("Nmeas = ", Nmeas,"Nexp = ",Nexp,"Seed = ",seed)
    for g in range(1,npar+1):
        temp = random.exponential(0.02)/10.

        for e in range(0,Nexp):
            dataval =[]
            for t in range(0,Nmeas):
                val = random.parabolic_dist(temp,1.,10.)
                dataval.append(val)

            average = sum(dataval)/len(dataval)
            avg_list.append(average)


    plt.figure()
    plt.hist(avg_list,bins = 100,color = "g")
    #plt.SetXTitle("x axis")

    plt.show()
