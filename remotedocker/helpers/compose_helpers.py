import yaml
import logging
import subprocess

L = logging.getLogger(__name__)


class DockerCompose:
	def __init__(self, compose_path=None):
		self.compose_path = compose_path
		if self.compose_path:
			with open(self.compose_path) as file:
				self.docker_compose = yaml.load(file, Loader=yaml.FullLoader)
		else:
			self.docker_compose = {"version": "3.8", "services": {}}

	def docker_compose_list_current(self):
		return self.docker_compose

	def docker_compose_append(self, to_append: dict):
		if validate_append(to_append):
			print("hhhhh")
			self.docker_compose["services"].update(to_append)
		else:
			raise ValueError("Invalid append specified")

	def docker_compose_remove(self, to_remove: str):
		self.docker_compose["services"].pop(to_remove)

	def docker_compose_persist(self):
		with open(self.compose_path, "w") as file:
			file.write(yaml.dump(self.docker_compose, sort_keys=False))

	def docker_compose_up(self):
		if self.compose_path:
			capture_output = subprocess.run(
				["docker-compose", "-f", compose_path, "up", "-d"], capture_output=True
			)
			return {"docker-compose-return-code": capture_output.returncode}

		else:
			capture_output = subprocess.run(
				["docker-compose", "-f", "docker-compose.yaml", "up", "-d"],
				capture_output=True,
			)
			return {"docker-compose-return-code": capture_output.returncode}


def depth(d):
	if isinstance(d, dict):
		return 1 + (max(map(depth, d.values())) if d else 0)
	return 0


def validate_append(to_append: dict):
	if depth(to_append) >= 2:
		for key in to_append.keys():
			if "image" in to_append[key].keys():
				return True
			else:
				raise ValueError("Image not specified")
	else:
		raise ValueError("Incorrect input")
