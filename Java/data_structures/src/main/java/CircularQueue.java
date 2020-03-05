public class CircularQueue {

    private int head;
    private int tail;
    private int[] data;

    public CircularQueue(){
        head = 0;
        tail = 0;
        data = new int[5];
    }
    public boolean isEmpty(){
        return (head == 0 && tail == 0);
    }

    public boolean isFull(){
        return  (tail == data.length && head == 0);
    }

    public boolean enQueue(int x){
        if (isEmpty()) {

            if( tail == data.length)
                tail = 0; // reset the pointer

            data[tail] = x;
            tail++;

//            if (head == 0)
//                head++;

            return true;
        }
        else
            return  false;
    }
    public boolean deQueue(){
        if (head == data.length)
            head = 0; //reset the pointer
        else
            head++;

        return true;
    }

    public int getHead() {
        return head;
    }

    public void setHead(int head) {
        this.head = head;
    }

    public int getTail() {
        return tail;
    }

    public void setTail(int tail) {
        this.tail = tail;
    }

    public int[] getData() {
        return data;
    }

    public void setData(int[] data) {
        this.data = data;
    }

    public static void main(String args[]){

        CircularQueue cq = new CircularQueue();
        cq.enQueue(5);
        cq.enQueue(2);

        assert(cq.head == 0);
        assert(cq.tail == 1);

        cq.deQueue();

        System.out.println(cq.data);
    }
}
