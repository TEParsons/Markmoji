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
    # Pick an emoji to represent this handler, it should be something memorable and intuitive!
    emoji = "⬇️"
    # Give us an example usage (for the documentation)
    example = "⬇️[Google](https://google.com)"
    # Give yourself credit! Assign yourself an emoji in ../authors.py and cite it here
    __author__ = "🦊"

    @property
    def html(self):
        """
        By overloading the `.html` property, I can control what gets 
        outputted when this handler is translated to html
        """
        return f"<a href='{self.link}'>{self.label}</a>"


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

    example = "🏐[Mather, G., Sharman, R. J., & Parsons, T. (2017). Visual adaptation alters the apparent speed of real-world actions. *Scientific reports, 7*(1), 1-10.](10.1038/s41598-017-06841-5)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<altmetric-embed data-doi={self.link}>{self.label}</altmetric-embed>"


class FacebookPostHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded post (from Facebook).

    Parameters
    ==========
    label : str
        Unused as embedded posts don't have alt text
    link : str
        Link to the post to embed
    """
    # F in a square looks like the facebook logo
    emoji = "🅵"

    example = "🅵[Barack Obama announces presidential run (2008)](https://www.facebook.com/TheXKCD/posts/pfbid0KZZoxocUJYYE8NnZUHtpDkmr7Jw1qpMBE4QpFKBNBMVJByNX9iPctUfpRCmCwCiMl)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<iframe src='https://www.facebook.com/plugins/post.php?href={self.link}'></iframe>"


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

    example = "🐘[God has a point](https://universeodon.com/@TheTweetOfGod/109597493614530062)"
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


class TumblrPostHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded Tumblr post

    Parameters
    ==========
    label : str
        Unused as embedded Tumblr posts don't have alt text
    link : str
        Link to the post to embed (format should be `{username}.tumblr.com/post/{numeric id}/whatever-else-it-doesn't-matter`)
    """

    emoji = "ⓣ"

    example = "ⓣ[Some cute spooky pokémon](https://tinyleavesdream.tumblr.com/post/663071895596548096)"
    __author__ = "🦊"

    @property
    def html(self):
        # Get username and post id from link
        _, username, post_id, _ = re.match("(https?://)?([\w\d-_]*)\.tumblr\.com/post/(\d*)(/.*)?", self.link).groups()
        # Construct holder
        return f"<div class='tumblr-post' data-href='https://embed.tumblr.com/embed/post/{username}/{post_id}'><a href='{self.link}'></a></div>  <script async src='https://assets.tumblr.com/post.js'></script>"


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

    example = "🐦[Ed Balls.](https://twitter.com/edballs/status/63623585020915713)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<blockquote class=twitter-tweet><a href='{self.link}'></a></blockquote><script async src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>"


class UnknownHandler(BaseMarkmojiHandler):
    """
    Handler to use when format isn't recognised.

    Parameters
    ==========
    """

    emoji = "❓"

    example = "❓[Google](https://google.com)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"{self.emoji}<a href='{self.link}'>{self.label}</a>"


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

    example = "▶️[Ten Hours of Nick Offerman's Yule Log](https://www.youtube.com/watch?v=IQpW5sG5bg8)"
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
