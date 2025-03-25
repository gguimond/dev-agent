from pocketflow import Flow
from nodes import CodeReview, PackCodebase

def create_code_review_flow():
    """
    Create and connect the nodes to form a code review flow.
    
    The flow works like this:
    1. PackCodebase node packs the code
    2. After PackCodebase completes, go to CodeReview
    
    Returns:
        Flow: A code review flow
    """
    # Create instances of each node
    pack = PackCodebase()
    review = CodeReview()

    pack >> review
    
    # Create and return the flow, starting with the DecideAction node
    return Flow(start=pack) 