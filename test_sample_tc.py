
class test_class:

    def __init__(self, framework_handle):
        self.frh = framework_handle

    def test_fn(self):
        print(self.frh.peer_ops_function("Probe"))
        print(self.frh.volume_ops_function("PPP"))
