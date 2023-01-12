import time


def writer(path, writable):
    print("Open file ->")
    file = open(path, "w")
    time.sleep(2)

    try:
        print("Write file ->")
        file.write(writable)
        time.sleep(5)
        9/0

    except ZeroDivisionError:
        return None

    except KeyboardInterrupt:
        print("Sheitooni nakon !!!")

    finally:
        print("Close file ->")
        file.close()


# writer("names.txt", """
#     ali,
#     reza,
#     mohammad,
#     fatemeh,
#     heydar
# """)

class FileWriter:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        print("Open file ->", self.path)
        self.file = open(self.path, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)


with FileWriter("names.txt") as file:
    9/0
    file.write("Salam !")
