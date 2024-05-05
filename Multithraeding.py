import threading
import time


def count_up():
    for i in range(1, 6):
        print("Counting up:", i)
        time.sleep(0.5)


def count_down():
    for i in range(5, 0, -1):
        print("Counting down:", i)
        time.sleep(0.5)


if __name__ == "__main__":
    # Har bir vazifani alohida joylashtirish
    thread1 = threading.Thread(target=count_up)
    thread2 = threading.Thread(target=count_down)

    # Vazifalarni boshlash
    thread1.start()
    thread2.start()

    # Vazifalarni tugatishni kutish
    thread1.join()
    thread2.join()

    print("Both threads have finished executing")
