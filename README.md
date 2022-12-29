Markmoji extends the [basic markdown syntax](https://www.markdownguide.org/basic-syntax/) using an easy to understand and quickly readable emoji-based syntax, allowing you to create custom HTML elements from just an emoji, a label and a URL.

# The Syntax
Similar to how basic markdown indicates an image using an exclamation point before a link (`![name](url)`), markmoji syntax uses an emoji beore a link (`🐦[name](url)`), with the emoji dictating the type of HTML element created.

# Python function
To parse markmoji syntax, just use the function `markmoji.markmoji()` with your markdown text as the input. It will return the same text but with any markmoji syntax returned as HTML objects.

# Integration with [`python-markdown`](https://python-markdown.github.io/)
Included in the package are the necessary classes to use markmoji as an extension to `markdown.Markdown`. Here's an example of how you might do it:
```
import markmoji
import markdown as md

# Define some dummy content
content = "🏐[label1](link1)\n🏐[label2](link2)/n🐦[label3](link3)"
# Create markdown processor with markmoji
processor = md.Markdown(extensions=[markmoji.Markmoji()])
# Do actual markdown conversion
content = processor.convert(content)
```

# Implementations
Currently, the following emojis can be used to create the corresponding elements, using the `[label]` and `(url)` parts of the string as described:

| Emoji | Element | Label... | Url... |
| ----- | ------- | -------- | ------ |
| 🐦 | Embedded tweet | Not used | URL of the tweet to embed |
| 🏐 | Altmetric citation | Text citation | Article DOI |

# Contributing
This is all designed with open source contribution in mind! To add your own handlers, check out the file `handlers/handlers.py` to see the existing implementations and some instructions on how to add your own. It's not all that hard to do, I promise!