class pipelineRunner:
    def __init__(self):
        self.stages = []

    def add_stage(self, stage):
        self.stages.append(stage)

    def run(self):
        for stage in self.stages:
            stage
        