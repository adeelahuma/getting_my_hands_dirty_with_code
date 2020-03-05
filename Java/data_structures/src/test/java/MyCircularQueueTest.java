public class MyCircularQueueTest {

    public static void main(String args[]){

        MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3


        System.out.println("Test case 1: ");
        assert circularQueue.enQueue(1) : "1 added to queue";  // return true
        assert circularQueue.enQueue(2) : "2 added to queue";  // return true
        assert circularQueue.enQueue(3) : "3 added to queue";  // return true

        System.out.println("Test case 2: ");
        assert !circularQueue.enQueue(4) : "queue full";  // return false, the queue is full


        System.out.println("Test case 3: ");
        assert circularQueue.Rear() == 3 ;  // return 3
        assert circularQueue.isFull();  // return true

        System.out.println("Test case 4: ");
        assert circularQueue.deQueue();  // return true

        System.out.println("Test case 5: ");
        assert circularQueue.enQueue(4);  // return true
        assert circularQueue.Rear() == 4;  // return 4

        System.out.println("Test case finished ");
    }
}
