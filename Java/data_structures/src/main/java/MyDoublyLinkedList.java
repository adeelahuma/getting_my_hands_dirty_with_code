package main.java;

public class MyDoublyLinkedList {
    DDNode head = null;

    void insertAtHead(int x){
        DDNode node = new DDNode(x);

        if (head == null){
            head = node;
        }else{
            head.prev = node;
            node.next = head;
            head = node;

        }

    }

    void insertAtTail(int x){
        DDNode node = new DDNode(x);
        if (head == null){
            head = node;
        }else{
            DDNode temp = head;
            while (temp.next != null){
                temp = temp.next;
            }
            temp.next = node;
            node.prev = temp;
        }

    }

    void print(DDNode p){

        if (p == null){

        } else {
            System.out.print(p.value);
            print(p.next);

        }

    }

    void reversePrint(){
        DDNode temp = head;
    //this has to be temp.next !=null because if we say temp != null,
        // then we won't have temp.prev at that point, we have reached at the end of list
        while (temp.next != null){
            //System.out.print(temp.value);
            temp = temp.next;
        }

        while(temp !=null){
            System.out.print(temp.value);
            temp = temp.prev;

        }


    }

    public static void main(String [] args){

        MyDoublyLinkedList doublyLinkedList = new MyDoublyLinkedList();
        doublyLinkedList.insertAtHead(1);
        doublyLinkedList.insertAtHead(2);
        System.out.println("\nprint list");
        doublyLinkedList.print(doublyLinkedList.head);

        doublyLinkedList.insertAtTail(3);
        doublyLinkedList.insertAtTail(4);
        System.out.println("\nprint list");
        doublyLinkedList.print(doublyLinkedList.head);
        System.out.println("\nReverse print list");
        doublyLinkedList.reversePrint();
    }

}

class DDNode{
    DDNode next;
    DDNode prev;
    int value;

    public DDNode(int x){
        value = x;
        next = prev = null;
    }

}
