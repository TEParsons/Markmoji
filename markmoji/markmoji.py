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
            # Keep track of whether we're in a code block
            inLiteral = False
            # Iterate through lines
            new_lines = []
            classes_used = []
            for line in lines:
                # If code block opener is found, toggle literal
                if "```" in line:
                    inLiteral = not inLiteral
                if not inLiteral:
                    # Process markmoji syntax on line
                    new_line, cls = markmoji(line)
                else:
                    # If we're in literal, keep line as is
                    new_line, cls = line, []
                # Add processed line
                new_lines.append(new_line)
                # Add class(es) used
                classes_used += cls
            # Prepend <head> with class requirements
            prefix = []
            for cls in set(classes_used):
                # Add requirement for each class used
                if "\n" in cls.requirements:
                    prefix += cls.requirements.split("\n")
                elif cls.requirements:
                    prefix += [cls.requirements]
            return prefix + new_lines
    
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
    # Keep track of classes used
    classes_used = []
    def _objectify(match):
        # Split match into emoji, label and link
        escaped = match.group(1)
        emoji = match.group(2)
        label = match.group(3)
        link = match.group(4)
        # If escaped, return unescaped & unprocessed
        if escaped:
            return f"{emoji}[{label}]({link})"
        # Find correct class from map of classes
        cls = map.get(emoji, handlers.UnknownHandler)
        # Create object
        obj = cls(label=label, link=link)
        # Mark this class as used
        if cls not in classes_used:
            classes_used.append(cls)
        # Return object as HTML
        return obj.html
    emojis = "|".join(list(map))
    content = re.sub(
        f"(?<!`)(\\\\)?({emojis})\[([^\]]*)\]\(([^\)]*)\)(?!`)", 
        _objectify, content)

    return content, classes_used