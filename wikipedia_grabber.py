# wikipedia_grabber.py - takes a string and grabs a description from the string's English-language wiki page

import re,wikipedia

def get_description(message_content):

    # if there are no search results on Wikipedia for the message content, return an answer to that effect
    search_results = wikipedia.search(message_content)
    if not search_results:
        return "something I've never heard of."

    # get the first search result and look up the summary for it
    else:
        search_result = search_results[0]
        try:
            wiki_description = wikipedia.summary(search_result,auto_suggest=False)

            # find the description in the first sentence of the paragraph and remove the conjugated form of "be"
            description = re.search(' was [^\.]+\.| are [^\.]+\.| were [^\.]+\.| is [^\.]+\.', wiki_description).group()
            return re.sub('\A were |\A was |\A are |\A is ','', description)

        # if the page is a disambiguation, get the first result from the disambiguation page
        except wikipedia.exceptions.DisambiguationError as e:
            try:
                wiki_description = wikipedia.summary(re.sub('[()]','',e.options[0]))
                description = re.search(' was [^\.]+\.| are [^\.]+\.| were [^\.]+\.| is [^\.]+\.', wiki_description).group()
                return re.sub('\A were |\A was |\A are |\A is ','', description)

            # if that doesn't work (as seen in some very vague search terms), ask for more detail
            except AttributeError:
                return "a case where you'll have to be more specific."
