import copy

def get_args_dict(argv):
    args = {}
    arguments =  copy.deepcopy(argv)
    arguments.pop(0)
    while len(arguments)>1:
        key = arguments.pop(0)
        value = arguments.pop(0)
        args[key] = value
    return args