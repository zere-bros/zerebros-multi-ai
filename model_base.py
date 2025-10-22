class BaseModel:
    def __init__(self, name):
        self.name = name

    def process(self, request):
        raise NotImplementedError("Must implement process method")