class BaseMarkmojiHandler:
    # The emoji handled by this handler, overload this when making your 
    # own markmoji handlers!
    emoji = "?"
    requirements = ""
    example = ""
    __author__ = ""

    def __init__(self, label:str, link:str, params:dict={}):
        """
        Base class for all markmoji handlers.

        Parameters
        ==========
        label : str
            The value in square brackets from the given markdown string
        link : str
            The value in round brackets from the given markdown string
        params : dict
            Dictionary of parameters from curly brackets in the given markdown string
        """
        self.label = label
        self.link = link
        self.params = params
    
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
        return f"<a href='{self.link}'{self.html_params}>{self.label}</a>"

    @property
    def md(self):
        """
        Output self as markdown.
        """
        if self.params:
            return f"{self.emoji}[{self.label}]({self.link}){{{self.params}}}"
        else:
            return f"{self.emoji}[{self.label}]({self.link})"
    
    @property
    def html_params(self):
        """
        Output own parameters as HTML <param> tags. Overload 
        when making your own markmoji handlers if you want 
        control over how parameters are handled!
        """
        output = ""
        # For each param, create a <param> tag
        for key, val in self.params.items():
            output += f" {key}={val}"
        
        return output

