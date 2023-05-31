from .handlers import handlers, map
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re
import emoji


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
        paramStr = match.group(5) or ""
        # Find correct class from map of classes
        cls = map.get(emoji, handlers.UnknownHandler)
        # Process params
        params = {}
        for pair in paramStr.split(","):
            # Skip invalid pairs
            if ":" not in pair:
                continue
            # Add valid pairs
            key, val = pair.split(":", maxsplit=1)
            params[key] = val.strip()
        # Create object
        obj = cls(label=label, link=link, params=params)
        # If escaped, return unescaped & unprocessed
        if escaped:
            return obj.md
        # Mark this class as used
        if cls not in classes_used:
            classes_used.append(cls)
        # Return object as HTML
        return obj.html
    # Make list of emojis
    emojis = "|".join(list(map))
    # Convert :emoji: syntax
    content = emoji.emojize(content)
    # Replace syntax with corresponding object
    content = re.sub((
        f"(?<!`)"  # not after code markers
        f"(\\\\)?({emojis})"  # starts with an emoji (match 2)
        f"\[([^\]]*)\]"  # something in square brackets (match 3)
        f"\(([^\)]*)\)"  # something in round brackets (match 4)
        f"(?:\{{([^\}}]*)\}})?"  # something in curly brackets (match 5) (optional)
        f"(?!`)"
    ), _objectify, content)

    return content, classes_used