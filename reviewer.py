class ReviewerAgent:
    def review(self, code: str) -> dict:
        issues = []

        if "except Exception" in code:
            issues.append("捕获异常过于宽泛，建议细化")

        if "timeout" not in code:
            issues.append("建议添加请求超时控制")

        score = 100 - len(issues) * 10

        return {
            "score": score,
            "issues": issues if issues else ["未发现明显问题"],
        }
