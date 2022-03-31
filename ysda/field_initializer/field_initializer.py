from inspect import signature


class FieldInitializer(type):

    def __setattr__(cls, attr, value):
        cls.__dict__[attr] = value

    def __call__(cls, *args, **kwargs):
        sig = signature(cls.__init__)
        call_kwargs = dict()
        if "__init__" in cls.__dict__:
            for param in sig.parameters.values():
                if param.name in kwargs:
                    call_kwargs[param.name] = kwargs[param.name]

        temp_object = super().__call__(*args, **call_kwargs)
        for item in kwargs:
            if hasattr(temp_object, item):
                pass
            else:
                temp_object.__dict__[item] = kwargs[item]
        return temp_object
