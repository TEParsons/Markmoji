import markmoji


def test_author_names():
    for cls in markmoji.handlers.map.values():
        assert cls.__author__ in markmoji.authors.authors, (
            f"Class {cls.__name__} is authored by '{cls.__author__}', but no such author exists in "
            f"`markmoji.authors.authors`. "
        )
