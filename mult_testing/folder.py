import re

# Input Markdown file
with open("README.md", "r") as file:
    content = file.read()

# Regex pattern for code blocks
code_block_pattern = r"```(\w+)\n(.*?)```"

# Wrap each code block with <details> and <summary>
wrapped_content = re.sub(
    code_block_pattern,
    r"<details>\n<summary>Click to show \1 code</summary>\n\n```\1\n\2```\n\n</details>",
    content,
    flags=re.DOTALL,
)

# Output to a new Markdown file
with open("README.md", "w") as file:
    file.write(wrapped_content)
