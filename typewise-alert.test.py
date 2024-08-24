import unittest
from typewisealert import infer_breach
class TestTypewise(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
