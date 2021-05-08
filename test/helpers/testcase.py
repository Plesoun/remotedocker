import asab
import unittest
import logging
from remotedocker import RemoteDockerApp

class TestCase(unittest.TestCase):
	def setUp(self) -> None:
		print("setting up app")
		self.App = RemoteDockerApp(args=[])


	def tearDown(self):
		asab.abc.singleton.Singleton.delete(self.App.__class__)
		self.App = None
		root_logger = logging.getLogger()
		root_logger.handlers = []
