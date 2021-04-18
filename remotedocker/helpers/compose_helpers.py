import yaml
import logging

L = logging.getLogger(__name__)

class DockerCompose:
	def __init__(compose_path):
		with open(compose_path) as file:
			self.docker_compose = yaml.load(file, Loader=yaml.FullLoader)

	def docker_compose_list_current(self):
		return self.docker_compose

	def docker_compose_up(self, parameters: list):
		pass

	def docker_compose_append(self, to_append: dict):
		pass

	def docker_compose_remove(self, to_remove: str):
		pass
