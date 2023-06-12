import sys
import pickle
from fsct.tools import make_dtm

print(sys.argv[1])
params = pickle.load(open(sys.argv[1], 'rb'))
X = make_dtm(params)
