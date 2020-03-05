#!/usr/bin/python3
import argparse
import os
import pathlib
import sys

from castnow import Castnow

from NameParser import NameParser


class Kitcast:
    """
    Keys:
    -file video
    -subtitle subtitle.srt
    -device chromecast_name
    """

    def __init__(self, args):

        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument("-f", '--file', action='store', dest='filename', nargs='*')
        parser.add_argument('-s', '--subtitle', action='store', dest='subtitle')
        parser.add_argument('-d', '--device', action='store', dest='device')

        self.results = parser.parse_args()
        self.file = self.results.filename
        # print(self.file + "\n\n")

    def _convert_to_cast(self):
        if len(self.file) > 1:
            pass
            try:
                self.file = NameParser(self.file).rename()
            except:
                print('Failed to rename file')
                print("The name should not contain special characters, nor spaces")
        else:
            self.file = self.file[0]
        try:
            if not self.file:
                print("no filename specified, use -f video_name.extension")
                return -1
            else:
                os.system("~/.KitCast/KitCast/./chromecastize.sh " + self.file)
                return 1
        except Exception as e:
            print(e.with_traceback())
            return 2

    def run(self):
        print("Converting file to chromecast format like ")
        if self._convert_to_cast() > 0:
            print("Successfully converted")
            Castnow(filename=self.file, results=self.results).cast()


if __name__ == '__main__':
    Kitcast(sys.argv).run()
