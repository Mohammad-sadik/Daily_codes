import sys

print("Enter your text (Press Ctrl+D or Ctrl+Z to end input):")
text = sys.stdin.read()
print("\nCounts:")
print(f"Blanks: {text.count(' ')}")
print(f"Tabs: {text.count('\t')}")
print(f"Newlines: {text.count('\n')}")