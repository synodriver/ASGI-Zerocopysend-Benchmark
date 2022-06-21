# ASGI-ZeroCopySend Benchmark

### Tested with wrk, running with [uvicorn](https://github.com/encode/uvicorn) and [nonecorn](https://github.com/nonebot/nonecorn), 

- uvicorn is mean to be fast, but lack of extension support
- nonecorn has all extensions support listed in [asgiref](https://asgi.readthedocs.io/en/latest/extensions.html)


## Result

- with the same asgi app, zerocopysend extension showed around a 10x speed up against normal one

- the one with uvicorn

![with uvicorn](https://raw.githubusercontent.com/synodriver/ASGI-Zerocopysend-Benchmark/main/result/20220621113603.png)

- the one with nonecorn

![with nonecorn](https://raw.githubusercontent.com/synodriver/ASGI-Zerocopysend-Benchmark/main/result/20220621113629.png)
