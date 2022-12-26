// Libraries Needed
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class DFS {
    public List<String> traverse(String root, Map<String,List<String>> graph){

      // Initialize variables
      HashMap<String, Boolean> vNodes = new HashMap<String, Boolean>(); // Create a hash map of the nodes visited 
      List<String> dfsFinal = new ArrayList<String>(); // store values of vNodes through DFS

      for(String i : graph.keySet()){
        vNodes.put(i, false); // fill hashmap with false value
      }

      dfsearch(root, graph, vNodes, dfsFinal); // call function

      return dfsFinal; // return final array list of strings
      
    }

    public void dfsearch(String root, Map<String,List<String>> graph, HashMap<String, Boolean> vNodes, List<String> dfsFinal){
      
      dfsFinal.add(root); // add node to final array
      vNodes.put(root, true); // add node to visited nodes and change to true

      for (String node:graph.get(root)) { // get the children of the node
        if (vNodes.get(node) == false) { // check if child was visited, if false then enter if loop
          dfsearch(node, graph, vNodes, dfsFinal); // call dfsearch function to go through with the search
        }

      }
      
    }
  
  public static void main(String [] args){
    
    System.out.println("used for testing");
  }

}