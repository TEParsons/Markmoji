# Base Python
import re
from pathlib import Path
# Packages (must be specified in requirements.txt)
import requests
import validators
# Relative imports
from .base import BaseMarkmojiHandler


class ExampleHandler(BaseMarkmojiHandler):
    """
    Example handler, just to show you how to make one.

    ### Parameters
    label (str)
    :    The value in square brackets from the given markdown string

    link (str)
    :    The value in round brackets from the given markdown string
    """
    # Pick an emoji to represent this handler, it should be something memorable and intuitive!
    emoji = "⬇️"
    # Anything which needs to be in <head> goes here, they will only be included once even if you have multiple markmojis
    requirements = "<script>console.log('hello world!')</script>"
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

    ### Parameters
    label (str)
    :    Text citation

    link (str)
    :    DOI link (if any)
    """
    # Volleyball emoji, because it looks a bit like the altmetric doughnuts
    emoji = "🏐"
    requirements = "<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>"

    example = "🏐[Mather, G., Sharman, R. J., & Parsons, T. (2017). Visual adaptation alters the apparent speed of real-world actions. <i>Scientific reports, 7</i>(1), 1-10.](10.1038/s41598-017-06841-5)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<div class='altmetric-citation'><div class='altmetric-embed' data-badge-type='donut' data-doi='{self.link}'></div><span>{self.label}</span></div>"


class FacebookPostHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded post (from Facebook).

    ### Parameters
    label (str)
    :    Unused as embedded posts don't have alt text

    link (str)
    :    Link to the post to embed
    """
    # F in a square looks like the facebook logo
    emoji = "🅵"

    example = "🅵[Funny comic](https://www.facebook.com/TheXKCD/posts/pfbid0KZZoxocUJYYE8NnZUHtpDkmr7Jw1qpMBE4QpFKBNBMVJByNX9iPctUfpRCmCwCiMl)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<iframe src='https://www.facebook.com/plugins/post.php?href={self.link}' class=facebook-embed></iframe>"


class InstagramPostHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded Instagram post.

    ### Parameters
    label (str)
    :    Unused as embedded posts don't have alt text

    link (str)
    :    Link to the post to embed
    """

    emoji = "📷"
    requirements = "<script async src='//www.instagram.com/embed.js'></script>"

    example = "📷[OSR RPG cover by Kim Dias Holm](https://www.instagram.com/p/CkYXXhlt5N7)"
    __author__ = "🦊"

    @property
    def html(self):
        _, _, post_id = re.match("(https?://)?(www\.)?instagram\.com/p/([\w\d]*)", self.link).groups()

        return f"<blockquote class='instagram-media' data-instgrm-captioned data-instgrm-permalink='https://www.instagram.com/p/{post_id}/?utm_source=ig_embed&amp;utm_campaign=loading' data-instgrm-version='14'><a href='https://www.instagram.com/p/{post_id}/?utm_source=ig_embed&amp;utm_campaign=loading'>{self.label}</a></blockquote>"


class HexmapHandler(BaseMarkmojiHandler):
    """
    Handler for creating a hexagonal map using tiles from 
    [Cuddly Clover on itch.io](https://cuddlyclover.itch.io/fantasy-hex-tiles).

    ### Parameters
    label (str)
    :    Title for the map

    file (str)
    :    Path or link to a csv file created via [Hexmap by Todd Parsons](https://teparsons.github.io/Hexmap/)
    """
    # Elephant emoji, like what everyone's got on their Twitter usernames
    emoji = "⬢"
    requirements = "<script src='https://teparsons.github.io/Hexmap/hex.js' async='async'></script>"

    example = "⬢[Kashar](https://teparsons.github.io/Iuncterra/assets/locations/kashar/Kashar.csv)"
    __author__ = "🦊"

    @property
    def html(self):
        # Load data
        if validators.url(self.link):
            data = requests.get(self.link).text
        elif Path(self.link).is_file():
            data = Path(self.link).read_text()
        else:
            data = "[]"
        # Construct hexmap
        return (
            f"<h3>{self.label}</h3>\n"
            f"<hex-grid data-tiles='{data}' data-readonly></hex-grid>\n"
        )


class TootHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded toot (from Mastodon).

    ### Parameters
    label (str)
    :    Unused as embedded toots don't have alt text

    link (str)
    :    Link to the toot to embed
    """
    # Elephant emoji, like what everyone's got on their Twitter usernames
    emoji = "🐘"
    requirements = "<script src='https://toot.wales/embed.js' async='async'></script>"

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
        return f"<iframe src='{link}' class='mastodon-embed'></iframe>"


class TumblrPostHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded Tumblr post

    ### Parameters
    label (str)
    :    Unused as embedded Tumblr posts don't have alt text

    link (str)
    :    Link to the post to embed (format should be `{username}.tumblr.com/post/{numeric id}/whatever-else-it-doesn't-matter`)
    """

    emoji = "ⓣ"
    requirements = "<script async src='https://assets.tumblr.com/post.js'></script>"

    example = "ⓣ[Some cute spooky pokémon](https://tinyleavesdream.tumblr.com/post/663071895596548096)"
    __author__ = "🦊"

    @property
    def html(self):
        # Get username and post id from link
        _, username, post_id, _ = re.match("(https?://)?([\w\d\-_]*)\.tumblr\.com/post/(\d*)(/.*)?", self.link).groups()
        # Construct holder
        return f"<div class='tumblr-post' data-href='https://embed.tumblr.com/embed/post/{username}/{post_id}'><a href='{self.link}'></a></div>"


class TweetHandler(BaseMarkmojiHandler):
    """
    Handler for an embedded tweet.

    ### Parameters
    label (str)
    :    Unused as embedded tweets don't have alt text

    link (str)
    :    Link to the tweet to embed
    """
    # Bird emoji... because Twitter...
    emoji = "🐦"
    requirements = "<script async src='https://platform.twitter.com/widgets.js' charset='utf-8'></script>"

    example = "🐦[Ed Balls.](https://twitter.com/edballs/status/63623585020915713)"
    __author__ = "🦊"

    @property
    def html(self):
        return f"<blockquote class=twitter-tweet><a href='{self.link}'></a></blockquote>"


class UnknownHandler(BaseMarkmojiHandler):
    """
    Handler to use when format isn't recognised.

    ### Parameters
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

    ### Parameters
    label (str)
    :    Alt text for the embedded video

    link (str)
    :    Link to the video to embed
    """
    # The ol' YouTube play button
    emoji = "▶️"

    example = "▶️[They're taking the hobbits to Isengard!](https://www.youtube.com/watch?v=jfKfPfyJRdk)"
    __author__ = "🦊"

    @property
    def html(self):
        # Get video ID from link
        match = re.match("^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*", self.link)
        if match:
            video_id = match.groups()[-1]
        else:
            video_id = self.link

        return f"<iframe src='https://www.youtube.com/embed/{video_id}' title='{self.label}' class='youtube-embed' allowfullscreen></iframe>"
