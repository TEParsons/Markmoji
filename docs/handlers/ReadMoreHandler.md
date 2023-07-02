<head><link rel='stylesheet' href='../style/style.css'></link></head>
## [**<**](..)
# `markmoji.handlers.ReadMoreHandler`

Handler for a summary/details pair of HTML objects.

### Parameters
label (str)
:   Content to go inside the <summary> tag (always shown)

link (str)
:   Content to go inside the <details> tag (hidden until clicked)

## Example
### Markdown:
```
↕[This text will always be shown.](This text will only be visible)
```
### Result:
↕[This text will always be shown.](This text will only be visible)

## Author
Todd Parsons (🦊)
