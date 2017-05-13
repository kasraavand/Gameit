import config
import json


class Parser:
    def __init__(self, *args, **kwars):
        self.attrs = self.load_attrs()
        _attr_keys = config.attr_keys
        self.attr_parent = _attr_keys['parent']
        self.attr_type = _attr_keys['type']
        self.attr_scope = _attr_keys['scope']

    def load_attrs(self):
        with open('attrs.json') as f:
            return json.load(f)
