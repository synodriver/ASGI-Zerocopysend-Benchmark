# ASGI-ZeroCopySend Benchmark

### Tested with wrk, running with uvicorn and nonecorn, 

- uvicorn is mean to be fast, but lack of extension support
- nonecorn has all extension support list in [asgiref](https://asgi.readthedocs.io/en/latest/extensions.html)


## Result

- with the same asgi app, zerocopysend extension showed around a 10x speed up against normal one

![with uvicorn](https://raw.githubusercontent.com/synodriver/ASGI-Zerocopysend-Benchmark/main/result/20220621113603.png)

![with nonecorn](https://raw.githubusercontent.com/synodriver/ASGI-Zerocopysend-Benchmark/main/result/20220621113629.png)
