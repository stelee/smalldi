# SmallDI
Yet another dependencies injection for Python

## Why we need DI

A lot of people **love** dependencies injection and we **do** have a lot of DI framework already. Like Spring in Java or AngularJS for Javascript.

Yet I haven't found any simple DI framework for python.

There is the [discussion](http://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python) explain why DI is not common in Python. I agree most part of it. But I still like Python to support DI, because:

* when building a complex system, DI can help me to build   the mockup object. And I don't want to put 'if...then...'  too much when importing the module
* In one of my recent project, I realize that I have to write a lot of 'from...import...' and most of them are duplicated among the files. I hate duplication and DI can help me with that
* I have written a lot of spring-based app and angularjs-based app. I like the way to write the code and I want to have the same for python app.

### How about theis DI framework

Actually, it can hardly be named as 'framework', just some libraries and decorators. When I start to write this, I was thinking of the implementation. A framework can be either as simple as serveral lines of code or as complex as spring framework. I want to keep the thing simple and complete.

* Since technically there is no real different for @component, @service, @provider; I would like to only keep @component to register the instance into the system
* Simple enough, only have the core function

### How to use it
For details, you can check the test code.

To register component

	@component()
	class MyComponent:
		def foo():
			return 'bar'

	MyComponent()

To inject component

	@injection('MyComponent')
	class App:
		pass

	app = App()
	print(app.myComponent.foo()) #output 'bar'

### In the future
Now it is the very early stage of this small framework. Good thing is that it can be used with other framework. I am going to use it in several projects(specially in one of the big django project). Add more function and add more dcoument.

### Thanks
Hope you will enjoy that! If you have any question, please [send email to me](mailto:liy@leesoft.ca). I would be very happy to talk to you.

### Others
Yes, it is under MIT license, open sourced and free to use! Now it only supports Python 3.x
