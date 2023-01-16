import markmoji
import webbrowser
import pytest
import markdown
from pathlib import Path


__folder__ = Path(__file__).parent


@pytest.mark.local_only
def test_examples():
    # Start off blank
    content = ""
    # Create 2 of everything
    for n in (1, 2):
        # Create example for each handler
        for cls in markmoji.handlers.map.values():
            # Append to content
            content += cls.example + "\n\n"
    # Setup processor
    processor = markdown.Markdown(extensions=["extra", markmoji.Markmoji()])
    # Process content
    content = processor.convert(content + "<footer>" + markmoji.authors.getCreditText() + "</footer>")
    # Save output
    outfile = __folder__ / "examples_local.html"
    with open(str(outfile), "w", encoding='utf-8') as f:
        f.write(content)
    # Open output
    webbrowser.open(str(outfile))
