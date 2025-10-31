import json
import re
import sys
from io import StringIO

class AssamesePythonTranspiler:
    def __init__(self, keyword_map_file='assamese_keywords.json'):
        """Initialize transpiler with keyword mappings"""
        with open(keyword_map_file, 'r', encoding='utf-8') as f:
            self.keyword_map = json.load(f)
        
        # Build reverse map for better performance
        self.assamese_to_python = {}
        for category, mappings in self.keyword_map.items():
            self.assamese_to_python.update(mappings)
    
    def transpile(self, assamese_code):
        """Convert Assamese code to Python"""
        python_code = assamese_code
        
        # Sort by length (descending) to handle longer phrases first
        sorted_keywords = sorted(
            self.assamese_to_python.items(), 
            key=lambda x: len(x[0]), 
            reverse=True
        )
        
        # Replace Assamese keywords with Python equivalents
        for assamese_keyword, python_keyword in sorted_keywords:
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(assamese_keyword) + r'\b'
            python_code = re.sub(pattern, python_keyword, python_code)
        
        return python_code
    
    def execute(self, python_code):
        """Execute Python code and capture output"""
        # Capture stdout
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output
        
        output = ""
        error = None
        
        try:
            # Execute the Python code
            exec(python_code, {'__builtins__': __builtins__})
            output = redirected_output.getvalue()
        except Exception as e:
            error = str(e)
        finally:
            # Restore stdout
            sys.stdout = old_stdout
        
        return output, error
    
    def run(self, assamese_code):
        """Transpile and execute Assamese code"""
        # Transpile to Python
        python_code = self.transpile(assamese_code)
        
        # Execute Python code
        output, error = self.execute(python_code)
        
        return {
            'assamese_code': assamese_code,
            'python_code': python_code,
            'output': output,
            'error': error,
            'success': error is None
        }


# Example usage
if __name__ == "__main__":
    transpiler = AssamesePythonTranspiler()
    
    # Example 1: Hello World
    example1 = """প্ৰিণ্ট("নমস্কাৰ পৃথিৱী!")"""
    
    print("=" * 50)
    print("Example 1: Hello World")
    print("=" * 50)
    result = transpiler.run(example1)
    print(f"Assamese Code:\n{result['assamese_code']}\n")
    print(f"Python Code:\n{result['python_code']}\n")
    print(f"Output:\n{result['output']}")
    
    # Example 2: Variables and arithmetic
    example2 = """x = ১০
y = ২০
যোগফল = x + y
প্ৰিণ্ট("যোগফল হৈছে:", যোগফল)"""
    
    print("\n" + "=" * 50)
    print("Example 2: Variables and Arithmetic")
    print("=" * 50)
    result = transpiler.run(example2)
    print(f"Assamese Code:\n{result['assamese_code']}\n")
    print(f"Python Code:\n{result['python_code']}\n")
    print(f"Output:\n{result['output']}")