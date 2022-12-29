from .handlers import handlers, map
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re


class Markmoji(Extension):
    """
    Markdown extension to link the markmoji preprocessor
    """
    class MarkmojiPreprocessor(Preprocessor):
        """
        Markdown preprocessor using markmoji
        """
        def run(self, lines):
            # Iterate through lines
            new_lines = []
            for line in lines:
                # Process markmoji syntax on line
                new_line = markmoji(line)
                # Add processed line
                new_lines.append(new_line)
            return new_lines
    
    def extendMarkdown(self, md):
        # Register as extension
        md.registerExtension(self)
        # Register preprocessor
        md.preprocessors.register(self.MarkmojiPreprocessor(md.parser), 'markmoji', 175)


def markmoji(content:str):
    """
    The thing that does the stuff...

    Set this function as your preprocessor 
    when using markdown to unlock the markmoji 
    syntax
    """
    
    def _objectify(match):
        # Split match into emoji, label and link
        emoji = match.group(1)
        label = match.group(2)
        link = match.group(3)
        # Find correct class from map of classes
        cls = map.get(emoji, handlers.UnknownHandler)
        # Create object
        obj = cls(label=label, link=link)
        # Return object as HTML
        return obj.html
    
    content = re.sub(f"({'|'.join(list(map))})\[(.*)\]\((.*)\)", _objectify, content)

    return content