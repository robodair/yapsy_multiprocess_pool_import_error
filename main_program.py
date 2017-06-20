from yapsy.PluginManager import PluginManager
import os

plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")

def main():
    simplePluginManager = PluginManager(plugin_info_ext="plugin")
    simplePluginManager.getPluginLocator().setPluginPlaces([plugin_dir])
    simplePluginManager.getPluginLocator().disableRecursiveScan()
    simplePluginManager.collectPlugins()

    generators = []
    for plugin_info in simplePluginManager.getAllPlugins():
        simplePluginManager.activatePluginByName(plugin_info.name)
        generators.append(plugin_info.plugin_object.generate)

    out = []
    for gen in generators:
        out.append(gen())
    return out

if __name__ == "__main__":
    main()
