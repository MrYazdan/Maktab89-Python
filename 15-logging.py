# from time import sleep
#
#
# # classic
# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls.instance


# metaclass
# class Singleton(type):
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls.instance
#
#
# s1 = Singleton()
# s2 = Singleton()


# class Logger(metaclass=Singleton):
# class Logger(Singleton):
#     ...
#
#
# l1 = Logger()
# l2 = Logger()
#
# print(l1 is l2)

# \033[...m     --->    pattern
# \033[0m     --->    reset
# \033[1m     --->    bold
# \033[3m     --->    italic
# \033[5m     --->    blink


# print("Salam")
# print(u"\033[35;5mSalam\033[0m", "Ali")
# print("Reza")

# 256 color :
# 38;5 -> foreground
# 48;5 -> background

# print("Salam")
# print(u"\033[38;5;160;1mSalam\033[0m")
# print(u"\033[48;5;160;1;38;5;220mSalam\033[0m")
#
# for n in range(0, 257):
#     if n % 10 == 0:
#         print()
#     print(u"\033[38;5;" + str(n) + u";1m" + str(n) + u"\033[0m\t", end="")
# print()
#
# # 38;2;r;g;b
# print(u"\033[38;2;0;255;0mSalam\033[0m")

import logging

# Debug => 10
# Info => 20
# Warn => 30
# Errr => 40
# Critical => 50

# logging.basicConfig(level=logging.ERROR)
# logging.debug("This is information")
# logging.info("This is information")
# logging.warning("This is information")
# logging.error("This is information")
# logging.critical("This is information")

# logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("Logging tutorial")
logger.handlers.clear()

stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('errors.logs')

stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.ERROR)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

logger.debug("Debug !!!")
logger.error("Error !!!")






