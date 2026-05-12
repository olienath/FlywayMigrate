# test_flywaymigrate.py
"""
Tests for FlywayMigrate module.
"""

import unittest
from flywaymigrate import FlywayMigrate

class TestFlywayMigrate(unittest.TestCase):
    """Test cases for FlywayMigrate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FlywayMigrate()
        self.assertIsInstance(instance, FlywayMigrate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FlywayMigrate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
