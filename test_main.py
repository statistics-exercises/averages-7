import scipy.stats as st
import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( len(this_x)==200, "your graph has the wrong number of data points" )
        for i in range( len(this_x) ) :
            self.assertTrue( np.abs(i + 1 - this_x[i])<1e-7, "the x-coordinates in your graph are incorrect" )
            bar = np.sqrt(var/(i+1))*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( 1 / this_y[i] - 1/pval )<bar, "you appear to be sampling from the wrong statistical distribution" )
    
