class PropertyMaker(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        fields = set(x[4:] for x in cls.__dict__ if ('get_' in x))
        fields.update(x[4:] for x in cls.__dict__ if ('set_' in x))
        for field in fields:
            get_field = None
            set_field = None
            if 'get_' + field in cls.__dict__:
                get_field = cls.__dict__['get_' + field]
            if 'set_' + field in cls.__dict__:
                set_field = cls.__dict__['set_' + field]

            setattr(cls, field, property(fget=get_field, fset=set_field))
