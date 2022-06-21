"""
Copyright (c) 2008-2021 synodriver <synodriver@gmail.com>
"""
# main.py
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import FileResponse
from baize.asgi import FileResponse as ZeroCopyFileResponse

# what if multiple fd opened concurrently?
async def homepage(request):
    return ZeroCopyFileResponse("0c76f16d4bEV5pS.jpg", headers={"content-type": "image/jpg", "x-zerocopysend": "true"})


async def normal(request):
    return FileResponse("0c76f16d4bEV5pS.jpg", headers={"content-type": "image/jpg"})


routes = [
    Route("/zerocopy", endpoint=homepage),
    Route("/nonezerocopy", endpoint=normal)
]

app = Starlette(routes=routes)


class TestMiddleWare:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        self.send = send
        await self.app(scope, receive, self.new_send)

    async def new_send(self, event):
        print(event["type"])
        return await self.send(event)


app.add_middleware(TestMiddleWare)

if __name__ == "__main__":
    from hypercorn.asyncio import serve
    from hypercorn.config import Config
    import asyncio

    config = Config()
    asyncio.run(serve(app, config))
    # use nonecorn or uvicorn
