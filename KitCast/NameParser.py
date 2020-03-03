import os
import pathlib
import shlex
import shutil


class NameParser:
    def __init__(self, name):
        self.name = name

    def get_original_name(self):
        return ''.join(self.name).replace("\\&", "&").replace("\\", " ")

    def rename(self):
        on = os.path.join(os.getcwd(), self.get_original_name())
        nn = self.get_original_name().replace(" ", "_")
        print("original name: ", on)
        print('new name: ', nn)

        os.rename(src=on, dst=os.path.join(os.getcwd(), nn))
        return nn


if __name__ == '__main__':
    NOME_ORIGINAL = 'Brooklyn Nine-Nine S06E02 Hitchcock & Scully.mkv'
    teste = ['Brooklyn\\', 'Nine-Nine\\', 'S06E02\\', 'Hitchcock\\', '\\&\\', 'Scully.mkv']
    s = ''.join(shlex.join(teste)).replace("'", '')

    print(
        NameParser(teste).rename()
    )
