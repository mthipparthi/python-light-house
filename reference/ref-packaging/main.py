import importlib
import pkgutil


class Shortener(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __getattr__(self, attr):
        # if attr not in self.available_shorteners:
        #     return self.__getattribute__(attr)

        # get instance of shortener class
        # short_module = importlib.import_module("{}.{}".format("pyshorteners.shorteners", attr))
        module = importlib.import_module("another_module")
        instance = getattr(module, attr)(**self.kwargs)

        return instance


def main():
    # module = importlib.import_module("another_module")
    # # available_modules = [i.name for i in pkgutil.iter_modules(module)]
    # print(module)
    s = Shortener(num1=2330022, num2=400)
    s.AnoModule1.print()


if __name__ == "__main__":
    main()
