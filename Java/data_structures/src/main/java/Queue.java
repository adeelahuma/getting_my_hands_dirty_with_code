import java.util.ArrayList;
import java.util.List;

public class Queue {

    private int startIndex;
    private List<Integer> data;


    public Queue(){
        data = new ArrayList<>();
        startIndex = 0;
    }

    public boolean enqueue(Integer x){
        data.add(x);
        return true;
    }
    //Just move the next (its as if the link is broken)
    public boolean dequeue(){
        //return data.remove(0);
        if(isEmpty()){
            return false;
        }
        startIndex++;
        return true;
    }

    public int getElementFromFront(){
        return data.get(startIndex);
    }

    public boolean isEmpty(){
        return (startIndex == data.size());
    }

    public static void main(String args[]){

        System.out.println("Basic main.Queue");

        Queue queue = new Queue();
        queue.enqueue(1);
        queue.enqueue(2);

        System.out.print("data in memory-->"+queue.data);
        System.out.println("front element-->" + queue.getElementFromFront());

        queue.dequeue();

        System.out.print("data in memory-->"+queue.data);
        System.out.println("front element-->" + queue.getElementFromFront());

        // we are just moving the pointer and
        // memory keeps growing as we keep queueing elements
        // not good in terms of memory
    }


}
