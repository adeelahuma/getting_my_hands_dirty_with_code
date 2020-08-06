package main.java;

import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.Map;
import java.util.HashMap;

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

        System.out.println("()  ==> "+ sApplication.balancedParenthesis("()"));
        System.out.println(")(  ==> "+ sApplication.balancedParenthesis(")("));
        System.out.println("[()]  ==> "+ sApplication.balancedParenthesis("[()]"));
        System.out.println("[(])  ==> "+ sApplication.balancedParenthesis("[(])"));
        System.out.println("[(){}]  ==> "+ sApplication.balancedParenthesis("[(){}]"));
        System.out.println("[](){}  ==> "+ sApplication.balancedParenthesis("[](){}"));
        System.out.println("{)}  ==> "+ sApplication.balancedParenthesis("{)}"));

    }

    void evaluatePostfix(String exp){

    }

    void infixToPostfix(String exp){

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