package main.java;

import java.lang.reflect.Array;
import java.util.*;

public class MyGraph {

    private Map<String, List> adjList = null;

    public MyGraph(){
        adjList = new HashMap<>();
    }

    void addVertex(String vertex ){
        adjList.put(vertex, new ArrayList());
    }

    void addEdge(String fromVertex, String toVertex){
        List edges1 = adjList.get(fromVertex);

        edges1.add(toVertex);

        List edges2 = adjList.get(toVertex);

        edges2.add(fromVertex);

    }

    void printEdges(){

        for(String key : adjList.keySet()){

            List<String> edges = adjList.get(key);
            if (edges != null) {
                for (String vertex : edges) {
                    System.out.print(" (" + key + ", " + vertex + ") ");
                }
            }
        }
    }

    public static  void main(String [] args){

        MyGraph graph = new MyGraph();

        graph.addVertex("a");
        graph.addVertex("b");
        graph.addVertex("c");

        graph.addEdge("a", "b");
        graph.addEdge("a", "c");
        graph.addEdge("b", "c");


        graph.printEdges();

    }
}
