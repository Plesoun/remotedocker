import logging
import remotedocker

L = logging.getLogger(__name__)

if __name__ == '__main__':
	app = webui_microservice.RemoteDockerApp()
	app.run()
