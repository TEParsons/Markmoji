try:
    from pybtex.database import Person
except ImportError:
    class Person:
        """
        If Pybtex isn't installed, use this placeholder object which has enough attributes that 
        markmoji doesn't break.
        """
        def __init__(self, string='', first='', middle='', prelast='', last='', lineage=''):
            self.first_names = [first]
            self.middle_names = [middle] + [prelast]
            self.last_names = [last]
            self.lineage = lineage

# Emojis representing authors, pick something fun!
authors = {
    "🦊": Person(first="Todd", middle="Ethan", last="Parsons"),
}

def getCreditText():
    from .handlers.map import map

    # Array to store accreditations in
    refs = {}
    for handler in map.values():
        # Get author object
        author = handler.__author__
        # Add author to accreditations list if not already present
        if author not in refs:
            refs[author] = " "
        # Add credit
        refs[author] += handler.emoji + " "
    # Write preface
    txt = (
        "Markmoji by Todd Parsons.\n"
        "\n"
        "Handlers by:\n"
    )
    # Add credit for each handler
    for author, credit in refs.items():
        author = authors.get(author, authors["🦊"])
        # Format name
        name = f"{author.first_names[0]} {author.last_names[0]}"
        # Construct line
        line = f"{name} ({credit})\n"
        # Append
        txt += line
    
    return txt
