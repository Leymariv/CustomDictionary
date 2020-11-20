#!/usr/bin/python3.9
# -*-coding:utf-8 -*

from ..dico import *
import unittest

class DicoTester(unittest.TestCase):
    def test_empty_dico(self):
        empty_dico = Dico()
        assert len(empty_dico.items)  == 0
        assert len(empty_dico) == 0
    
    def test_raise_TypeErrorException(self):
        try:
            copy_dico = Dico("toto")
            assert False
        except Exception as exc:
            assert isinstance(exc, TypeError)

    def test_raise_AttributeErrorException(self):
        try:
            a = Dico()
            b = Dico()
            copy_dico = Dico(a, b)
            assert False
        except Exception as exc:
            assert isinstance(exc, AttributeError)
            
    def test_dico_instance_by_kvalues(self):
        dico = Dico(Valmon = 10, Guillaume = 5, Xav = 3)
        assert len(dico) == 3

    def test_dico_key_access(self):
        dico = Dico(Valmon = 10, Guillaume = 5, Xav = 3)
        assert dico['Valmon'] == 10
        
    def test_raise_TypeKeyNotFoundException(self):
        try:
            dico = Dico(Valmon = 10, Guillaume = 5, Xav = 3)
            dico['toto']
            assert False
        except Exception as exc:
            assert isinstance(exc, KeyError)

    def test_dico_value_modification(self):
        dico = Dico(Valmon = 10, Guillaume = 5, Xav = 3)
        dico['Alex'] = 'WAW'
        dico['Valmon'] = 3
        assert dico['Valmon'] == 3
        assert len(dico) == 4
        
    def test_dico_instance_by_copy(self):
        dico1 = Dico(Valmon=10, Guillaume=5, Xav=3)
        dico = Dico(dico1)
        dico1['Alex'] = 'WAW'
        dico1['Valmon'] = 3
        assert dico['Valmon'] == 10
        assert len(dico) == 3

    def test_dico_instance_by_copy(self):
        dico = Dico(Valmon=10, Guillaume=5, Xav=3)
        del dico['Valmon']
        try:
            dico['Valmon']
        except Exception as exc:
            assert isinstance(exc, KeyError)
        assert len(dico) == 2

    def test_dico_key_in_dico(self):
        dico = Dico(Valmon=10, Guillaume=5, Xav=3)
        assert 'Valmon' in dico

    def test_dico_sort(self):
        dico = Dico(Valmon=10, Guillaume=5, Xav=3, Alex = 'NaN')
        dico.sort()
        assert dico.keys[0] == 'Alex'
        assert dico.values[0] == 'NaN'
        assert dico.keys[3] == 'Xav'
        assert dico.values[3] == 3
    
    def test_dico_reverse(self):
        dico = Dico(Valmon=10, Guillaume=5, Xav=3, Alex = 'NaN')
        dico.reverse()
        assert dico.keys[0] == 'Alex'
        assert dico.values[0] == 'NaN'
        assert dico.keys[1] == 'Xav'
        assert dico.values[1] == 3
        assert dico.keys[3] == 'Valmon'
        assert dico.values[3] == 10

    def test_dico_going_through(self):
        dico = Dico(Valmon=10, Guillaume=5, Xav=3, Alex = 'NaN')
        dico_items = {}
        for k,v in dico:
            dico_items[k] = v

        for k,v in dico_items.items():
            assert dico[k] == v

    def test_dico_addition(self):
        dico = Dico(Valmon=10, Guillaume=5, Xav=3, Alex = 'NaN')
        dico_2_add = Dico(Patate = 'P', Aubergine = 'A', Courgette ='C')
        dico + dico_2_add
        assert len(dico) == 7
        assert dico['Aubergine'] == 'A'
        assert dico['Valmon'] == 10
        assert dico['Patate'] == 'P'
        
if __name__ == '__main__':
    unittest.main()   
