class Patching:
    async def __call__(self,):
        return await self.__method()

    async def __method(self):
        return "Patching"
