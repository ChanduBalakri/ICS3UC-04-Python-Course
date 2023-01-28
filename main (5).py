##
# Zodiac Compatibility - Unit Testing
#
# @author name
# @course ICS3UC
# @date 2000/00/00 - last modified
##

import unittest #Include the pyUnit unittest framework
import zodiac    #The file that you are testing

# The following is the class in which all functions will be ran by unittest
class ZodiacTestP1(unittest.TestCase):
    # Main class for testing;
    # Functions beginning with "test" will be run
    # testing for subprogram getZodiacSign
    def test_getZodiac1(self):
      # Provide your test cases
      self.assertEqual(zodiac.getZodiacSign(1,20), ("capricorn", "earth"))
      self.assertEqual(zodiac.getZodiacSign(5, 11), ("aries","fire"))
      self.assertNotEqual(zodiac.getZodiacSign(7, 19), ("gemini", "water"))
      
    # testing for subprogram getPowerCouple
    def test_getPower1(self):
    # Provide your test cases
      self.assertEqual(zodiac.getPowerCouple("taurus", "cancer"), ("power couple"))
      self.assertEqual(zodiac.getPowerCouple("libra", "capricorn"), ("power couple"))
      self.assertEqual(zodiac.getPowerCouple("aquarius", "pisces"), ("power couple"))

    # testing for subprogram getPowerCouple
    def test_getDanger1(self):
      # Provide your test cases
      self.assertEqual(zodiac.getDangerousMatches("aries", "cancer"), ("danger couple"))
      self.assertEqual(zodiac.getDangerousMatches("leo", "capricorn"), ("danger couple"))

      self.assertEqual(zodiac.getDangerousMatches("virgo", "sagittarius"), ("danger couple"))
      
#Main
if __name__=='__main__':
    unittest.main(exit=False)