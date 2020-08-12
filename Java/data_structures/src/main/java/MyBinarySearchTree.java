package main.java;

import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

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

    // time complexity -- > o(log n)
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

    //time complexity  O(n)  --> n = number of nodes
    //space complexity O(n)
    //  when binary tree is complete max nodes at last level is n/2 . so max nodes in the queue = n/2
    void breadthFirstTraversal(BNode head){

        Queue<BNode> queue = new LinkedList<>();
        if (head != null){
            queue.add(head);

            while(!queue.isEmpty()){
                BNode temp = queue.poll();
                System.out.print(temp.data);
                System.out.print(" ");

                if (temp.left != null) queue.add(temp.left);
                if (temp.right != null) queue.add(temp.right);
            }
        }
    }

    // Pre order traversal --> Root, left , right
    //memory usage is in stack  for each function call
    // space complexity = O(h) --> h = height of the tree
    //time complexity = O (n) --> n = number of nodes
    void preOrderTraversal (BNode head){

        if (head != null) {
            System.out.print(head.data);
            System.out.print(" ");
            preOrderTraversal(head.left);
            preOrderTraversal(head.right);
        }
    }


    // In order traversal --> left , root, right
    //memory usage is in stack  for each function call
    // space complexity = O(h) --> h = height of the tree
    void inOrderTraversal (BNode head){

        if (head != null) {

            inOrderTraversal(head.left);
            System.out.print(head.data);
            System.out.print(" ");
            inOrderTraversal(head.right);
        }
    }

    // Post order traversal --> left , right, root
    //memory usage is in stack  for each function call
    // space complexity = O(h) --> h = height of the tree
    void postOrderTraversal (BNode head){

        if (head != null) {

            postOrderTraversal(head.left);
            postOrderTraversal(head.right);
            System.out.print(head.data);
            System.out.print(" ");
        }
    }


    /**
     * Check if binary tree is a binary search tree
     *
     * <<Approach-1>>
     *     - Do post order traversal
     *     - value and left node
     *     - value at right node
     *     - compare it with root node
     * <<Approach-2>>
     *      - Find max in left tree
     *      - Find min in right sub-tree
     *      - if root value is greater than the max value of left tree AND root value is less than the min value of right tree
     * <<Approach-3>>
     *     - set range for each node value and check if node value is within that range
     *     -
     *     -
     * */


    boolean isBSTUtil(BNode head, int minVal, int maxVal){
        if (head == null)
            return true;

        if (head.data >= minVal && head.data < maxVal &&
            isBSTUtil(head.left, minVal, head.data) &&
             isBSTUtil(head.right, head.data, maxVal)){
            return true;
        }else{
            return false;
        }
    }

    boolean isBinarySearchTree(BNode head){

        return isBSTUtil(head, Integer.MIN_VALUE, Integer.MAX_VALUE);
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

        System.out.println("Breadth First Traversal --> ");
        bst.breadthFirstTraversal(bst.root);

        System.out.println("\nPreOrder  Traversal --> ");
        bst.preOrderTraversal(bst.root);

        System.out.println("\nInOrder  Traversal --> ");
        bst.inOrderTraversal(bst.root);

        System.out.println("\nPost Order  Traversal --> ");
        bst.postOrderTraversal(bst.root);

        System.out.println("\nIs Binary Search Tree --> " + bst.isBinarySearchTree(bst.root));

        //Add a Node to the left of the tree that breaks BST criteria
        BNode node = bst.root;
        while(node.left != null){
            node = node.left;
        }
        node.left = new BNode(23);

        System.out.println("\nIs Binary Search Tree --> " + bst.isBinarySearchTree(bst.root));

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
