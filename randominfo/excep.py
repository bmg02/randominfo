class CustomError(Exception):
    def __init__(self, err):
        self.err = err
        pass
    def __str__(self):
        return self.err