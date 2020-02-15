# -*- coding: utf-8 -*-
"""
@author:        Andreas Kaeberlein
@copyright:     Copyright 2020
@credits:       AKAE

@license:       GPLv3
@maintainer:    Andreas Kaeberlein
@email:         andreas.kaeberlein@web.de
@status:        Development

@file:          atwg_unittest.py
@date:          2020-01-07
@version:       0.1.0

@note           Unittest for ATWG.py
                  run ./test/unit/atwg_unittest.py
"""



#------------------------------------------------------------------------------
# Python Libs
#
import sys        # python path handling
import os         # platform independent paths
import unittest   # performs test
import math       # check nan

# Module libs
#
sys.path.append(os.path.abspath((os.path.dirname(os.path.abspath(__file__)) + "/../../")))  # add project root to lib search path
import ATWG                                                                                 # Python Script under test
#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
class TestATWG(unittest.TestCase):

    #*****************************
    def setUp(self):
        """
        @note   set-ups test
        """
    #*****************************


    #*****************************
    def test_time_to_sec(self):
        """
        @note   checks time string to second conversion
        """
        # init values
        dut = ATWG.ATWG()
        # check exception: no time string
        with self.assertRaises(ValueError) as cm:
            dut.time_to_sec()
        self.assertEqual(str(cm.exception), "No time string provided")
        # check time in secs and numeric
        self.assertEqual(dut.time_to_sec(60), 60)
        # check time strin in pure seconds
        self.assertEqual(dut.time_to_sec("145"), 145)
        # check positional strings, format 'd:h:m:s'
        self.assertEqual(dut.time_to_sec("::30"), 30)
        self.assertEqual(dut.time_to_sec("02:30"), 150)
        self.assertEqual(dut.time_to_sec("01:02:30"), 3750)
        self.assertEqual(dut.time_to_sec("1.5:::"), 129600)
        # check with time units
        self.assertEqual(dut.time_to_sec("2day 2h"), 180000)
        self.assertEqual(dut.time_to_sec("1.5day 2.5h"), 138600)
        # check without numeric base
        self.assertEqual(dut.time_to_sec("h"), 3600)
        self.assertEqual(dut.time_to_sec("min"), 60)
        self.assertEqual(dut.time_to_sec("sec"), 1)
    #*****************************
    
    
    #*****************************
    def test_sec_to_time(self):
        """
        @note   checks time string to second conversion
        """
        # init values
        dut = ATWG.ATWG()
        # check exception: no time string
        with self.assertRaises(ValueError) as cm:
            dut.sec_to_time()
        self.assertEqual(str(cm.exception), "No time provided")
        # check exception: neagtive number of seconds provided
        with self.assertRaises(ValueError) as cm:
            dut.sec_to_time(-25)
        self.assertEqual(str(cm.exception), "Only non-negativ secs allowed")
        # convert to string, blank separated
        self.assertEqual(dut.sec_to_time(129631), "1d 12h 31s")
        self.assertEqual(dut.sec_to_time(29), "29s")
        self.assertEqual(dut.sec_to_time(0), "0")
        self.assertEqual(dut.sec_to_time(61), "1m 1s")
        self.assertEqual(dut.sec_to_time(61.5), "1m 1.5s")
        # convert to string, colomn based
        self.assertEqual(dut.sec_to_time(sec=129731, sep=":"), "1:12:2:11")
    #*****************************
    
    
    #*****************************
    def test_temp_grad_to_time(self):  
        """
        @note   check slew temperature to slew time conversion function
        """    
        # init values
        dut = ATWG.ATWG()
        # check exception: no gradient
        with self.assertRaises(ValueError) as cm:
            dut.temp_grad_to_time()
        self.assertEqual(str(cm.exception), "No temperature gradient given")
        # check conversion
        self.assertEqual(dut.temp_grad_to_time(gradient="5sec", deltaTemp=None), 5)
        
        
        
    #*****************************
    
    
    #*****************************
    def test_parse_cli(self):
        """
        @note   checks time string to second conversion
        """
        # init values
        dut = ATWG.ATWG()
        # check
        dut.parse_cli(["myFile", "--sine", "--riseTime=5sec", "--minTemp=5C", "--maxTemp=10c"])
        
        
        
    
    #*****************************
    

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
#------------------------------------------------------------------------------
