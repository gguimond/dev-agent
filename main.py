import sys
from flow import create_code_review_flow

def main():
    """Simple function to process a code review."""
    
    # Get path from command line if provided with --
    path = '.'
    for arg in sys.argv[1:]:
        if arg.startswith("--"):
            path = arg[2:]
            break
    
    # Create the agent flow
    code_review_flow = create_code_review_flow()
    
    # Process the path
    shared = {"code_path": path}
    print(f"🤔 Processing path: {path}")
    code_review_flow.run(shared)
    print("\n🎯 Final code review:")
    print(shared.get("code_review", "No code review found"))

if __name__ == "__main__":
    main()