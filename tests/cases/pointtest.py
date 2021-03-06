# $Id: pointtest.py 4533 2005-04-14 18:33:56Z sean $
#
# Project:  MapServer
# Purpose:  xUnit style Python mapscript tests of Point
# Author:   Sean Gillies, sgillies@frii.com
#
# ===========================================================================
# Copyright (c) 2004, Sean Gillies
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
# ===========================================================================
#
# Execute this module as a script from mapserver/mapscript/python
#
#     python tests/cases/pointtest.py -v
#
# ===========================================================================

import os, sys
import unittest

# the testing module helps us import the pre-installed mapscript
from testing import mapscript
from testing import MapscriptTestCase

class PointObjTestCase(MapscriptTestCase):
    
    def testPointObjConstructorNoArgs(self):
        """point can be created with no arguments"""
        p = mapscript.pointObj()
        self.assertAlmostEqual(p.x, 0.0)
        self.assertAlmostEqual(p.y, 0.0)
    
    def testPointObjConstructorArgs(self):
        """point can be created with arguments"""
        p = mapscript.pointObj(1.0, 1.0)
        self.assertAlmostEqual(p.x, 1.0)
        self.assertAlmostEqual(p.y, 1.0)
    
    def testSetXY(self):
        """point can have its x and y reset"""
        p = mapscript.pointObj()
        p.setXY(1.0, 1.0)
        self.assertAlmostEqual(p.x, 1.0)
        self.assertAlmostEqual(p.y, 1.0)
        if hasattr(p, 'm'):
            self.assertAlmostEqual(p.m, -2e38)
    
    def testSetXYM(self):
        """point can have its x and y reset (with m value)"""
        p = mapscript.pointObj()
        p.setXY(1.0, 1.0, 1.0)
        self.assertAlmostEqual(p.x, 1.0)
        self.assertAlmostEqual(p.y, 1.0)
        if hasattr(p, 'm'):
            self.assertAlmostEqual(p.m, 1.0)

    def testSetXYZ(self):
        """point can have its x, y, z reset (with m value)"""
        p = mapscript.pointObj()
        p.setXYZ(1.0, 2.0, 3.0, 4.0)
        self.assertAlmostEqual(p.x, 1.0)
        self.assertAlmostEqual(p.y, 2.0)
        if hasattr(p, 'z') and hasattr(p, 'm'):
            self.assertAlmostEqual(p.z, 3.0)
            self.assertAlmostEqual(p.m, 4.0)

    def testPoint__str__(self):
        """return properly formatted string"""
        p = mapscript.pointObj(1.0, 1.0)
        if hasattr(p, 'z'):
            p_str = "{ 'x': %.16g, 'y': %.16g, 'z': %.16g }" % (p.x, p.y, p.z)
        else:
            p_str = "{ 'x': %.16g, 'y': %.16g }" % (p.x, p.y)
        assert str(p) == p_str, str(p)
 
    def testPointToString(self):
        """return properly formatted string in toString()"""
        p = mapscript.pointObj(1.0, 1.0, 0.002, 15.0)
        if hasattr(p, 'z') and hasattr(p, 'm'):
            p_str = "{ 'x': %.16g, 'y': %.16g, 'z': %.16g, 'm': %.16g }" \
                  % (p.x, p.y, p.z, p.m)
        else:
            p_str = "{ 'x': %.16g, 'y': %.16g }" % (p.x, p.y)

        assert p.toString() == p_str, p.toString()



if __name__ == '__main__':
    unittest.main()
