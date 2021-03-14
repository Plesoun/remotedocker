import asab
import logging
from python_on_whales import docker

L = logging.getLogger(__name__)

class StatusWebservice(asab.Service):
	def __init__(self, app, service_name="status.StatusWebservice"):
		super().__init__(app, service_name):


	async def run_status_command(self, command: str):
		command_matrix = {
		"ps": docker.ps(),
		"images": docker.images(),
		}

		result = command_matrix.get(command, None)
		parsed_result = self.parse_command_output(command, result)
		return parsed_result


	def parse_command_output(command: str, result: Object):
		parse_matrix = {
		"ps": "neco",
		"images": "necotaky",
		}
		pass
