import logging

import asab
import asab.web.rest
import asab.web.tenant

L = logging.getLogger(__name__)

class StatusWebHandler:
	def __init__(self, app, svc):
		self.StatusWebservice = svc
		web_app = app.WebContainer.WebApp
		web_app.router.add_get(r"/docker/{status_command}", self.status)

	async def status(self, request):
		# Could send multiple commands in the future
		command = request.match_info["status_command"]
		response = await self.StatusWebservice.run_status_command(command)
		if response is False:
			return asab.web.rest.json_response(request, {"result": "Command not found"})
		return asab.web.rest.json_response(request, response)
