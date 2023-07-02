# v1.3.0
### New handlers
- Readmore (↕): A summary/details pair of HTML objects.
- Google Material icon (⚇): An icon from the Google Material set

# v1.2.1
### Bug fixes
- Oops! I doinked up the packaging and the entire handlers folder wasn't included... 😅
- I'd also made a very silly typo in the version

# v1.2
### Syntax changes
- Additional attributes can now be specified using curly braces - full Markdown syntax isn't yet supported (can't use # for id or . for class), but anything in dict-like format is fine (e.g. {class: my-class})
- Emojis can now be specified using :emoji: syntax, as in the emoji Python module
### New handlers
- Tables (🔢): An HTML table from a CSV file.
- Soundcloud sound (🌧️): An embedded SoundCloud sound.
- LinkedIn post (📠): An embedded LinkedIn post.
- IPA pronunciation guide (🗣️): Format text written in International Phonetic Alphabet, adding a link to ipa-reader.xyz

# v1.1
### New handlers
- GoogleMapsHandler (📍): Embed a Google Maps map. For now, has to be the link provided by the "Embed HTML" feature in the Share menu.
- HexmapHandler (⬢): For creating a hexagonal map using tiles from Cuddly Clover on itch.io.

# v1.0
## 🎉The first release of Markmoji! 🎉
Markmoji extends the basic markdown syntax using an easy to understand and quickly readable emoji-based syntax, allowing you to create custom HTML elements from just an emoji, a label and a URL.