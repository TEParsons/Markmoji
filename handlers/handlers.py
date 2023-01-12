import re

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
    __author__ = "🦊"

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
    __author__ = "🦊"

    @property
    def html(self):
        return f"{self.emoji}<a href='{self.link}'>{self.label}</a>"


# --- From here on in, keep it alphabetical! ---


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
    __author__ = "🦊"

    @property
    def html(self):
        return f"<altmetric-embed data-doi={self.link}>{self.label}</altmetric-embed>"


class TootHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded toot (from Mastodon).

    Parameters
    ==========
    label : str
        Unused as embedded toots don't have alt text
    link : str
        Link to the toot to embed
    """
    # Elephant emoji, like what everyone's got on their Twitter usernames
    emoji = "🐘"
    __author__ = "🦊"

    @property
    def html(self):
        link = self.link
        # Make sure we're using the /embed link
        _, embed = re.match("(https?://)?[\w\d]*\.com/@[\w\d]*/\d*(/embed)?", link).groups()
        if embed is None:
            link += "/embed"
        # Construct iframe
        return f"<iframe src='{self.link}' class='mastodon-embed'></iframe><script src='https://toot.wales/embed.js' async='async'></script>"


class TweetHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded tweet.

    Parameters
    ==========
    label : str
        Unused as embedded tweets don't have alt text
    link : str
        Link to the tweet to embed, or its ID
    """
    # Bird emoji... because Twitter...
    emoji = "🐦"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<blockquote class=twitter-tweet><a href='{self.link}'></a></blockquote><script async src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>"


class YouTubeHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded YouTube video.

    Parameters
    ==========
    label : str
        Alt text for the embedded video
    link : str
        Link to the video to embed
    """
    # The ol' YouTube play button
    emoji = "▶️"
    __author__ = "🦊"

    @property
    def html(self):
        # Get video ID from link
        match = re.match("^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*", self.link)
        if match:
            video_id = match.groups()[-1]
        else:
            video_id = self.link

        return f"<iframe src='https://www.youtube.com/embed/{video_id}' title='{self.label}' allowfullscreen></iframe>"
