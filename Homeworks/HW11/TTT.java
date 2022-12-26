// Libraries Needed
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class TTT {

	public static void main(String[] args) {
    
    Scanner input = new Scanner(System.in); // scanner for user input
    Board board = new Board(); // initialize board class
    boolean playing = true; // check if we can continue playing the game

		while(playing) { // check if we are still playing game to stay in loop
      
			System.out.print("Enter a value from 1-9: "); // ask user for input
			int userVal = input.nextInt(); // store value input of user

			player(board, userVal, board.compartments); // fill board for player
			board.boardFormat(board.board_template); // print current board with player input

			if (board.win(board.board_template, board.compartments)) { // check if player won or draw
        playing = false; // playing to false because game ended
        break; // break out of rest actions
      }

      comp(board, board.compartments); // fill board for computer
      board.boardFormat(board.board_template); // print current board with computer input

      if (board.win(board.board_template, board.compartments)) { // check if computer won or draw
        playing = false; // playing to false because game ended
        break; // break out of rest actions
      }

    }

	}

	public static void player(Board board, int val, Set<Integer> compartments){ // it is the players turn
		compartments.add(val); // add input to compartment 
		board.selection(board.board_template, val, 'X'); // add input to board with players mark
	}
		
	public static void comp(Board board, Set<Integer> compartments) {
		Random ran = new Random(); // initialize random 
		int val; // initialize val
    boolean findVal = true;
	
		while(findVal) { // computers turn
      
      val = (int) (ran.nextInt(9) + 1); // create random value for comp position

			// If the computerValue is not within the spaces, then play that turn and update the board
      if(!compartments.contains(val)) { // if val not in compartments then we can use value
        findVal = false; // will exit while loop
        compartments.add(val); // add value to compartments
				System.out.println(String.format("Computer Played: %d", val)); // print value chosen by computer
        board.selection(board.board_template, val, 'O'); // add computers turn to board
      }

    }

	}
			
}