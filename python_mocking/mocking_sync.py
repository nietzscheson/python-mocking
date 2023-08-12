class Mocking:
    def call(self):
        self.static_method()
        Mocking.class_method()
        self.instance_method()
        self._Mocking__private_instance_method()
        Mocking._Mocking__private_class_method()
        Mocking._Mocking__private_static_method()

    @staticmethod
    def static_method():
        print("static_method")

    @classmethod
    def class_method(cls):
        print("class_method")

    def instance_method(self):
        print("instance method")

    def __private_instance_method(self):
        print("private instance method")

    @classmethod
    def __private_class_method(cls):
        print("private class method")

    @staticmethod
    def __private_static_method():
        print("private static method")
