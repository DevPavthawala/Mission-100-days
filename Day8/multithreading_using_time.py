import time
import threading
def calc_square(number):
    print("Calculate Square")
    for n in number:
        time.sleep(0.2)
        print(f"Square { n*n}")

def calc_cube(number):
    print("Calculate Cube")
    for n in number:
        time.sleep(0.2)
        print(f"Cube  {n**3}")

arr = [2,3,4,5,6]

t = time.time()

t1 = threading.Thread(target=calc_square,args=(arr,))
t2 = threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"done in {time.time()-t}")
print("hah....I am done with all my work now!")