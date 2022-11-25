from os import system as terminal, name as os_name


def clear():
    terminal('clear') if os_name != "nt" else terminal('cls')
