import logging
import asab.web.rest


L = logging.getLogger(__name__)


class RemoteDockerApp(asab.Application):
	def __init__(self):
		super().__init__()
		import asab.web

		self.add_module(asab.web.Module)
		import asab.proactor

		self.add_module(asab.proactor.Module)
		self.ProactorService = self.get_service("asab.ProactorService")

		self.WebService = self.get_service("asab.WebService")
		self.WebContainer = asab.web.WebContainer(self.WebService, "webcontainer")
		self.WebContainer.WebApp.middlewares.append(
			asab.web.rest.JsonExceptionMiddleware
		)

		from .status import StatusWebHandler, StatusWebservice

		self.StatusWebservice = StatusWebservice(self)
		self.StatusWebHandler = StatusWebHandler(self, self.StatusWebservice)

		from .manage import ManageWebHandler, ManageWebservice

		self.ManageWebservice = ManageWebservice(self)
		self.ManageWebHandler = ManageWebHandler(self, self.ManageWebservice)

		from .run import RunWebHandler, RunWebservice

		self.RunWebservice = RunWebservice(self)
		self.RunWebHandler = RunWebHandler(self, self.RunWebservice)
