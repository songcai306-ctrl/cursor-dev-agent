import argparse
from core.orchestrator import DevOrchestrator


def main():
    parser = argparse.ArgumentParser(description="Cursor Dev Agent CLI")
    parser.add_argument("--task", type=str, required=True, help="Development task description")

    args = parser.parse_args()

    orchestrator = DevOrchestrator()
    result = orchestrator.run(args.task)

    print("\n=== FINAL RESULT ===")
    for k, v in result.items():
        print(f"\n[{k.upper()}]\n{v}")


if __name__ == "__main__":
    main()
