
class Rules(object):

    ruleSets = {'basic': {'stayAlive': '23', 'comeAlive': '3'},
                'hard': {'stayAlive': '45', 'comeAlive': '5'},
                'impossible': {'stayAlive': '67', 'comeAlive': '6'},
                'peculiar': {'stayAlive': '36', 'comeAlive': '5'},}

    ruleSet = 'basic'

    stayAlive = ruleSets[ruleSet]['stayAlive']
    comeAlive = ruleSets[ruleSet]['comeAlive']

    @classmethod
    def set_rules(cls, ruleSet):
        """
        Using classmethod set the current display set
        Using classmethod set the current display set
        and be able to change it
        :param displaySet: chosen set of characters that
        are printed during simulation
        :return: none
        """
        legalValues = cls.ruleSets.keys()
        if ruleSet in legalValues:
            cls.ruleSet = ruleSet
            cls.stayAlive = cls.ruleSets[ruleSet]['stayAlive']
            cls.comeAlive = cls.ruleSets[ruleSet]['comeAlive']
        elif ruleSet == 'choice':
            cls.stayAlive = input('How many neighbors do you want your cell to have to survive? ')
            cls.comeAlive = input('How many neighbors do you want your cell to have to be born? ')
        else:
            raise ValueError(f'RuleSet must be in {legalValues}.')

