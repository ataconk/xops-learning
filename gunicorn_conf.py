from multiprocessing import cpu_count



# Socket Path

bind = 'unix:/usr/local/bin/home/gunicorn.sock'



# Worker Options

workers = cpu_count() + 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = '/usr/local/bin/home/access_log'

errorlog =  '/usr/local/bin/home/error_log'
