import sublime
import sublime_plugin
import subprocess

class OpenWithVimCommand(sublime_plugin.WindowCommand):
    def run(self):
        terminal = "gnome-terminal"
        option = "--command"
        vim = "/usr/bin/vim"
        path = None

        if self.window.active_view():
            path = "\"" + self.window.active_view().file_name() + "\""
        else:
            sublime.error_message(__name__ + ": No file to open.")
            return

        args = [terminal, option, vim + " " + path]
        subprocess.Popen(args)
