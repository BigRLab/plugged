# plug

An extremely simple arbitrary import system built ontop of SourceFileLoader from `importlib`. Supports glob based paths.


## Examples / Overview


Quick drop in `import` replacement for local files.


```python
# main.py
hello = plug.im('plugins/hello.py')

print(hello.hello('sj1k'))

# plugins/hello.py

def hello(name):
   return f'Hello {name}!'
```


## Setup / init funcs

plug supports calling init / teardown logic across all plugins.

```python
# main.py
modules = plug.load('plugins/*.py')
plugins = plug.namespace(plug.call(modules, name='setup', *args, **kwargs))

module, init = plugins.hello   # init is the result of setup(*args, **kwargs)
print(module, init)

# plugins/hello.py

class Hello: pass

def setup(*args, **kwargs):
   return Hello(*args, **kwargs)
```


## Plug points

Plug points are fun to play with. No, these are not the ones that zap.

```python
# main.py

plugs = plug.namespace(plug.points('plugins/*.py'))
print(plugs.func())


# plugins/mahfile.py

import plug

@plug.point
def func():
   print('Do the thing')
```

Plug points are entry points telling plug exactly what funcs you want to run.
It only loads these from the modules but that comes with the upside of discarding the module names entirely.


## CLASSES!!!

The classes populate their `__dict__` attribute when they load the plugins. This lets you call them as if they were methods.
Mix it with your other classes, overwriting methods galore!


The `PointExtend` is really unique, if you have any class decorated with `plug.point` the extender will gather any methods from this class that also have `plug.point`,
it will call these like they were defined on the PointExtend class, even passing the self instance.

Yeah, that's right, we've got OOP across arbitrary files. (I wanted to combine `You're welcome` with `I'm sorry` and settled on `You're sorry`)


```python
# main.py

class Main(plug.mixin.PointExtend):

   def main_method(self):
      self.testing('AAHAHAHAHAHA AAAAHHAHHAAAAHAHAHAHA')

m = Main('plugins/*.py')
m.main_method()

# plugins/test.py

@plug.point
class Test:

   @plug.point
   def testing(self, message):
      print(message)
```
