import threading
import time
def loop1(in1):
    print('Start loop 1 at:',time.ctime())
    print("premeter ",in1)
    time.sleep(4)
    print('End loop 1 at:',time.ctime())

def loop2(in1,in2):
    print('Start loo 2 at:',time.ctime())
    time.sleep(2)
    print("premeter1 ",in1,"premeter2 ",in2)
    print('End loop 2 at:',time.ctime())
def main():
    print('Starting at:',time.ctime())

    t1=threading.Thread(target=loop1,args=("lisa",))
    t1.start()
    t2=threading.Thread(target=loop2,args=("lisa","jane"))
    t2.start()

    t1.join()
    t2.join()

    print('Ending at:', time.ctime())

if __name__=='__main__':
    main()