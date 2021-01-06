"""

Converts domain text variables into lists of Facet class objects

"""

from modules.domain_texts import domain_text_array

class Facet(object):
    
    def __init__(self, _name, _description, _lowDescript, _highDescript):
        self.name = _name
        self.description = _description[0].upper() + _description[1:]
        _lowDescript = _lowDescript[0].upper() + _lowDescript[1:]
        _highDescript = _highDescript[0].upper() + _highDescript[1:]
        self.scale = [_lowDescript, _highDescript]

    def __str__(self):
        return '{self.name}: {self.describe}'.format(self=self)


def processDomainText(text):
    facetList = []
    for facetText in text.split("\n\n"):
        facetList.append(processFacetText(facetText))
    return facetList

def processFacetText(text):
    txt = text.split("\n")
    return Facet(txt[0], txt[1], txt[2], txt[3])



# MODULE EXPORTS 
domains = [processDomainText(dt) for dt in domain_text_array]
domain_names = ['Honesty-Humility', 'Emotionality', 'eXtraversion', 'Agreeableness', 'Conscientiousness', 'Openess to Experience']
domain_descriptions = ["Avoid manipulating others for personal gain, feel little temptation to break rules, are uninterested in lavish wealth and luxuries, and feel no special entitlement to elevated social status",
                       "Experience fear of physical dangers, experience anxiety in response to life's stresses, feel a need for emotional support from others, and feel empathy and sentimental attachments with others",
                       "Feel positively about themselves, feel confident when leading or addressing groups of people, enjoy social gatherings and interactions, and experience positive feelings of enthusiasm and energy",
                       "Forgive the wrongs that they suffered, are lenient in judging others, are willing to compromise and cooperate with others, and can easily control their temper",
                       "Organize their time and their physical surroundings, work in a disciplined way toward their goals, strive for accuracy and perfection in their tasks, and deliberate carefully when making decisions",
                       "Become absorbed in the beauty of art and nature, are inquisitive about various domains of knowledge, use their imagination freely in everyday life, and take an interest in unusual ideas or people"]


## Deprecated function? ... Was not used in original master script
#def getDomainText(domain_idx, value):
#    domain = domains[domain_idx]
#    facets = [facet.scale[value] for facet in domain]
#    return '\n'.join(facets)