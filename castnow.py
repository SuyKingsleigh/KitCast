import os


class Castnow:
    # filename = video
    # device = chromecast
    # sub = subtitle file
    def __init__(self, filename, device=None, sub=None):
        self.file_name = filename

        # chromecast name
        if device:
            self.device = device
        else:
            self.device = False

        # subtitle file name
        if sub:
            self.sub = sub
        else:
            self.sub = False

    # command to run
    def _commands(self):
        command = "castnow "
        if self.device:
            command += " --device " + self.device

        if self.sub:
            command += " --subtitles " + self.sub + " ./" + self.sub

        command += " ./" + self.file_name
        return command

    def cast(self):
        try:
            os.system(command=self._commands())
        except Exception as e:
            print(e.with_traceback())
