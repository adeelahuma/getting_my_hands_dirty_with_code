public class MyCircularQueue {

    private int head;
    private int tail;
    private int[] data;
    private int size;       //capacity of queue

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        head = -1;
        tail = -1;
        size = 0;
        data = new int[k];
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (!isFull()) {

            if (head == -1)
                head = 0;

            if( tail == data.length-1)
                tail = 0; // reset the pointer

            data[++tail] = value;
             size++; //a new element added
            return true;
        }
        else
            return  false;
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (isEmpty())
            return false;
        if (head == data.length)
            head = 0; //reset the pointer
        else
            head++;
        size--;
        return true;
    }

    /** Get the front item from the queue. */
    public int Front() {
        if (isEmpty())
            return -1;
        return data[head];
    }

    /** Get the last item from the queue. */
    public int Rear() {
        if (isEmpty())
            return -1;
        return data[tail];
    }

    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return  size < data.length;
    }

    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return  size == data.length;
    }

}