import unittest
from typewise_alert import infer_breach


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')


if __name__ == '__main__':
  unittest.main()
