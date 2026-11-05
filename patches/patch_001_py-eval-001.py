# Patch for: Code injection via eval/exec
# CWE-95 | CRITICAL
# Original file: starfyre/js/store.py line 25
# User-controlled input passed to eval() or exec(). An attacker can execute arbitrary Python code on the server.

# VULNERABLE (original):
# new_data = eval(f"{temp_data.strip().strip(';')}")

# PATCHED (fixed):
# Fixed: use ast.literal_eval for safe parsing
import ast
result = ast.literal_eval(user_input)  # only parses literals
