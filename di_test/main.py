import unittest
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from di.context import Context
from di.decorators import *


class TestContextSingleton(unittest.TestCase):
    def test_id_singlton(self):
        context1 = Context()
        context2 = Context()
        self.assertEqual(id(context1), id(context2))
    def test_component_create(self):
        @component()
        class Foo:
            pass
        Foo()
        self.assertIsNotNone(Context().getComponent('Foo'))
    def test_component_is_another_singleton(self):
        @component()
        class Bar:
            pass
        bar1 = Bar()
        bar2 = Bar()
        self.assertEqual(bar1, bar2)
    def test_component_create_with_identifier(self):
        @component(identifier='mycomp')
        class Foo2:
            pass
        Foo2()
        self.assertFalse(Context().hasComponent('Foo2'))
        self.assertTrue(Context().hasComponent('mycomp'))
    def test_simple_injection(self):
        @component()
        class MyService:
            def foo(self):
                return 'bar'
        @inject('MyService')
        class MyUseService:
            pass

        MyService()
        use_service = MyUseService()
        self.assertEqual('bar', use_service.myService.foo())
    def test_more_complex_injection(self):
        @component()
        class MyService2:
            def foo(self):
                return 'bar'
        @inject(MyService2='asMyService')
        class MyUseService2:
            pass
        MyService2()
        use_service = MyUseService2()
        self.assertEqual('bar', use_service.asMyService.foo())


if __name__ == '__main__':
    unittest.main()
