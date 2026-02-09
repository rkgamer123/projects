
import java.util.Scanner;

public class UNORunner {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		UNOGame game = new UNOGame();
		game.startGame(sc);
		
	}
}
