<head><link rel='stylesheet' href='../style/style.css'></link></head>
## [**<**](..)
# `markmoji.handlers.TumblrPostHandler`

Handler for an embedded Tumblr post

### Parameters
label (str)
:    Unused as embedded Tumblr posts don't have alt text

link (str)
:    Link to the post to embed (format should be `{username}.tumblr.com/post/{numeric id}/whatever-else-it-doesn't-matter`)

## Example
### Markdown:
```
ⓣ<https://tinyleavesdream.tumblr.com/post/663071895596548096>
```
### Result:
ⓣ<https://tinyleavesdream.tumblr.com/post/663071895596548096>

## Author
Todd Parsons (🦊)
