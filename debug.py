#!/usr/bin/env python3.7

def odump(obj, no_dunder=True, whelp=False):
    """Dump attributes of an object with values, somewhat similar to PHP's print_r"""
    import builtins
    builtin_types = [ty for ty in builtins.__dict__.values() if isinstance(ty, type)]
    print(type(obj))
    if type(obj) not in builtin_types and hasattr(obj, '__doc__') and getattr(obj, '__doc__'):
        print(getattr(obj, '__doc__'))
        print()
    for attr in dir(obj):
        if no_dunder and attr.startswith('__'):
            continue
        oattr = getattr(obj, attr)
        if hasattr(oattr, '__class__'):
            tdesc = f'({oattr.__class__.__name__})'
        else:
            tdesc = f'({str(type(attr))})'
        if callable(oattr):
            soattr = '<function or method>'
            tdesc = ''
        else:
            try:
                soattr = str(oattr)
                if not soattr:
                    soattr = "''"
            except TypeError as exc:
                # Some objects return wrong (non-string) results for str() call,
                # (raising exception like "TypeError: __str__ returned non-string (type list)")
                soattr = f'ERROR: string representation of an attribute could not be computed ({exc}))'
        print(f'.{attr:20} = {soattr:5} {tdesc}', end='')
        if whelp and hasattr(oattr, '__doc__') and getattr(oattr, '__doc__'):
            if type(oattr) in builtin_types:
                print(f' (builtin)')
            else:
                print(f"\n {getattr(oattr, '__doc__')}\n")

"""
odump example:
        

class ACME:

    __doc__ = 'A company that makes everything for coyotes worldwide.'

    factories = 150

    def __init__(self, main_customer='Wile E. Coyote', product1=None):
        self._main_customer = main_customer
        self.product1 = product1

    @classmethod
    def how_many(cls):
        "Brag how many factories are owned by ACME"
        return cls.factories


company = ACME(product1='rocket')
odump(company, whelp=True)

<class '__main__.ACME'>
A company that makes everything for coyotes worldwide.

._main_customer       = Wile E. Coyote (str) (builtin)
.factories            = 150   (int) (builtin)
.how_many             = <function or method> 
 Brag how many factories are owned by ACME

.product1             = rocket (str) (builtin)
"""

if __name__ == '__main__':
    class ACME:

        __doc__ = 'A company that makes everything for coyotes worldwide.'

        factories = 150

        def __init__(self, main_customer='Wile E. Coyote', product1=None):
            self._main_customer = main_customer
            self.product1 = product1

        @classmethod
        def how_many(cls):
            "Brag how many factories are owned by ACME"
            return cls.factories

    company = ACME(product1='rocket')
    odump(company, whelp=True)