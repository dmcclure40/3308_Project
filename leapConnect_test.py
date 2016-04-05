#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import leapConnect

class LeapConnectTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		pass
		
	@classmethod
	def tearDownClass(cls):
		pass
		
	def setUp(self):
		pass
	
	def tearDown(cls):
		pass
	
	def on_connect_test(self):
		p=leapConnect.Listener(Leap.Listener)
		self.assertEqual(p.on_connect,"Connected")
if __name__== '__main__':
	unittest.main()
