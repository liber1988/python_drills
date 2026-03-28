def eot_new(): return 'EOT NEW'

def deprecated3(message, eot_new):
    def dicorator(func):
        def wrapper(*args, **kwargs):
            print(message.format(func=func))
            return eot_new(*args, **kwargs)
        return wrapper
    return dicorator

@deprecated3('using eot_new not {func.__name__}', eot_new)
def eot(): return 'EOT'


eot()