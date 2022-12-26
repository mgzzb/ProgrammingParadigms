// Libraries Needed
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class Board{

  char[][] board_template = {{' ',' ',' '}, {' ',' ',' '}, {' ',' ',' '}}; // define the template of the board
  Set<Integer> compartments = new HashSet<> (); // define the compartments in the board
  
  public static boolean win(char[][] board_template, Set<Integer> compartments){

    if (end('O', board_template)) { // Check if board is full and won by computer
      
      System.out.println("Final Board:"); 
      boardFormat(board_template); // print board state
      System.out.println("Computer has won!"); // print who won
      
			return true; // end game
      
    }else if (end('X', board_template)) { // Check if board is full and won by player

			System.out.println("Final Board:"); 
      boardFormat(board_template); // print board state
      System.out.println("Player 1 has won!"); // print who won

			return true; // end game
      
    } else if (compartments.size() == 9) { // if board is full and no one one --> draw
      
      System.out.println("Final Board:"); 
      boardFormat(board_template); // print board state
      System.out.println("Draw!"); // print Draw

			return true; // end game
		
    }

    return false; // game did not win
    
  }

  public static void selection(char[][] board_template, int move, char player) {

    if(move == 1){ // create board based on number selection
      board_template[0][0] = player;
    }else if(move == 2){
      System.out.println("manis");
      board_template[0][1] = player;
    }else if(move == 3){
      board_template[0][2] = player;
    }else if(move == 4){
      board_template[1][0] = player;
    }else if(move == 5){
      board_template[1][1] = player;
    }else if(move == 6){
      board_template[1][2] = player;
    }else if(move == 7){
      board_template[2][0] = player;
    }else if(move == 8){
      board_template[2][1] = player;
    }else if(move == 9){
      board_template[2][2] = player;
    }

	}
  
  public static boolean end(char input, char[][] board) {

    // rows the same --> return true for win
    for( int i = 0; i < 3; i++){
      if ((board[i][0] == input) && (board[i][1] == input) && (board[i][2] == input)){
        return true;
      }
    }

    // cols the same --> return true for win
    for( int i = 0; i < 3; i++){
      if ((board[0][i] == input) && (board[1][i] == input) && (board[2][i] == input)){
        return true;
      }
    }

	 	// diag the same --> return true for win
		if ((board[0][0] == input) && (board[1][1] == input) && (board[2][2] == input))
			return true;
		if ((board[2][0] == input) && (board[1][1] == input) && (board[0][2] == input))
			return true;
		
		// return false if game not over
		return false;
	
	}

  public static void boardFormat(char[][] board) {
    
    // print the board
    System.out.println("");

    System.out.print(String.format(" %c", board[0][0]) + " | " + String.format("%c", board[0][1]) + " | " + String.format("%c ", board[0][2]) + "\n---+---+---\n");
    
    System.out.print(String.format(" %c", board[1][0]) + " | " + String.format("%c", board[1][1]) + " | " + String.format("%c ", board[1][2]) + "\n---+---+---\n");

    System.out.print(String.format(" %c", board[2][0]) + " | " + String.format("%c", board[2][1]) + " | " + String.format("%c ", board[2][2]) );
    System.out.println("\n");
        
	}

  
}