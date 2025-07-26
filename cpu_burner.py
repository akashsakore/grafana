import threading

def burn_cpu():
    while True:
        pass  # Infinite loop to consume CPU

# Number of threads = number of CPU cores you want to stress
num_threads = 4  # Adjust this based on your system (e.g., 4 for quad-core)

threads = []

for _ in range(num_threads):
    t = threading.Thread(target=burn_cpu)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

