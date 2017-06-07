from collections.abc import Mapping
from functools import reduce
from models import DataModel


class GetMethod(Mapping):
    def __init__(self, *args, **kwargs):
        self.data_model = DataModel(db_name=kwargs['db_name'])
        self.parent_id = kwargs['parent_id']
        self.method_id = kwargs['method_id']
        self.methods_meta_info = self.data_model.get_method_meta()

    def __getitem__(self, names):
        try:
            base_name = names.pop(0)
            base_method_info = self.methods_meta_info[base_name]
            parent = base_method_info['parent']
            base_method = self.data_model.get_method(parent, self.parent_id,
                                                     base_name, self.method_id)

            # Since we can assign multiple method object based on different
            # events to each method name under a particular parent_id
            # when in a rule we are using a parent_method_id which actually is
            # demonstrating a method name under a parent type (for
            # example user_payback) this method cannot have different ids or
            # parent ids. For example if a method has been activated
            # at a special time and we added this onther the user_id x and
            # method name payback. THen this particular payback method
            # can only has one pay_request_id.
            def get_attrs(names, method):
                while True:
                    name = names.pop(0)
                    if name.endswith('id'):
                        parent, method_name = name.split('_')[:2]
                        method_inf = next(mtd for mtd in method['linked_methods'] if mtd['parent']==parent and mtd['method']==method_name)
                        method_id, parent_id = method_inf['id'], method_inf['parent_id']
                        method = self.data_model.get_method(parent, parent_id,
                                                            method_name, method_id)
                        return get_attrs(names, method)
                    else:
                        return method['name']

            return get_attrs(names, base_method)


        except KeyError:
            # should be handled properly
            # print (self._all_methods)
            raise

    def __iter__(self):
        return iter(self._all_methods)

    def __len__(self):
        return len(self._all_methods)
