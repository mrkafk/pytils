#!/usr/bin/env python3.7

def odump(obj, no_dunder=True, whelp=False):
    """Dump attributes of an object with values, somewhat similar to PHP's print_r."""

    if whelp:
        import builtins
        builtin_types = [ty for ty in builtins.__dict__.values() if isinstance(ty, type)]
    if whelp and hasattr(obj, '__doc__'):
        r = repr(obj)
        print(r)
        print(getattr(obj, '__doc__'))
        print(f'\n == Attributes of {r}: ==\n')
    for attr in dir(obj):
        if no_dunder and attr.startswith('__'):
            continue
        oattr = getattr(obj, attr)
        print(f'--> obj.{attr} = {repr(oattr)}')
        if whelp and hasattr(oattr, '__doc__'):
            if type(oattr) in builtin_types:
                print(f'builtin: {type(oattr)}')
            else:
                print(getattr(oattr, '__doc__'))
            print()

"""
    odump example:
        
    class ACME:
    
        __doc__ = 'A company that makes everything for coyotes worldwide.'
    
        factories = 150
    
        def __init__(self, main_customer='Willy the Coyote', product1=None):
            self._main_customer = main_customer
            self.product1 = product1
    
        @classmethod
        def how_many(cls):
            "Brag how many factories are owned by ACME"
            return cls.factories 
    
> company = ACME(product1='sling')


> odump(company, whelp=True)

<__main__.ACME object at 0x7f6f4d94a198>
A company that makes everything for coyotes worldwide.

 == Attributes of <__main__.ACME object at 0x7f6f4d94a198>: ==

--> obj._main_customer = 'Willy the Coyote'
builtin: <class 'str'>

--> obj.factories = 150
builtin: <class 'int'>

--> obj.how_many = <bound method ACME.how_many of <class '__main__.ACME'>>
Brag how many factories are owned by ACME

--> obj.product1 = 'sling'
builtin: <class 'str'>        
"""
