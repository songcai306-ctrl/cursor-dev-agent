class ReviewerAgent:
    def review(self, code):
        issues = []
        if "except Exception" in code:
            issues.append("建议细化异常类型")

        return {
            "issues": issues,
            "score": 85
        }
