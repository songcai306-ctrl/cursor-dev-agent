from core.orchestrator import DevOrchestrator

if __name__ == "__main__":
    task = "实现一个带缓存的API请求模块，并补充单元测试"

    orchestrator = DevOrchestrator()
    result = orchestrator.run(task)

    print("\n=== FINAL RESULT ===")
    print(result)
