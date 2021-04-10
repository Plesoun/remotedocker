import logging

import asab
import asab.web.rest

L = logging.getLogger(__name__)

class ManageWebHandler:
	def __init__(self, app, svc):
		self.ManageWebservice = svc
		web_app = app.WebContainer.WebApp
		web_app.router.add_get(r"/manage/cli/{manage_command}/{manage_arguments}", self.manage_cli)
		web_app.router.add_get(r"/manage/api/{manage_command}/{manage_arguments}", self.manage_api)

	async def manage_cli(self, request):
		# Could send multiple commands in the future
		command = request.match_info["manage_command"]
		arguments = request.match_info["manage_arguments"]
		response = await self.ManageWebservice.run_manage_cli_command(command, arguments)
		if response is False:
			return asab.web.rest.json_response(request, {"result": "Command not found"})
		return asab.web.rest.json_response(request, response)


	async def manage_api(self, request):
		command = request.match_info["manage_command"]
		arguments = request.match_info["manage_arguments"]
		response = await self.ManageWebservice.run_manage_api_command(command, arguments)
		if response is False:
			return asab.web.rest.json_response(request, {"result": "Command not found"})
		return asab.web.rest.json_response(request, response)
