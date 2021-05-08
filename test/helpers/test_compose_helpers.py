import unittest
from .testcase import TestCase

from remotedocker.compose.service import DockerComposeService, validate_append
import os


class TestDockerComposeHelpers(TestCase):

	def test_appending_to_service(self):
		self.assertEqual({"Created": "test"}, self.App.DockerComposeService.add_object(object_id="test"))

	def test_removing_from_service(self):
		self.App.DockerComposeService.add_object(object_id="test")
		self.assertEqual({"Removed": "test"}, self.App.DockerComposeService.remove_object(object_id="test"))

	def test_list_objects(self):
		self.App.DockerComposeService.add_object(object_id="test1")
		self.App.DockerComposeService.add_object(object_id="test2")
		self.App.DockerComposeService.add_object(object_id="test3")
		self.assertEqual(["test1", "test2", "test3"], list(self.App.DockerComposeService.list_objects()))

	def test_object_info(self):
		self.App.DockerComposeService.add_object(object_id="test1")
		self.App.DockerComposeService.add_object(object_id="test2", compose_path="{}/test/helpers/docker-compose.yaml".format(os.getcwd()))
		self.assertEqual({"version": "3.8", "services": {}}, self.App.DockerComposeService.object_info(object_id="test1"))
		self.assertEqual({
					"version": "3.8",
					"services": {
						"sup_bro": {
							"image": "hello-world",
							"container_name": "howdy",
							"network_mode": "host",
						}
					},
				}, self.App.DockerComposeService.object_info(object_id="test2"))

	# def test_compose_validity(self):
	# 	print(self.App.DockerComposeService)


	# 	self.assertEqual(
	# 		self.App.docker_compose,
	# 		{"version": "3.8", "services": {}},
	# 	)
	#
	# 	self.assertEqual(
	# 		self.docker_compose_class_instance_full.docker_compose,
	# 		{
	# 			"version": "3.8",
	# 			"services": {
	# 				"sup_bro": {
	# 					"image": "hello-world",
	# 					"container_name": "howdy",
	# 					"network_mode": "host",
	# 				}
	# 			},
	# 		},
	# 	)
	#
	# def test_list_current(self):
	# 	self.assertEqual(
	# 		self.docker_compose_class_instance_empty.list_current(),
	# 		{"version": "3.8", "services": {}},
	# 	)
	#
	# 	self.assertEqual(
	# 		self.docker_compose_class_instance_full.list_current(),
	# 		{
	# 			"version": "3.8",
	# 			"services": {
	# 				"sup_bro": {
	# 					"image": "hello-world",
	# 					"container_name": "howdy",
	# 					"network_mode": "host",
	# 				}
	# 			},
	# 		},
	# 	)
	#
	# def test_validate_append(self):
	# 	self.assertRaises(
	# 		ValueError,
	# 		validate_append,
	# 		"wrong_input",
	# 	)
	#
	# 	self.assertRaises(
	# 		ValueError,
	# 		self.docker_compose_class_instance_empty.append,
	# 		{"sup_bro": {"container_name": "howdy", "network_mode": "host"}},
	# 	)
	#
	# 	self.assertRaises(
	# 		ValueError,
	# 		self.docker_compose_class_instance_empty.append,
	# 		{"image": "hello-world"},
	# 	)
	#
	# def test_append(self):
	# 	self.docker_compose_class_instance_empty.append(
	# 		to_append={
	# 			"the_other": {
	# 				"image": "hello-world",
	# 				"container_name": "uaaa",
	# 			}
	# 		}
	# 	)
	# 	self.assertEqual(
	# 		self.docker_compose_class_instance_empty.list_current(),
	# 		{
	# 			"version": "3.8",
	# 			"services": {
	# 				"the_other": {
	# 					"image": "hello-world",
	# 					"container_name": "uaaa",
	# 				}
	# 			},
	# 		},
	# 	)
