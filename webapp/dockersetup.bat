docker run --name pronuance-redis -p 6379:6379 -it -d redis redis-server --save 60 1 --loglevel warning