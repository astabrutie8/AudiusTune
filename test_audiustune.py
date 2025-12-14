# test_audiustune.py
"""
Tests for AudiusTune module.
"""

import unittest
from audiustune import AudiusTune

class TestAudiusTune(unittest.TestCase):
    """Test cases for AudiusTune class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AudiusTune()
        self.assertIsInstance(instance, AudiusTune)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AudiusTune()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
