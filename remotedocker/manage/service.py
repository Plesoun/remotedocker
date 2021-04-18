import asab
import logging
from python_on_whales import docker

L = logging.getLogger(__name__)


class ManageWebservice(asab.Service):
	def __init__(self, app, service_name="status.ManageWebservice"):
		super().__init__(app, service_name)
		self.ProactorService = app.get_service("asab.ProactorService")

	async def run_manage_cli_command(self, command: str, arguments: str):
		parsed_arguments = arguments
		if command == "run":
			pass
		elif command == "start":
			result = await self.ProactorService.execute(docker.start, parsed_arguments)
		elif command == "stop":
			result = await self.ProactorService.execute(docker.stop, parsed_arguments)
		elif command == "remove":
			result = await self.ProactorService.execute(docker.remove)
		else:
			pass
		if result is None:
			return {"response": "OK"}
		return False

	async def run_manage_cli_command(self, command: str, arguments: str):
		return {"response": "Not Implemented"}
