from time import sleep


# classic
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


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

print("Salam")
print(u"\033[38;5;160;1mSalam\033[0m")
print(u"\033[48;5;160;1;38;5;220mSalam\033[0m")

for n in range(0, 257):
    if n % 10 == 0:
        print()
    print(u"\033[38;5;" + str(n) + u";1m" + str(n) + u"\033[0m\t", end="")
print()

# 38;2;r;g;b
print(u"\033[38;2;0;255;0mSalam\033[0m")
