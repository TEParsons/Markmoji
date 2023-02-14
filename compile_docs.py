import markdown
import pybtex
import markmoji

import logging
import textwrap
from os import mkdir
from pathlib import Path

# Setup some useful stuffimp
encoding = 'utf-8'
logging.getLogger().setLevel(logging.INFO)
rootDir = Path(__file__).parent / "docs"
handlersDir = rootDir / "handlers"
# Make sure we have a handlers dir
if not handlersDir.is_dir():
    mkdir(str(handlersDir))

# Setup markdown processor
md = markdown.Markdown(extensions=["extra", markmoji.Markmoji()])

# Create markdown file for each handler

handlerList = {}
for cls in markmoji.handlers.map.values():
    # Skip internal handlers
    if cls.__name__ in ("ExampleHandler", "UnknownHandler"):
        continue
    # Append name
    handlerList[cls.emoji] = cls.__name__
    # Create content...
        # Add style ref
    content = (
        "<head><link rel='stylesheet' href='../style/style.css'></link></head>\n## [**<**](..)\n"
    )
    # Title
    content += f"# `markmoji.handlers.{cls.__name__}`\n"
    # Add its docstring
    content += textwrap.dedent(cls.__doc__)
    # Add its example
    content += (
        f"\n"
        f"## Example\n"
        f"{cls.example}\n"
        f"\n"
    )
    # Add author
    author = markmoji.authors.authors[cls.__author__]
    authorName = f"{author.first_names[0]} {author.last_names[0]}"
    content += (
        f"## Author\n"
        f"{authorName} ({cls.__author__})\n"
    )
    # Save markdown file
    filename = handlersDir / (cls.__name__ + ".md")
    with open(str(filename), "w", encoding=encoding) as f:
        f.write(content)
# Create index for handlers
content = "<head><link rel='stylesheet' href='../style/style.css'></link></head>\n## [**<**](..)\n"
content += (
    "# Handlers\n"
    "Below are links to the handlers which Markmoji can use, and their corresponding emoji:\n"
    "\n"
)
for emoji, name in handlerList.items():
    content += f"- [{emoji}: {name}](./{name}.html)\n"
# Save handlers index
filename = handlersDir / "index.md"
with open(str(filename), "w", encoding=encoding) as f:
    f.write(content)

# Parse markdown
for file_md in rootDir.glob("**/*.md"):
    # Read markdown
    with open(str(file_md), "r", encoding=encoding) as f:
        content_md = f.read()
    # Parse markdown
    content_html = md.convert(content_md)
    # Save html
    file_html = file_md.parent / (file_md.stem + ".html")
    with open(str(file_html), "w", encoding=encoding) as f:
        f.write(content_html)
    