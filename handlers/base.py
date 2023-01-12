class BaseMarkmojiHandler:
    # The emoji handled by this handler, overload this when making your 
    # own markmoji handlers!
    emoji = "?"
    __author__ = ""

    def __init__(self, label:str, link:str):
        """
        Base class for all markmoji handlers.

        Parameters
        ==========
        label : str
            The value in square brackets from the given markdown string
        link : str
            The value in round brackets from the given markdown string
        """
        self.label = label
        self.link = link
    
    def __str__(self):
        """
        Calls to str(obj) will return self as html
        """
        return self.html
    
    @property
    def html(self):
        """
        Output self as a HTML tag. Overload this 
        when making your own markmoji handlers!
        """
        return f"<a href='{self.link}'>{self.label}</a>"

    @property
    def md(self):
        """
        Output self as markdown.
        """
        return f"{self.emoji}[{self.label}]({self.link})"