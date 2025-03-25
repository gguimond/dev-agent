from pocketflow import Node
from utils import call_llm, call_repomix, read_file, create_file

class PackCodebase(Node):
    def prep(self, shared):
        """Get the code path from shared store."""
        return shared["code_path"]
        
    def exec(self, code_path):
        """Repomix the code."""
        # Call the repomix utility function
        print(f"Repomix for: {code_path}")
        call_repomix(code_path)
        # Read generated file
        print(f"Read generated file")
        return read_file('custom-output.md')
    
    def post(self, shared, prep_res, exec_res):
        """Save the content from repomix."""
        # Add the context to the context in the shared store
        shared["context"] = {"role": "user", "content": exec_res}

        print(f"✅ Added repo content to context")

        return "default"

class CodeReview(Node):
    def prep(self, shared):
        """Get the context from shared store."""
        return shared["context"]
        
    def exec(self, context):
        """Call llm with appropriate prompt."""
        # Call the llm function
        print(f"Call llm")
        response = call_llm(context)
        # Create code review file
        print(f"Create code review file")
        create_file('code_review.md', response)
        return response
    
    def post(self, shared, prep_res, exec_res):
        """Save the final answer and complete the flow."""
        # Save the code review in the shared store
        shared["code_review"] = exec_res
        
        print(f"✅ Code review generated successfully")
        
        # We're done - no need to continue the flow
        return "done"