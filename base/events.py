class EventDispatcher:
    def __init__(self):
        self.__funcs = {}

    def emit(self, eid:int, args:tuple=None, kwargs:dict=None):
        if eid not in self.__funcs:
            return
        
        for func in self.__funcs[eid]:
            if args and kwargs:
                func(*args, **kwargs)
            
            elif args:
                func(*args)

            elif kwargs:
                func(**kwargs)
            
            else:
                func()

    def connect(self, eid:int, func):
        if eid not in self.__funcs:
            self.__funcs[eid] = []

        self.__funcs[eid].append(func)