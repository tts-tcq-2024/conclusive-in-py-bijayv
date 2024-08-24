import unittest
import typewisealert
class TestTypewise(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewisealert.infer_breach(20, 50, 100) == 'TOO_LOW')
    check_and_alert("TO_CONTROLLER", {'coolingType': "PASSIVE_COOLING"}, 20)
if __name__ == '__main__':
  unittest.main()
