import asab
import subprocess
import yaml
import logging

from ..helpers import depth, validate_append


L = logging.getLogger(__name__)


# lock while one compose is in progress, run as worker make async (docker-compose up)
class DockerComposeService(asab.Service):
	def __init__(self, app, service_name="compose.DockerComposeService", compose_path=None):
		super().__init__(app, service_name)

		self.ComposeObjects = {}

	def add_object(self, object_id):
		pass

	def remove_object(self, object_id):
		pass
