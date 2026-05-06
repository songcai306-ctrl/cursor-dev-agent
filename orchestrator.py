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

    def run(self, task):
        print("Step 1: Planning...")
        plan = self.planner.plan(task)

        print("Step 2: Coding...")
        code = self.coder.generate(plan)

        print("Step 3: Reviewing...")
        review = self.reviewer.review(code)

        print("Step 4: Testing...")
        test_report = self.tester.test(code)

        return {
            "plan": plan,
            "code": code,
            "review": review,
            "test": test_report
        }
