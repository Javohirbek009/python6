import threading

def func():
    for x in range(100):
        print("hello")
def func2():
    for x in range(100):
        print("hi")

func()
func2()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func2)


t1.start()
t2.start()


 ###
 
def func():
    for x in range(100):
        print("hello")
def func2():
    for x in range(100):
        print("hi")

func()
func2()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func2)


t1.start()
t2.start()