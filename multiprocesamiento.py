from multiprocessing import Process

def funcion(i):
    for x in range(2000000):
        print('proceso '+i+" - "+str(x))

if __name__ == '__main__':
    p = Process(target=funcion,args=('w'))
    p2 = Process(target=funcion,args=('x'))
    p3 = Process(target=funcion,args=('y'))
    p4 = Process(target=funcion,args=('z'))
    p.start()
    p2.start()
    p3.start()
    p4.start()
    p.join()
    p2.join()
    p3.join()
    p4.join()
