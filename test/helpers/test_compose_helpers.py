import unittest
from .testcase import TestCase

from remotedocker.compose.service import DockerComposeService, validate_append
import os


class TestDockerComposeHelpers(TestCase):

	def test_compose_validity(self):
		print(self.App.DockerCompose)
		self.assertEqual(
			self.App.docker_compose,
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
			self.docker_compose_class_instance_empty.list_current(),
			{"version": "3.8", "services": {}},
		)

		self.assertEqual(
			self.docker_compose_class_instance_full.list_current(),
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
			self.docker_compose_class_instance_empty.append,
			{"sup_bro": {"container_name": "howdy", "network_mode": "host"}},
		)

		self.assertRaises(
			ValueError,
			self.docker_compose_class_instance_empty.append,
			{"image": "hello-world"},
		)

	def test_append(self):
		self.docker_compose_class_instance_empty.append(
			to_append={
				"the_other": {
					"image": "hello-world",
					"container_name": "uaaa",
				}
			}
		)
		self.assertEqual(
			self.docker_compose_class_instance_empty.list_current(),
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
