import asab
import logging
from python_on_whales import docker

from ..helpers import prepare_run_command
from ..helpers import prepare_entrypoint_command

L = logging.getLogger(__name__)

class RunWebservice(asab.Service):
	def __init__(self, app, service_name="status.RunWebservice"):
		super().__init__(app, service_name)
		self.ProactorService = app.get_service("asab.ProactorService")


	def run(self, json_data, mode=None):
		print(json_data)
		print(mode)
		parsed_run_commands = prepare_run_command(json_data)
		parsed_entrypoint_command = None

		if mode == "cli":
			pass

		elif mode == "api":
			pass

		else:
			return {"response": "Incorrect or no mode provided."}
