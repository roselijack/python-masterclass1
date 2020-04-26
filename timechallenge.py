import time
time.perf_counter()
time.monotonic()
time.time()
time.process_time()
#print(time.strftime('%X',time.perf_counter()))
print(time.get_clock_info('perf_counter')) #打印特定时钟实现信息
print(time.get_clock_info('monotonic'))
print(time.get_clock_info('time'))
print(time.get_clock_info('process_time'))