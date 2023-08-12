class MockingAsync:
    async def call(self):
        await self.static_method()
        await MockingAsync.class_method()
        await self.instance_method()
        await self._MockingAsync__private_instance_method()
        await MockingAsync._MockingAsync__private_class_method()
        await MockingAsync._MockingAsync__private_static_method()

    @staticmethod
    async def static_method():
        print("static_method")

    @classmethod
    async def class_method(cls):
        print("class_method")

    async def instance_method(self):
        print("instance method")

    async def __private_instance_method(self):
        print("private instance method")

    @classmethod
    async def __private_class_method(cls):
        print("private class method")

    @staticmethod
    async def __private_static_method():
        print("private static method")
