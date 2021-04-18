import unittest

from remotedocker.helpers.compose_helpers import DockerCompose
import os

class TestDockerComposeHelpers(unittest.TestCase):

	def setUp(self):
		self.docker_compose_class_instance_empty = DockerCompose()
		self.docker_compose_class_instance_full = DockerCompose(compose_path="{}/test/helpers/docker-compose.yaml".format(os.getcwd()))

	def tearDown(self):
		print("Tearing down DockerCompose test")

	def test_compose_validity(self):
		self.assertEqual(
							self.docker_compose_class_instance_empty.docker_compose,
		 					{
								'version': '3.8',
								'services': {}
								}
							)

		self.assertEqual(
							self.docker_compose_class_instance_full.docker_compose,
		 					{
								'version': '3.8',
								'services': {
												'sup_bro':{
															'image': 'hello-world',
															'container_name': 'howdy',
															'network_mode': 'host'
															}
												}
								}
							)
