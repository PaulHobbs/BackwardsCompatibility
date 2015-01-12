"""
Backwards compatibility
Copyright (C) 2015  Paul Hobbs, paul.mcdill.hobbs@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import ast

import backwardscompatibility.parser


def find_backwards_incompatibilty_errors(old, new, prefix=''):
  removed_symbols = parser.symbols_defined(old) - parser.symbols_defined(new)
  if removed_symbols:
    yield prefix + 'the following symbols were removed: ' + ', '.join(removed_symbols)

  new_classes = definitions(new, typ=ast.ClassDef)

  for cls in definitions(old, typ=ast.ClassDef).iteritems():
    new_cls = new_classes.get(cls.name)
    if new_cls:
      errors = find_backwards_incompatibilty_errors(cls.body, new_cls.body, prefix=prefix + 'in %s: ' % cls.name)
      for error in errors:
        yield errors
