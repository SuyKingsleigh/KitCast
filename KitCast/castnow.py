import os


class Castnow:
    # filename = video
    # device = chromecast
    # subtitle = subtitle file
    def __init__(self, filename, results):
        self.file_name = filename

        # chromecast original_name
        if results.device:
            self.device = results.device
        else:
            self.device = False

        # subtitle file original_name
        if results.subtitle:
            self.subtitle = results.subtitle
        else:
            self.subtitle = False

    # command to run
    def _commands(self):
        command = "castnow "
        if self.device:
            command += " --device " + self.device

        if self.subtitle:
            command += " --subtitles " + self.subtitle

        command += " " + self.file_name

        return command

    def cast(self):
        try:
            os.system(command=self._commands())
        except Exception as e:
            print(e.with_traceback())
