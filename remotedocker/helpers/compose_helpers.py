import yaml
import logging
import subprocess

L = logging.getLogger(__name__)

class DockerCompose:
	def __init__(compose_path=None):
		self.compose_path = compose_path
		if self.compose_path:
			with open(self.compose_path) as file:
				self.docker_compose = yaml.load(file, Loader=yaml.FullLoader)
		else:
			self.docker_compose = {
									'version': '3.8',
									'services': {}
									}

	def docker_compose_list_current(self):
		return self.docker_compose

	def docker_compose_up(self, parameters: list):
		if self.compose_path:
			capture_output = subprocess.run(
								["docker-compose", "-f", compose_path, "up", "-d"],
								capture_output=True
								)
			return {"docker-compose-return-code": capture_output.returncode}
		else:
			capture_output = subprocess.run(
								["docker-compose", "-f", "docker-compose.yaml", "up", "-d"],
								capture_output=True
								)
			return {"docker-compose-return-code": capture_output.returncode}

	def docker_compose_append(self, to_append: dict):
		self.docker_compose["services"].update(to_append)

	def docker_compose_remove(self, to_remove: str):
		self.docker_compose["services"].pop(to_remove)

	def docker_compose_persist(self):
		with open(self.compose_path, "w") as file:
			file.write(yaml.dump(self.docker_compose, sort_keys=False))
