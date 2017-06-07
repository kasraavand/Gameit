from datetime import datetime, date, time
import json
from models import Importer


class Parser:
    def __init__(self, *args, **kwargs):
        method_path = kwargs['method_path']
        self.raw_methods = self.load_raw_data(method_path)
        self.importer = Importer(db_name=kwargs['db_name'])

    def load_raw_data(self, method_path):
        with open(method_path) as f:
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

        for attr_name, attr in attrs.items():
            attr_type = attr['type']
            try:
                attr_type = __builtins__[str(attr)]
            except KeyError:
                if attr_type == 'datetime':
                    attr_type = datetime
                else:
                    attr_type = "UNDEFINED"
            try:
                start, end = attr['scope']
                scope = (validate_scope(start), validate_scope(end))
            except (KeyError, ValueError):
                yield attr_name, {
                    "type": attr_type,
                }
            else:
                yield attr_name, {
                    "type": attr_type,
                    "scope": scope

                }

    def parse_method(self):
        # Create method object.
        for name, method in self.raw_methods.items():
            attributes = dict(self.pars_attributes(method['attributes']))
            method['attributes'] = attributes
            yield Method(name, **method)

    def pickle_methods(self):
        pass


class Method:
    def __init__(self, *args, **kwargs):
        attributes = kwargs.pop('attributes')
        method = self.importer.get_method(self, kwargs['parent_type'],
                                          kwargs['parent_id'], kwargs['method_name'])
        self.name = args[0]
        self.__dict__.update(kwargs)
        self.__dict__.update(attributes)

    def __getattribute__(self, name):
        if name.endswith('id'):
            name = name.strip("_id")
        elif not name.startswith("__") and name != 'name':
            method = self.importer.import_method(self.)
        return object.__getattribute__(self, name)

    def __len__(self):
        return 3
