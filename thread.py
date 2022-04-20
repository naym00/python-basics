import threading
  
def print_cube(n1, n2):
    print(f"Cube: {n1*n1*n1} and {n2*n2*n2}")
  
def print_square(n1, n2):
    print(f"Cube: {n1*n1} and {n2*n2}")
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10, 20))
    t2 = threading.Thread(target=print_cube, args=(10, 20))
  
    t1.start() # starting thread 1
    t2.start() # starting thread 2
  
    t1.join() # wait until thread 1 is completely executed
    t2.join() # wait until thread 2 is completely executed
  
    # both threads completely executed
    print("Done!")