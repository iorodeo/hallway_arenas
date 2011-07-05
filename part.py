"""
Base class for makeing parts
"""
class Part(object):

    def __init__(self, **kwargs):
        self.params = kwargs
        self.make()

    def __str__(self):
        if self.part:
            return self.part.__str__()
        else:
            return ''

    def make(self):
        self.part = []

