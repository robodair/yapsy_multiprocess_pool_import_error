import main_interface
import multiprocessing as mp

class MultiprocessPlugin(main_interface.PluginInterface):

    def generate(self):
        pool = mp.Pool(8)

        result = pool.map(do_work, [1, 2, 3, 4, 5, 6, 7, 8])

        return result

def do_work(what):
    work = "Plugin process doing work: " + str(what)
    print work

    return work
