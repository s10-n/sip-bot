# wikipedia_grabber.py - takes a string and grabs a description from the string's English-language wiki page

import re
import wikipedia

def get_description(message_content):
    search_results = wikipedia.search(message_content)
    if not search_results:
        return "something I've never heard of."
    else:
        search_result = search_results[0]
        try:
            wiki_description = wikipedia.summary(search_result)
            description = re.search(' was [^\.]+\.| are [^\.]+\.| were [^\.]+\.| is [^\.]+\.', wiki_description).group()
            return re.sub('\A were |\A was |\A are |\A is ','', description)
        except wikipedia.exceptions.DisambiguationError as e:
            try:
                wiki_description = wikipedia.summary(re.sub('[()]','',e.options[0]))
                description = re.search(' was [^\.]+\.| are [^\.]+\.| were [^\.]+\.| is [^\.]+\.', wiki_description).group()
                return re.sub('\A were |\A was |\A are |\A is ','', description)
            except AttributeError:
                return "a case where you'll have to be more specific."
