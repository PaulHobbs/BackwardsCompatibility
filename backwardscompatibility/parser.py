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

import ordereddict


def parse_file(file_name):
  with open(file_name) as fp:
    return ast.parse(fp.read(), file_name).body


def is_public(name):
  return not name.startswith('_')


def symbols_defined(body):
  names = set()
  for statement in body:
    if isinstance(statement, ast.Assign):
      names |= set(name.id for name in statement.names
                   if is_public(name.id))
    if isinstance(statement, (ast.FunctionDef, ast.ClassDef)):
      if is_public(statement.name):
        names.add(statement.name)

  return names


def definitions(body, typ):
  return OrderedDict(
    (statement.name, statement)
    for statement in body
    if isinstance(statement, typ) and is_public(statement.name))
