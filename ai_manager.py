class AIManager:
    def __init__(self):
        self.models = {}

    def register_model(self, name, model):
        self.models[name] = model

    def get_model(self, name):
        return self.models.get(name)

    def route_request(self, request):
        target_model = request.get("target_model")
        if target_model in self.models:
            return self.models[target_model].process(request)
        else:
            return {"error": "Model not found"}