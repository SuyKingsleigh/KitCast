#!/usr/bin/env python3
import argparse
import os
import sys

from kitcast.src.castnow import Castnow


class Kitcast:
    """
    Keys:
    -file video
    -subtitle subtitle.srt
    -device chromecast_name
    """
    def __init__(self, args):

        parser = argparse.ArgumentParser()
        parser.add_argument("-f", '--file', action='store', dest='filename')
        parser.add_argument('-s', '--subtitle', action='store', dest='subtitle')
        parser.add_argument('-d', '--device', action='store', dest='device')

        self.results = parser.parse_args()
        self.file = self.results.filename
        print(self.file + "\n\n")


    def _convert_to_cast(self):
        try:
            if not self.file:
                print("no filename specified, use -f video_name.extension")
                return -1
            else:
                os.system("./chromecastize.sh " + self.file)
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