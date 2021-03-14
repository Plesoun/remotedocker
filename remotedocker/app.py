import logging
import asab.web
import asab.web.rest


L = logging.getLogger(__name__)

class RemoteDockerApp(asab.Application):
	def __init__(self):
		super().__init__()
		self.add_module(asab.web.Module)

		self.WebService = self.get_service("asab.WebService")
		self.WebContainer = asab.web.WebContainer(self.WebService, "webcontainer")
		self.WebContainer.WebApp.middlewares.append(asab.web.rest.JsonExceptionMiddleware)

		from .status import StatusWebHandler, StatusWebservice
		self.StatusWebservice = StatusWebservice(self)
		self.StatusWebHandler = StatusWebHandler(self, self.StatusWebservice)
