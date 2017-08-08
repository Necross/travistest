import unittest
import testpackage

class PackageTest(unittest.TestCase):

	def test_packit(self):
		self.assertEqual(7, testpackage.package.packit(3,4))

	def test_failing_packit(self):
		self.assertEqual(7, testpackage.package.packit(3,4))

