from yapsy.IPlugin import IPlugin

class PluginInterface(IPlugin):

    def generate(self):
        raise NotImplementedError()
