package main.java;

public class MyBinarySearchTree {
    BNode root = null;

    BNode insert(BNode head, int x){

        if (head == null) {
            head = new BNode(x);
        }else if (x <= head.data){
            head.left = insert(head.left, x);
        }else if (x > head.data){
            head.right = insert(head.right, x);
        }

        return head;
    }


    boolean search(BNode head, int data){

        if (head == null) {
            return false;
        } else if (data == head.data){
            return true;
        }else if (data < head.data){
            return search(head.left, data);
        }else {
            return search(head.right, data);
        }
    }

    int findMin(BNode head){
        //recursive approach
//        if (head == null){
//            return -99;
//        }else if (head.left == null){
//            return head.data;
//        }else {
//            return  findMin(head.left);
//        }

        //iterative approach

        if (head == null){
            return -99;
        }

        while (head.left != null){
            head = head.left;
        }
        return head.data;

    }

    int findMax(BNode head){
        if (head == null){
            return -99;
        }else if (head.right == null){
            return head.data;
        }else{
            return findMax(head.right);
        }

    }

    int findHeight(BNode head){

        if (head == null)
            return -1;

        int leftHeight = findHeight(head.left);
        int rightHeight = findHeight(head.right);
        return Math.max(leftHeight,rightHeight)+1;
    }



    public static void main(String [] args){

        MyBinarySearchTree bst = new MyBinarySearchTree();

        bst.root = bst.insert(bst.root, 15);
        bst.root = bst.insert(bst.root, 10);
        bst.root = bst.insert(bst.root, 20);
        bst.root = bst.insert(bst.root, 25);

        System.out.println(bst.search(bst.root, 20));
        System.out.println(bst.search(bst.root, 10));
        System.out.println(bst.search(bst.root, 8));

        System.out.println("Min Value --> " + bst.findMin(bst.root));
        System.out.println("Max Value --> " + bst.findMax(bst.root));

        System.out.println("Height of Root --> " + bst.findHeight(bst.root));


    }


}

class BNode {

    int data;
    BNode left ;
    BNode right;

    BNode(int x){
        data = x;
        left = right = null;
    }


}
