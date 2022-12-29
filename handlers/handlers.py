from .base import BaseMarkmojiHandler


class ExampleHandler(BaseMarkmojiHandler):
    """
    Example handler, just to show you how to make one.

    Parameters
    ==========
    label : str
        The value in square brackets from the given markdown string
    link : str
        The value in round brackets from the given markdown string
    """

    emoji = "⬇️"

    @property
    def html(self):
        """
        By overloading the `.html` property, I can control what gets 
        outputted when this handler is translated to html
        """
        return f"<a href='{self.link}'>{self.label}</a>"


class UnknownHandler(BaseMarkmojiHandler):
    """
    Handler to use when format isn't recognised.

    Parameters
    ==========
    """

    emoji = "❓"

    @property
    def html(self):
        return f"{self.emoji}<a href='{self.link}'>{self.label}</a>"

    

class AltmetricHandler(BaseMarkmojiHandler):
    """
    Handler for an altmetric citation.

    Parameters
    ==========
    label : str
        Text citation
    link : str
        DOI link (if any)
    """
    # Volleyball emoji, because it looks a bit like the altmetric doughnuts
    emoji = "🏐"

    @property
    def html(self):
        return f"<altmetric-embed data-doi={self.link}>{self.label}</altmetric-embed>"


class TweetHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded tweet.

    Parameters
    ==========
    label : str
        Unused as embedded tweets don't have alt text
    link : str
        Link to the tweet to embed
    """
    # Bird emoji... because Twitter...
    emoji = "🐦"

    @property
    def html(self):
        return f"<blockquote class=twitter-tweet><a href='{self.link}'></a></blockquote>"