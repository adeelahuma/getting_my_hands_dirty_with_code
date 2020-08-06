package main.java;

public class MyStack implements StackI{

    int [] stack = new int[10];
    int t = -1;

    public void push(int x){
        t++;
        if (t >= stack.length) {
            System.out.println("Stack Overflow");
            System.exit(0);
        }
        stack[t] = x;

    }
    public int pop (){
        if (t <=-1)
        {
            System.out.println("Stack Illegal index");
            System.exit(0);
        }
        int ret = stack[t];
        stack[t] = 0;
        t--;
        return ret;
    }


    public int top(){
        return stack[t];
    }

    public boolean isEmpty(){
        if (t == -1)
            return true;

        return false;
    }

    void print(){
        //print till 'top' because thats the top of our stack
        for (int i = 0 ; i <= t; i++){
            System.out.print(" " + stack[i] + " ");
        }
    }


    public static void main(String [] args){

        MyStack myStack = new MyStack();

        myStack.push(1);
        myStack.push(2);
        myStack.push(3);
        myStack.push(4);
        myStack.push(5);
        myStack.print();
//        myStack.push(6);
//        myStack.push(7);
//        myStack.push(8);
//        myStack.push(9);
//        myStack.push(10);
//
//        myStack.print();

        System.out.println("Is empty: " + myStack.isEmpty());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        System.out.println(myStack.pop());
        myStack.print();
        System.out.println(myStack.top());
    }



}
