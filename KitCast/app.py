#!/usr/bin/python3
import argparse
import os
import sys

from castnow import Castnow


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

    def _convert_to_cast(self, file):
        try:
            if not file:
                print("no filename specified, use -f video_name.extension")
                return False
            else:
                os.system("~/.KitCast/KitCast/./chromecastize.sh " + file)
                return True
        except Exception as e:
            print(e.with_traceback())
            return False

    def run(self):
        print("Converting file to chromecast format like ")
        for file in self.file:
            print("casting ", file)
            if self._convert_to_cast(file):
                print("Successfully converted")
                Castnow(filename=file, results=self.results).cast()


if __name__ == '__main__':
    Kitcast(sys.argv).run()
