#!/usr/bin/python3.9
# -*-coding:utf-8 -*

import os

class Dico:
    def __init__(self, *args, **kwargs):
        self.items = []
        if len(args) > 1:
            raise AttributeError('Cannot instanciate', __name__, 'with multiple value arguments')
        elif len(args) == 1 and not kwargs:
            dico_cpy = args[0]
            if isinstance(dico_cpy, type(self)):
                for i in dico_cpy.items:
                    self.items.append(self._Item(i.key, i.value))
            else:
                raise TypeError("Can only instanciate '{}' with '{}' type, but received: '{}'".format(__name__, __name__, dico_cpy))
        else:
            for k,v in kwargs.items():
                self.items.append(self._Item(k, v))
                
    def __keys(self):
        return list(map(lambda i: i.key, self.items))
    def __values(self):
        return list(map(lambda i: i.value, self.items))

    keys = property(__keys)
    values = property(__values)
    
    def sort(self):
        sorted_items = []
        for key in sorted(self.keys):
            item = next(i for i in self.items if i.key == key)
            sorted_items.append(item)
        self.items = sorted_items

    def reverse(self):
        self.items.reverse()
        
    def __len__(self):
        return len(self.items)

    def __str__(self):
        str = ""
        str += '{'
        for i in self.items:
            str += "{} : {}, ".format(i.key, i.value)
        return str[:len(str)-2] + '}'

    def __contains__(self, key):
        return next((i for i in self.items if i.key == key), None)
    
    def __getitem__(self, key):
        try:
            item = next(i for i in self.items if i.key == key)
        except:
                raise KeyError("Key '{}' not found".format(key))
        return item.value

    def __setitem__(self, key, value):
        item = next((i for i in self.items if i.key == key), None)
        if item:
            item.value = value
        else:
            self.items.append(self._Item(key, value))

    def __delitem__(self, key):
        item = next((i for i in self.items if i.key == key), None)
        self.items.remove(item)
        del item

    def __add__(self, dico_2_add):
        if isinstance(dico_2_add, type(self)):
            for i in dico_2_add.items:
                if i.key not in self.items:
                    self.items.append(i)
        else:
            raise TypeError("Can only add '{}' with '{}' type, but received: '{}'".format(__name__, __name__, dico_2_add))
        
    def __iter__(self):
        return self._ItDico(self)

    class _ItDico:
        def __init__(self, dico):
            self.dico = dico
            self.pos = -1
        def __next__(self):
            self.pos += 1
            if(self.pos >= len(self.dico)):
                raise StopIteration
            return self.dico.keys[self.pos], self.dico.values[self.pos]

    class _Item:
        def __init__(self, k, v):
            self.key = k
            self.value = v

        def __str__(self):
            return "{} : {}".format(self.key, self.value)
