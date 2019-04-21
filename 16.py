import multiprocessing
from time import  sleep,ctime

def consumer(input_q):
    print("into consumer:",ctime())
    while True:
        item=input_q.get()
        if item is None:
            break
        print("pull",item,"out of q")
        input_q.task_done()
    print("out of consumer:",ctime())

def producer(sequence,output_q):
    print("into producer:", ctime())
    for item in sequence:
        print("put", item, "into q")
        output_q.put(item)
    print("out of producer:", ctime())

if __name__ == '__main__':
    q=multiprocessing.JoinableQueue()
    cons_p=multiprocessing.Process(target=consumer,args=(quit()))
    cons_p.daemon=True
    cons_p.start()

    sequence=[1,2,3,4] #生产的产品
    producer(sequence,q)

    q.put(None)
    cons_p.join()

