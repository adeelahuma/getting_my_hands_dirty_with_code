package main.java;

public class MyLinkedList {
    Node head = null; // points to head or first node
    int count = 0;
    public static void main (String [] args){

        // create a linked list of 2,3,6
        MyLinkedList myLinkedList = new MyLinkedList();
//        myLinkedList.insertNodeAtEnd(1);
//        myLinkedList.insertNodeAtEnd(2);
//        myLinkedList.insertNodeAtEnd(3);
//        myLinkedList.print();
//        System.out.println("count--> "+myLinkedList.count);
//        System.out.println("-------");
//        myLinkedList.count =0;
//        myLinkedList.head = null;
//        myLinkedList.insertNodeAtBegin(1);
//        myLinkedList.insertNodeAtBegin(2);
//        myLinkedList.insertNodeAtBegin(3);
//        myLinkedList.print();
//        System.out.println("count--> "+myLinkedList.count);

//        System.out.println("-------");
////        myLinkedList.count =0;
//        myLinkedList.head = null;
//        System.out.println("<------> ");
//        myLinkedList.print();
//        System.out.println("<------> ");
//        myLinkedList.insertNodeAtPosition(2,1);
//        myLinkedList.insertNodeAtPosition(3,2);
//        myLinkedList.insertNodeAtPosition(4,1);
//        myLinkedList.insertNodeAtPosition(5,2);
        myLinkedList.print();
//        System.out.println("<------> ");
//        myLinkedList.deleteNodeAtPos(2);
//        myLinkedList.print();
//        System.out.println("<------> ");
//        myLinkedList.deleteNodeAtPos(1);
//        myLinkedList.print();
//        System.out.println("<------> ");
//        myLinkedList.deleteNodeAtPos(2);
//        myLinkedList.print();
//        System.out.println("<---del last mode---> ");
//        myLinkedList.deleteNodeAtPos(1);
//        myLinkedList.print();
        //System.out.println("count--> "+myLinkedList.count);
        System.out.println("<---Reversing empty list---> ");
        myLinkedList.reverseLinkedList();
        myLinkedList.print();
        System.out.println("<------> ");
//        myLinkedList.head = null;
        myLinkedList.insertNodeAtPosition(1,1);
        myLinkedList.print();
        System.out.println("<------> ");
        myLinkedList.reverseLinkedList();
        myLinkedList.print();

        myLinkedList.insertNodeAtPosition(2,2);
        myLinkedList.insertNodeAtPosition(3,3);
//        myLinkedList.print();
        myLinkedList.pprint(myLinkedList.head);
        System.out.println("<------> ");
//        myLinkedList.reverseLinkedList();
//        myLinkedList.print();

        myLinkedList.Print(myLinkedList.head);
        System.out.println("<------> ");
        myLinkedList.rPrint(myLinkedList.head);
        System.out.println("<------> ");
        myLinkedList.reverseLinkedList(myLinkedList.head);
        myLinkedList.Print(myLinkedList.head);
    }

    void insertNodeAtEnd(int x){
//        System.out.println("insertNodeAtEnd");
        Node node = new Node(x);

        if (head == null){

            head = node;

        }else{

            Node temp = head;

            while (temp.next != null){
                temp = temp.next;
            }
//            System.out.println(temp.value);
            temp.next = node;

            }
        count++;
        }

    void insertNodeAtBegin(int x){
        Node node = new Node(x);

        if (head == null){

            head = node;

        }else{
            node.next = head;
            head = node;
        }
        count++;
    }

    void insertNodeAtPosition(int x, int pos){
        //potential scenarios
        // head is null
        // insert at 1
        //insert in middle
        //insert at the end

        Node node = new Node(x);

        if (pos == 1){ // works when head == null or inserting at the beginning
            node.next = head;
            head= node;
        }
        else {

            Node temp = head;
            for (int i = 1; i < pos - 1; i++) {
//            if (temp.next == null)
//                return -1;

                temp = temp.next;
            }

            node.next = temp.next;
            temp.next = node;

        }

        //count++;
    }

    void deleteNodeAtPos(int pos){

        Node temp = head;

        //go to n-1 node
        for (int i =1; i < pos-1; i++){
            temp = temp.next;
        }


        if (temp.next != null) {
            Node delNode = temp.next;
            temp.next = delNode.next;
        }
        else
            head =null;

    }


    void print(){

        if (head != null){
            Node temp = head;
            while (temp !=  null){
                System.out.print(temp.value + " ");
                temp = temp.next;

            }
        }
    }

    void Print(Node p){

        if(p == null){
            System.out.print("");
        }else {
            System.out.print(p.value);
            Print(p.next);


        }
    }

    void rPrint(Node p){

        if(p == null){
            System.out.print("");
        }else {
            rPrint(p.next);
            System.out.print(p.value);

        }
    }

    void reverseLinkedList(Node p){

        if(p.next  == null){
            head = p;
//            return p;
        }else{
            reverseLinkedList(p.next);
            Node prev = p.next;
            prev.next = p;
            p.next = null;
//            return  p;
        }

    }


    void reverseLinkedList(){
        // head --> 2 --> 4 --> 6 ---> 5 --> null
        //reverse // head --> 5 --> 6 --> 4 ---> 2 --> null
        Node current = head;
        Node prev = null;
        Node next = null;

        while (current != null){

            next = current.next;
            current.next = prev;
            prev = current;
            current = next;

        }
        head = prev;
    }


    void pprint(Node p){
        if (p ==null){

        }else{
            System.out.print(p.value);
            pprint(p.next);
        }

    }

    Node  rReverse(Node p){
        if (p.next == null){
            return p; //p is now head
        }else{
            Node prev = rReverse(p.next);

            prev.next = p;
            p.next = null;
            return p;
        }

    }

}


class Node{
    Node next;
    int value;

    Node(int v){
        next = null;
        value = v;
    }

    Node(int v, Node h){
        next = h;
        value = v;
    }

    public String toString(){
        return ("val--> "+ value);
    }
}