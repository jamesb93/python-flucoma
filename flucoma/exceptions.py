class BinError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)

class ShellError(Exception):
    def __init__(self, msg:str):
        super().__init__(msg)