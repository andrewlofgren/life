from life import Life
import toolbox

class Rules(object):

    ruleSets = {'basic': {'stayAlive': '23', 'comeAlive': '3'},
                'hard': {'stayAlive': '45', 'comeAlive': '5'},
                'impossible': {'stayAlive': '67', 'comeAlive': '6'},
                'peculiar': {'stayAlive': '36', 'comeAlive': '5'},}

    ruleSet = 'basic'

    stayAlive = ruleSets[ruleSet]['liveChar']
    comeAlive = ruleSets[ruleSet]['deadChar']

    @classmethod
    def set_display(cls, ruleSet):
        """
        Given a currentDisplaySet that is a key of the displaySets, change the
        liveChar and deadChar class variables to the corresponding values for that
        displayset.
        :param displaySet: A key to the displaySets
        :return: None
        """
        legalValues = cls.ruleSet.keys()
        if ruleSet in legalValues:
            cls.currentRuleSet = ruleSet
            cls.stayAlive = cls.ruleSets[ruleSet]['liveChar']
            cls.comeAlive = cls.ruleSets[ruleSet]['deadChar']
        else:
            raise ValueError(f'DisplaySet must be in {legalValues}.')

