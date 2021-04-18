import asab
import logging
from python_on_whales import docker

L = logging.getLogger(__name__)


class StatusWebservice(asab.Service):
	def __init__(self, app, service_name="status.StatusWebservice"):
		super().__init__(app, service_name)

	async def run_status_command(self, command: str):
		command_matrix = {
			"ps": docker.ps(),
			"images": docker.images(),
		}

		result = command_matrix.get(command, None)
		parsed_result = parse_command_output(command, result)
		return parsed_result


def parse_command_output(command: str, result: list):
	parsed_result = []
	if command == "ps":
		for container_object in result:
			parsed_result.append(
				{
					"name": container_object.name,
					"entrypoint": container_object.args,
					"restart_count": container_object.restart_count,
					"mounts": [
						{
							"name": mount.name,
							"type": mount.type,
							"source": mount.source,
							"destination": mount.destination,
							"mode": mount.mode,
						}
						for mount in container_object.mounts
					],
				}
			)
	return parsed_result
	if command == "images":
		return {"result": "not implemented"}

	else:
		return False
