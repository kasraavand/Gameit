from src.RuleParser import Rule
import json
import pickle


class Rule(Rule):
    def __init__(self, *args, **kwargs):
        super()
        self.method_path = kwargs['method_path']
        self.rules_path = kwargs['rules_path']
        self.raw_rules = self.load_rules()

    def callattr(self, attrs):
        return self.method_getter[attrs]

    def load_rules(self):
        with open(self.rules_path) as f:
            raw_rules = json.load(f)
        return raw_rules

    def create_functions(self):
        for name, rule in self.raw_rules.items():
            rule = Rule(name=name,
                        method_path=self.method_path,
                        **rule)

        with open('functions/func.pickle', 'wb') as f:
            pickle.dump(rule, f, -1)
