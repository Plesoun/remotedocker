import unittest

from remotedocker.helpers.compose_helpers import DockerCompose, validate_append
import os


class TestDockerComposeHelpers(unittest.TestCase):
	def setUp(self):
		self.docker_compose_class_instance_empty = DockerCompose()
		self.docker_compose_class_instance_full = DockerCompose(
			compose_path="{}/test/helpers/docker-compose.yaml".format(os.getcwd())
		)

	def tearDown(self):
		print("Tearing down DockerCompose test")

	def test_compose_validity(self):
		self.assertEqual(
			self.docker_compose_class_instance_empty.docker_compose,
			{"version": "3.8", "services": {}},
		)

		self.assertEqual(
			self.docker_compose_class_instance_full.docker_compose,
			{
				"version": "3.8",
				"services": {
					"sup_bro": {
						"image": "hello-world",
						"container_name": "howdy",
						"network_mode": "host",
					}
				},
			},
		)

	def test_list_current(self):
		self.assertEqual(
			self.docker_compose_class_instance_empty.docker_compose_list_current(),
			{"version": "3.8", "services": {}},
		)

		self.assertEqual(
			self.docker_compose_class_instance_full.docker_compose_list_current(),
			{
				"version": "3.8",
				"services": {
					"sup_bro": {
						"image": "hello-world",
						"container_name": "howdy",
						"network_mode": "host",
					}
				},
			},
		)

	def test_validate_append(self):
		self.assertRaises(
			ValueError,
			validate_append,
			"wrong_input",
		)

		self.assertRaises(
			ValueError,
			self.docker_compose_class_instance_empty.docker_compose_append,
			{"sup_bro": {"container_name": "howdy", "network_mode": "host"}},
		)

		self.assertRaises(
			ValueError,
			self.docker_compose_class_instance_empty.docker_compose_append,
			{"image": "hello-world"},
		)

	def test_append(self):
		self.docker_compose_class_instance_empty.docker_compose_append(
			to_append={
				"the_other": {
					"image": "hello-world",
					"container_name": "uaaa",
				}
			}
		)
		self.assertEqual(
			self.docker_compose_class_instance_empty.docker_compose_list_current(),
			{
				"version": "3.8",
				"services": {
					"the_other": {
						"image": "hello-world",
						"container_name": "uaaa",
					}
				},
			},
		)
