import asab
import logging
from python_on_whales import docker

L = logging.getLogger(__name__)

class RunWebservice(asab.Service):
	def __init__(self, app, service_name="status.RunWebservice"):
		super().__init__(app, service_name)
		self.ProactorService = app.get_service("asab.ProactorService")


	def run(self):
		pass
