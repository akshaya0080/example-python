# test_corenlp.py

# test_corenlp.py

from nlplogic.corenlp import (  # pylint: disable=unused-import
    search_wikipedia,
    summarize_wikipedia,
    get_text_blob,
    get_phrases
)



def test_get_phrase():
    assert 'golden state' in get_phrases("Golden State Warriors")

              