import asab
import subprocess
import yaml
import logging

from ..helpers import depth, validate_append
from .compose_object import DockerCompose


L = logging.getLogger(__name__)


# lock while one compose is in progress, run as worker make async (docker-compose up)
class DockerComposeService(asab.Service):
	def __init__(
		self,
		app,
		service_name="compose.DockerComposeService",
	):
		super().__init__(app, service_name)
		self.App = app
		self.ComposeObjects = {}

	def add_object(self, object_id: str, compose_path=None):
		self.ComposeObjects[object_id] = DockerCompose(
			self.App, compose_path
		)
		return {"Created": object_id}

	def remove_object(self, object_id: str):
		self.ComposeObjects.pop(object_id)
		return {"Removed": object_id}

	def list_objects(self):
		return self.ComposeObjects.keys()

	def object_info(self, object_id: str):
		info = self.ComposeObjects.get(object_id)
		if info:
			return info.docker_compose
		else:
			raise ValueError(
				"Object id: {} not found.".format(object_id)
			)
