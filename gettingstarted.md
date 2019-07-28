# Quick Start!

First you gotta install it, `pip3 install plugged --user`.


## plugged.im

The quick and easy method!

```python
import plugged # This will be assumed from now on

plugins = plugged.im('plugins/*.py')
plugins.file.function('My', 'params')

# -- or --

plugin = plugged.im('plugins/file.py')
plugin.function('My', 'params')
```

`plugged.im` returns a namespace when loading multiple files, When loading a single file it will return the module reference directly.


## plugged.load


The fun method!

```python
plugins = plugged.namespace(plugged.load('plugins/*.py'))
plugins.file.function('My', 'params')

# -- or --

plugins = dict(plugged.load('plugins/*.py'))
plugins['file'].function('My', 'params')

# --

for name, module in plugged.load('plugins/*.py'):
   module.function('My', 'params')
```

`plugged.load` yields an iterator where the values are `(name, module)`.
This is pretty OP when combined with a lot of internal structures.


## plugged.point

*UNLIMITED POWWWWEEEEEEEEEEEEEEEEERR*

These are entry point decorations for classes or functions.
Anything you want instant and easy access to just drop a `@plugged.point` above it.

```python
# main.py

plugins = plugged.namespace(plugged.points('plugins/*.py'))
plugins.function('My', 'params')

myclass = plugins.MyClass()
myclass.method()

# plugins/file.py

@plugged.point
def function(*args, **kwargs):
   print('Do the thing')

# plugins/other.py

@plugged.point
class MyClass:
   def method(self):
      print(f'Positive {self} image')
```
