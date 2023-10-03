import unittest
from Cryptage import * 


class Test_Cryptage(unittest.TestCase): 
    def setUp(self):
        self.instance=Test_Cryptage()
    
    def crypt(self,message,pas):
        