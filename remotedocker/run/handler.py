import logging

import asab
import asab.web.rest

L = logging.getLogger(__name__)

class RunWebHandler:
	def __init__(self, app, svc):
		self.RunWebservice = svc
		web_app = app.WebContainer.WebApp
		web_app.router.add_get(r"/run/cli", self.run_cli)
		web_app.router.add_get(r"/run/api", self.run_api)

	@asab.web.rest.json_schema_handler({
	'type': 'object',
	'properties': {
		'docker_commands': {'type': 'object'},
		'entrypoint_commands': {'type': 'object'}
	}})
	async def run_cli(self, request, *, json_data):
		print(json_data)
		return asab.web.rest.json_response(request, {"result": "OK"})


	@asab.web.rest.json_schema_handler({
	'type': 'object',
	'properties': {
		'docker_commands': {'type': 'object'},
		'entrypoint_commands': {'type': 'object'}
	}})
	async def run_api(self, request):
		print(json_data)
		return asab.web.rest.json_response(request, {"result": "OK"})
