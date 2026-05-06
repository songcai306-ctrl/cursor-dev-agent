from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.reviewer import ReviewerAgent
from agents.tester import TesterAgent


class DevOrchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.coder = CoderAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()

    def run(self, task: str):
        plan = self.planner.plan(task)
        code = self.coder.generate(plan)
        review = self.reviewer.review(code)
        test = self.tester.test(code)

        return {
            "plan": plan,
            "code": code,
            "review": review,
            "test": test,
        }
