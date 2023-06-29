class PipelineException(Exception):
    "Raise cuando un pipeline debe parar."

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
