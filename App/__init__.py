import os
import sys
print os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+os.sep+'src')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+os.sep+'src'+os.sep+'neural_net')

import main