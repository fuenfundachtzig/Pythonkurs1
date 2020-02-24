#!/usr/bin/env python

from distutils.core import setup, Extension

person_module = Extension('_person',
                           sources = ['person_wrap.cxx',
                                      'person.cxx'],
                          )

setup(name        = 'person',
      version     = '0.1',
      author      = 'John Doe',
      description = '''C++ class Person wrapper''',
      ext_modules = [person_module],
      py_modules  = ["person"],
     )
