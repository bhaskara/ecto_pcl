#!/usr/bin/env python

"""
This example shows how to read/write pcd files.
"""

import ecto, ecto_pcl
import sys

plasm = ecto.Plasm()

pcdfile = 'cloud.pcd'
if len(sys.argv) > 1:
    pcdfile = sys.argv[1]

reader = ecto_pcl.PCDReader("Reader", filename=pcdfile)
writer = ecto_pcl.PCDWriter("Writer", filename_format="ascii_%04d.pcd", binary=False)

plasm.connect(reader[:] >> writer[:])

if __name__=="__main__":
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute(niter=1)

