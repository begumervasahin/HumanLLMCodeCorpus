b1 = True
b2 = True
b3 = False
b4 = True
b5 = True
import numpy as np
import matplotlib.pyplot as plt
import os
import config as cf; reload(cf)
import tools as tl; reload(tl)
import get_score as gs; reload(gs)
import get_paleo as ps; reload(ps)
import compare_score as cs; reload(cs)
b6 = cf.b6
b7 = cf.b7
b8 = np.arange(b6,b7+1)
b9 = [b3,b4,b5]
if b4:
  if not os.path.exists(cf.output_data_path+"plots"):
    os.makedirs(cf.
output_data_path+"plots")
b10 = cf.b10
b11 = cf.b11
b12 = tl.load_observations(b10,b11)
if b2:
  for ensnum in b8:
    print "ensemble number: "+str(ensnum)
    b13 = gs.pd_score(ensnum,b12,b9)
    if b1:
      b14 = ps.paleo_score(ensnum,b12,b9)
    if b3:
      plt.show()
b15 = cs.compare_score(b8,b1,b9)
b16 = b15.b16