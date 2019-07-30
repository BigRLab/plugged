# extenders

`plugged.mixin.Extend` and `plugged.mixin.PointExtend` are really fun, or insane. Depends on who you ask.

*Ill just show you*

```python
# main.py

class MyClass(plugged.mixin.PointExtend):
   
   def method1(self):
      print('I AM METHOD 1')


cls = MyClass(plugged.load('plugins/*.py'))
cls.method1()
cls.method2()
cls.method3()


# plugins/hello.py

@plugged.point
def method2():
   print('I AM METHOD 2')

   # Functions are loaded like methods that don't have access to self.
   # This keeps the funcs much cleaner and still usable as normal functions.


# plugins/other.py

@plugged.point
class MyPlugin:
   
   @plugged.point
   def method3(self):
      print('I AM METHOD 3', self)
      print(self.method1())

      # self in this instance is a reference to 'MyClass' in main.py
```
