package main.java;

import java.util.*;

public class StackApplications {
    StackI stackLL = new MyStackLL();

    public static void main(String [] args){

        StackApplications sApplication = new StackApplications();
        System.out.println("String reversal w stack");

        sApplication.reverseString("Palindrome");
        sApplication.reverseString("Lahore");

        /////////////////////////////////////////////////////////////

        System.out.println("char array reversal w/o stack");

        char[] str = {'W', 'a', 's','h', 'i', 'n', 'g', 't', 'o', 'n'};
        sApplication.reverseStringWithoutStack(str);

        str = new char[]{'L', 'a', 'h', 'o', 'r', 'e'};
        sApplication.reverseStringWithoutStack(str);

        /////////////////////////////////////////////////////////////

//        System.out.println("()  ==> "+ sApplication.balancedParenthesis("()"));
//        System.out.println(")(  ==> "+ sApplication.balancedParenthesis(")("));
//        System.out.println("[()]  ==> "+ sApplication.balancedParenthesis("[()]"));
//        System.out.println("[(])  ==> "+ sApplication.balancedParenthesis("[(])"));
//        System.out.println("[(){}]  ==> "+ sApplication.balancedParenthesis("[(){}]"));
//        System.out.println("[](){}  ==> "+ sApplication.balancedParenthesis("[](){}"));
//        System.out.println("{)}  ==> "+ sApplication.balancedParenthesis("{)}"));



        System.out.println("  ==> "+ sApplication.isBalanced(""));
        System.out.println("()  ==> "+ sApplication.isBalanced("()"));
        System.out.println(")(  ==> "+ sApplication.isBalanced(")("));
        System.out.println("[()]  ==> "+ sApplication.isBalanced("[()]"));
        System.out.println("[(])  ==> "+ sApplication.isBalanced("[(])"));
        System.out.println("[(){}]  ==> "+ sApplication.isBalanced("[(){}]"));
        System.out.println("[](){}  ==> "+ sApplication.isBalanced("[](){}"));
        System.out.println("{)}  ==> "+ sApplication.isBalanced("{)}"));



        System.out.println("<<<<<<Infix to Postfix >>>>>>>>>");
        System.out.println("a+b ==>  " + sApplication.infixToPostfix("a+b"));
        System.out.println("a+b*c ==>  " + sApplication.infixToPostfix("a+b*c"));
        System.out.println("a+b*c+d ==>  " + sApplication.infixToPostfix("a+b*c+d"));
        System.out.println("empty string ==>  " + sApplication.infixToPostfix(""));
        System.out.println("null string ==>  " + sApplication.infixToPostfix(null));
        System.out.println("a+b*c/d ==>  " + sApplication.infixToPostfix("a+b*c/d"));
        System.out.println("a+b-c+d ==>  " + sApplication.infixToPostfix("a+b-c+d"));


        System.out.println("<<<<<<<< Evaluate Postfix Notion >>>>>>>>");
        String exp = "2+2*3";
        String postfix = sApplication.infixToPostfix(exp);
        System.out.println(exp + " ==> " + postfix + " ==> "+ sApplication.evaluatePostfix(postfix));
        exp = "2+2*3+2";
        System.out.println(exp + " ==> " + sApplication.infixToPostfix(exp) + " ==> "+ sApplication.evaluatePostfix(sApplication.infixToPostfix(exp)));

        System.out.println("null ==> " + sApplication.infixToPostfix(null) + " ==> "+ sApplication.evaluatePostfix(null));


    }

    int evaluatePostfix(String exp){

        List operands = new ArrayList();
        operands.add("*");
        operands.add("/");
        operands.add("+");
        operands.add("-");

        Stack<String> stack = new Stack<String>();

        if (exp != null && !exp.isEmpty()){

            for (int i = 0 ; i < exp.length(); i++){
                String curr = String.valueOf(exp.charAt(i));

                if(operands.contains(curr)){
                    int op1 = Integer.parseInt(stack.pop());
                    int op2 = Integer.parseInt(stack.pop());
                    int result = 0;

                    switch (curr){
                        case "*":
                            result = op1 *op2;
                            break;
                        case "/":
                            result = op1 / op2;
                            break;
                        case "+":
                            result = op1 + op2;
                            break;
                        case "-":
                            result = op1 - op2;
                            break;
                         default:
                            break;
                    }
                    stack.push(Integer.toString(result));
                }else{
                    stack.push(curr);
                }
            }
        }

        return stack.isEmpty()? -99 : Integer.parseInt(stack.pop());
    }

    /**
     *  Infix to Postfix Notation
     *
     *  Assumptions:
     *      >> Single digit operation
     *      >> + , -, *, /
     *
     *  Test Cases:
     *  a + b  ==> a b +
     *  a + b * c  ==> a b c * +
     *  a + b * c - e  ==> a b c * + e -
     *  a + b / c  ==> a b c / +
     *  + b c --> error
     * */

    String infixToPostfix(String exp){
        Stack<String>  symbolStack = new Stack<String>();

        Map<String, Integer> operatorOrder = new HashMap<>();

        operatorOrder.put("*", 2);
        operatorOrder.put("/", 2);
        operatorOrder.put("+", 1);
        operatorOrder.put("-", 1);

//        String[] infixExp = new String[exp.length()];
        StringBuffer postFixExp = new StringBuffer();


        if (exp != null && !exp.isEmpty()){

            for (int i = 0 ; i < exp.length(); i++){

                String curr = String.valueOf(exp.charAt(i));

                if (operatorOrder.keySet().contains(curr)){ //operator


                    if (!symbolStack.isEmpty()) {

                        String last = symbolStack.peek();

                        //equal precedence ==> pop from top of stcak and use it and push the currenet one
                        //curr precedence > last then use the curr and p

                        if (operatorOrder.get(curr) > operatorOrder.get(last)) {
                            symbolStack.push(curr);
                        } else if (operatorOrder.get(curr) <= operatorOrder.get(last)){
                            while(!symbolStack.isEmpty())
                                postFixExp.append(symbolStack.pop());

                            symbolStack.push(curr);
                        }
                    }else {
                        symbolStack.push(curr);
                    }

                }else {
                    postFixExp.append(curr);
                }
            }

            while(!symbolStack.isEmpty())
                postFixExp.append(symbolStack.pop());

        }

        return postFixExp.toString();

    }

    boolean isBalanced(String exp){

        String [] openSymbols = {"{", "[", "("};
        String [] closeSymbols = {"}", "]", ")"};

        Map<String,String> mapping  = new HashMap<String,String>();
        mapping.put("(", ")");
        mapping.put("{", "}");
        mapping.put("[", "]");


        Stack<String> stack = new Stack<String>();

        if(exp != null && !exp.isEmpty()){

            for (int i = 0 ; i < exp.length(); i++){
                String curr = String.valueOf(exp.charAt(i));
                if (Arrays.asList(openSymbols).contains(curr)){
                    stack.push(curr);
                }else if (Arrays.asList(closeSymbols).contains(curr)){
                    if (stack.isEmpty())
                        return false;

                   String top = stack.peek();

                   if (curr.equals(mapping.get(top))){
                       stack.pop();
                   }
                   else
                       return false;
                }
            }


            if (stack.isEmpty())
                return true;
        }

        return false;
    }

    boolean balancedParenthesis(String exp){

        /*
        *    ()  --> Balanced
        *    )(  --> NO
        *   [()]  --> Yes
        *  [(])     --> No
        *  [()()]  --> Yes
        * */

        //opening symbol --> { ,[, (
        //closing symbol --> } ,], )

        Map<String,String> symbolMapping = new HashMap<String,String>();
        symbolMapping.put("(", ")");
        symbolMapping.put(")", "(");
        symbolMapping.put("{", "}");
        symbolMapping.put("}", "{");
        symbolMapping.put("[", "]");
        symbolMapping.put("]", "[");

//        List openSymbol = Arrays.asList("(", "{", "[");
//        List closeSymbol = Arrays.asList(")", "}", "]");
        String []  openSymbol = {"(", "{", "["};
        String [] closeSymbol = {")", "}", "]"};

        Stack pStack = new Stack();

        for (int i = 0 ; i < exp.length(); i++){

            String curr = Character.toString(exp.charAt(i));

            if (Arrays.asList(openSymbol).contains(curr)) { //opening symbol in valid opening symbols
                pStack.push(curr);
            }else if (Arrays.asList(closeSymbol).contains(curr)){ //closing symbol in valid opening symbols

                if (pStack.isEmpty()) //at this point must have at least one matching opening entry
                    return false;

                String expectedOpenTag = symbolMapping.get(curr);

                if (expectedOpenTag.equals(pStack.peek())){
                    pStack.pop();
                }else {
                    return false;
                }

            }
            else{ //not a valid symbol
                return false;
            }
        }

        return pStack.isEmpty();
    }


    void reverseStringWithoutStack(char[] str){
        int j = str.length-1;
        int i = 0;

        while (i <= j){

            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
            i++;
            j--;
        }
        System.out.println(str);

    }


    //Time Complexity O(n)
    //Space Complexity O(n) --> n = number of characters in the string
    void reverseString(String name){

        for(int i =0; i < name.length() ; i++){
//            System.out.println(name.charAt(i));
            stackLL.push(name.charAt(i)); // O(1)

        }

        for (int i =0; i < name.length(); i++){
//            System.out.print((char)sApplication.stackLL.pop());
            System.out.print((char)stackLL.pop());  //O(1)

        }

        System.out.println();
    }
}

class Symbol {
    String open;
    String close;

    Symbol(String c, String o){
        close = c;
        open = o;
    }
}