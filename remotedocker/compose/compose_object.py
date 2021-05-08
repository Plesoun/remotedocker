import asab
import subprocess
import yaml
import logging

from ..helpers import depth, validate_append


L = logging.getLogger(__name__)


# lock while one compose is in progress, run as worker make async (docker-compose up)
class DockerCompose:

	def __init__(self, app, compose_path=None):
		self.ProactorService = app.get_service("asab.ProactorService")
		self.compose_path = compose_path
		if self.compose_path:
			with open(self.compose_path) as file:
				self.docker_compose = yaml.load(
					file, Loader=yaml.FullLoader
				)
		else:
			self.docker_compose = {
				"version": "3.8",
				"services": {},
			}
	def list_current(self):
		return self.docker_compose

	def append(self, to_append: dict):
		if validate_append(to_append):
			self.docker_compose["services"].update(
				to_append
			)
		else:
			raise ValueError("Invalid append specified")

	def remove(self, to_remove: str):
		self.docker_compose["services"].pop(to_remove)

	def persist(self):
		with open(self.compose_path, "w") as file:
			file.write(
				yaml.dump(
					self.docker_compose, sort_keys=False
				)
			)

	async def up(self):
		if self.compose_path:
			capture_output = subprocess.run(
				[
					"docker-compose",
					"-f",
					compose_path,
					"up",
					"-d",
				],
				capture_output=True,
			)
			return {
				"docker-compose-return-code": capture_output.returncode
			}

		else:
			capture_output = subprocess.run(
				[
					"docker-compose",
					"-f",
					"docker-compose.yaml",
					"up",
					"-d",
				],
				capture_output=True,
			)
			return {
				"docker-compose-return-code": capture_output.returncode
			}
