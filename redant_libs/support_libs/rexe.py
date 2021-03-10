class Remote_ops:
    def __init__(self, value):
        self.rex_value = value

    def remote_command_execute(self, cmd):
        return str(self.rex_value) + cmd
