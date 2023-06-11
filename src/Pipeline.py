import ComponentePipeline


class Pipeline(ComponentePipeline):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def execute(self, context):
        print("Pipeline has started")

        for module in self.components:
            module.execute(context)

        print("Pipeline has finished")
