#!/usr/bin/python3
import argparse
import os
import pathlib
import shlex
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
        parser.add_argument("-f", '--file', action='store', dest='filename', nargs='*', required=True, help=
        "The name of the video you want to cast, must include extension")
        parser.add_argument('-s', '--subtitle', action='store', dest='subtitle',
                            help="Subtitle file, must include extension")
        parser.add_argument('-d', '--device', action='store', dest='device',
                            help="If you want more than one device you should name the chromecast")

        self.results = parser.parse_args()
        self.file = self.results.filename

    def _convert_to_cast(self):
        self.file = shlex.join(self.file)

        if len(self.file) > 1: print("The name should not contain spaces nor special characters")

        try:
            if not self.file:
                print("no filename specified, use -f video_name.extension")
                return False
            else:
                os.system("~/.KitCast/KitCast/./chromecastize.sh " + self.file)
                return True
        except Exception as e:
            print(e.with_traceback())
            return False

    def run(self):
        print("Converting file to chromecast format like ")
        if self._convert_to_cast():
            print("Successfully converted")
            Castnow(filename=self.file, results=self.results).cast()


if __name__ == '__main__':
    Kitcast(sys.argv).run()
