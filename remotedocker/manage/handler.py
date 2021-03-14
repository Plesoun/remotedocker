import logging

import asab
import asab.web.rest

L = logging.getLogger(__name__)

class ManageWebHandler:
	def __init__(self, app, svc):
		self.ManageWebservice = svc
		web_app = app.WebContainer.WebApp
		web_app.router.add_get(r"/manage/{manage_command}/{manage_arguments}", self.manage)

	async def manage(self, request):
		# Could send multiple commands in the future
		command = request.match_info["manage_command"]
		arguments = request.match_info["manage_arguments"]
		response = await self.ManageWebservice.run_manage_command(command, arguments)
		if response is False:
			return asab.web.rest.json_response(request, {"result": "Command not found"})
		return asab.web.rest.json_response(request, response)
