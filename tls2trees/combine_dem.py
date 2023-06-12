import os
import sys
import pandas as pd
import ply_io

DEM = pd.DataFrame()

for dem in sys.argv[1:]:

    DEM = pd.concat([DEM, pd.read_csv(dem)])

ply_io.write_ply('DEM.ply', DEM.rename(columns={'xx':'x', 'yy':'y', 'ZZ':'z'}))
