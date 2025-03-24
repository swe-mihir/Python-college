import threading
import time

def print_numbers(thread_name, delay, start, end):
    for i in range(start, end + 1):
        time.sleep(delay)  
        print(f"{thread_name} - {i}")

def main():
    thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1, 1, 5))
    thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 3, 6, 10))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exiting main thread")

if __name__ == "__main__":
    main()
