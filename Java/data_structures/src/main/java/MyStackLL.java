package main.java;

public class MyStackLL implements StackI {
    Node stack;
    int top = -1;
    public void push(int x){

        Node node = new Node(x);

        //inserting at the top of the list
        if (stack == null){
            stack = node;
        }else{
            node.next = stack;
            stack = node;

        }
    }

    public int pop(){
        //INSERT AT THE TOP OF THE STACK
        if (stack == null){
           return -1;
        }else{
            int ret = stack.value;
            stack = stack.next;
            return ret;
        }
    }

    public int top(){
        if (stack == null)
            return -1;
        else
            return stack.value;
    }

    public boolean isEmpty(){
        if (stack == null)
            return true;

        return false;
    }

    void print(){
        Node temp = stack;


        while (temp != null){
            System.out.println(temp.value);
            temp = temp.next;
        }



    }
    public static  void main(String [] args){
        System.out.println();

        MyStackLL stack = new MyStackLL();

        stack.push(1);
        stack.push(2);

        stack.print();

        System.out.println(stack.pop());

        stack.print();

        System.out.println(stack.top());

        stack.push(3);
        stack.push(4);
        System.out.println(stack.top());


    }

}
