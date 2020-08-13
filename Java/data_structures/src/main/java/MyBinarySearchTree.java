package main.java;



import java.util.LinkedList;
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

    int maxValLeft (BNode head){

        int maxVal = Integer.MIN_VALUE;

        if (head == null)
            return maxVal;

        maxVal = head.data;

        while(head != null){
            if (maxVal < head.data)
                maxVal = head.data;

            head = head.left;
        }

        return maxVal;

    }

    int minValRight (BNode head){

        int minVal = Integer.MAX_VALUE;

        if (head == null)
            return minVal;

        minVal = head.data;

        while(head != null){
            if (minVal > head.data)
                minVal = head.data;

            head = head.right;
        }

        return minVal;

    }
    // Approach 2
    boolean isBST(BNode head){
        if (head == null)
            return false;

        return (head.data >= maxValLeft(head.left) && head.data < minValRight(head.right));

    }


    //Approach - 3
    // set min- max range for each node
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

    // time complexity -- > o(log n)
    BNode findMinLeft(BNode head){

        if (head == null){
            return null;
        }

        while (head.left != null){
            head = head.left;
        }
        return head;
    }

    BNode deleteANode(BNode head, int data){

        if (head == null)
            return null;

        if (head.data == data){

            if (head.left == null && head.right == null){ //case-1
                head = null;

            } else if (head.left == null ){ //case-2
                head = head.right;

            }else if (head.right == null){ //case-2
                head = head.left;

            } else{ //case-3

                BNode temp = findMinLeft(head.right);
                head.data = temp.data ;
                head.right = deleteANode(head.right, temp.data);
            }

        } else if ( data < head.data ){
            head.left = deleteANode(head.left, data);
        }else{
            head.right = deleteANode(head.right, data);
        }

        return head;
    }


    //TODO:
    BNode getSuccessor(BNode head, int data){
        if (head == null)
            return null;

        return null;
    }

    /*
    *  Count the number of leaves in a binary tree
    * */

    int countLeaves(BNode head){
        int count = 0;

        if (head == null)
            count = 0;

        Queue<BNode> queue = new LinkedList<BNode>();

        queue.add(head);

        while(!queue.isEmpty()){
            BNode temp = queue.poll();

            if(temp.left == null && temp.right == null) {
                count += 1;
            } else if(temp.left != null && temp.right != null){
                queue.add(temp.left);
                queue.add(temp.right);
            } else if (temp.left != null) {
                queue.add(temp.left);
            }else if (temp.right != null){
                queue.add(temp.right);
            }
        }

        return count;
    }

    /**
     *  Get Mirror of a binary Tree
     *
     *  Approach - 1:
     *      >> use a queue to save each node ; similar to Breadth first traversal
     *
     *  Approach- 2:
     *      >> use post order traversal and then shift pointers
     * */

    //Approach -1
    BNode getMirrorTree(BNode head){

        BNode mNode = null;

        if (head == null)
            mNode = null;

        mNode = head;

        Queue<BNode> queue = new LinkedList<>();
        queue.add(head);

        while(!queue.isEmpty()){

            BNode curr = queue.poll();
            if (curr.left != null)
                queue.add(curr.left);

            if (curr.right != null)
                queue.add(curr.right);

            BNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
        }

        return mNode;
    }

    //Approach - 2

    BNode getMirrorTree2(BNode head){

        if (head == null)
            return head;

        BNode left = getMirrorTree2(head.left);
        BNode right = getMirrorTree2(head.right);
        head.right = left;
        head.left = right;

        return head;
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

        System.out.println("\nIs Binary Search Tree Approach 3--> " + bst.isBinarySearchTree(bst.root));
        System.out.println("\nIs Binary Search Tree Approach 2--> " + bst.isBST(bst.root));

        System.out.println("\nAdding an larger value in the left sub tree");
        //Add a Node to the left of the tree that breaks BST criteria
        BNode node = bst.root;
        while(node.left != null){
            node = node.left;
        }
        node.left = new BNode(23);

        System.out.println("\nIs Binary Search Tree Approach 3--> " + bst.isBinarySearchTree(bst.root));
        System.out.println("\nIs Binary Search Tree Approach 2--> " + bst.isBST(bst.root));


        MyBinarySearchTree bst1 = new MyBinarySearchTree();

        bst1.root = bst1.insert(bst1.root, 12);
        bst1.root = bst1.insert(bst1.root, 5);
        bst1.root = bst1.insert(bst1.root, 3);
        bst1.root = bst1.insert(bst1.root, 7);
        bst1.root = bst1.insert(bst1.root, 1);
        bst1.root = bst1.insert(bst1.root, 9);
        bst1.root = bst1.insert(bst1.root, 15);
        bst1.root = bst1.insert(bst1.root, 13);
        bst1.root = bst1.insert(bst1.root, 17);

        System.out.println("\n Leaves in BST ==> " + bst1.countLeaves(bst1.root));

        System.out.println("\n Tree Breadth First Traversal... ");
        bst1.breadthFirstTraversal(bst1.root);

        System.out.println("\n Tree after deleting 1: ");
        bst1.root = bst1.deleteANode(bst1.root, 1);

        bst1.breadthFirstTraversal(bst1.root);


        System.out.println("\n Tree after deleting 5: ");
        bst1.root = bst1.deleteANode(bst1.root, 5);

        bst1.breadthFirstTraversal(bst1.root);

        System.out.println("\n Tree after deleting 12 [ROOT]: ");
        bst1.root = bst1.deleteANode(bst1.root, 12);

        bst1.breadthFirstTraversal(bst1.root);

        System.out.println("\n Leaves in BST ==> " + bst1.countLeaves(bst1.root));


        System.out.println("\n Mirror of a Tree - Approach - 1");
        BNode mNode = bst1.getMirrorTree(bst1.root);
        bst1.breadthFirstTraversal(mNode);

        //FIXME
        System.out.println("\n Mirror of a Tree - Approach - 2");
        BNode mNode2 = bst1.getMirrorTree2(mNode);
        bst1.breadthFirstTraversal(mNode2);

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
