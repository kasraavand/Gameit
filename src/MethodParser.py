from datetime import datetime, date, time
import config
import json


class Parser:
    def __init__(self, *args, **kwargs):
        attr_path = config.arrtibutes_path
        self.raw_methods = self.load_raw_data(attr_path)

    def load_raw_data(self, attr_path):
        with open(attr_path) as f:
            raw_methods = json.load(f)
        return raw_methods

    def pars_attributes(self, attrs):
        def validate_scope(scp):
            if scp is not None:
                try:
                    scp = float(scp)
                except:
                    try:
                        scp = eval(scp)
                    except:
                        raise Exception("Undefined value for scope. {}".format(scp))
                finally:
                    return scp

        for attr in attrs:
            attr_type = attr['type']
            try:
                attr_type = __builtins__.__dict__[attr]
            except KeyError:
                if attr_type == 'datetime':
                    attr_type = datetime
                else:
                    attr_type = "UNDEFINED"
            scope = attr['scope']

            start, end = map(str.strip, scope.strip("()").split(','))
            scope = (validate_scope(start), validate_scope(end))
            yield {
                "type": attr_type,
                "scope": scope
            }

    def parse_method(self):
        for method in self.raw_methods:
            attributes = dict(self.pars_attributes(method['attributes']))
            method['attributes'] = attributes
            yield Method(**method)


class Method:
    def __init__(self, *args, **kwargs):
        self.attributes = kwargs['attributes']
        self.parent = kwargs['parent']
        self.description = kwargs['description']

    def __getattribute__(self, name):
        try:
            attr = self.attributes[name]
        except KeyError:
            raise
        else:
            return attr[name]
