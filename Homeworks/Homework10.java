public class Homework10 {
  public boolean check(char[] correctPositions, String word)   {
    boolean bool = true; //boolean variable

    for (int i = 0; i < correctPositions.length; i++) {

      if (word.charAt(i) == correctPositions[i]) { //check if word at position i is equal to char at correctPositions[i]
        bool = true; // bool is true
      } else if (correctPositions[i] == '*') { //If correctPositions at position i is * then bool is true
        bool = true;
      } else {
        return false; // bool will return false if the other statements where false
      }
    }

    return bool; // return variable
  }
}
