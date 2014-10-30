def import_it(name):
        mods = name.split('.')
        clz = None
        try:
            result = __import__(name)
        except:
            thing = '.'.join(mods[:-1])
            result = __import__(thing)
            clz = mods[-1]
            mods = mods[:-1]
        for mod in mods[1:]:
            result= getattr(result,mod)
        if clz is not None:
            result = getattr(result,clz)
        return result
