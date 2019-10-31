def _add_logger(obj, channel=None, root_channel=None, attr_name="__logger"):
    cls = obj
    channel = channel or cls.__name__
    root_channel = root_channel if root_channel is not None else cls.__module__
    if root_channel:
        channel = root_channel + "." + channel
    if attr_name.startswith("__"):
        attr_name = "_" + cls.__name__ + "__logger"
    # attr_name="__logger"
    setattr(obj, attr_name, logging.getLogger(channel))


def logged(obj):
    _add_logger(obj, root_channel="")
    return obj


from utils import set_log_config

set_log_config()


import logging


# @logged
# class BaseClass:
#     def __init__(self, *args, **kwargs):
#         self._name = "Helloow  ewew"
#         self.__mahyss = None

#     def print_me(self):
#         print(type(self.__logger))
#         self.__logger.error("printme printme printme")


@logged
class Myclass:

    # my_class_car = "my_class_car"

    # @classmethod
    # def my_class_var(cls):
    #     return cls.my_class_car

    def __init__(self, **kwargs):
        self._name = "MYClass"
        self.__mahys22s = 100
        return self

    def __call__(self):
        print(dir(self))
        print(type(self.__logger))
        self.increment()

        self.print_me()
        # print(self.__logger.info("Hello WOrld"))
        # print(self.my_class_var())

    def increment(self):
        self.__mahys22s += 1
        self.__logger.error(f"Hello WOrld {self.__mahys22s}")


def main():
    mc = Myclass()
    print(mc())
    # print(f"{mc.my_class_var()}")

    for i in range(2):
        print(Myclass().increment())


if __name__ == "__main__":
    main()
