import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;


public class UNOGame {
	
	public void clearConsole() {
		/* ANSI BASED SCREEN CLEAR */
	    System.out.print("\033[H\033[2J");
	    System.out.flush();

		/* PLATFORM BASED SCREEN CLEAR */
		try {
			final String os = System.getProperty("os.name");

			if (os.contains("Windows")) {
				new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
			} else { // Assume Unix-like systems (Linux, macOS)
				new ProcessBuilder("clear").inheritIO().start().waitFor();
			}
		} catch (final Exception e) {
			// Handle exceptions, e.g., print an error message
			e.printStackTrace();
		}
	}
	
	public void startGame(Scanner sc) {
		UNODeck deck = new UNODeck();
		
		deck.shuffle();
		
		List<UNOCard> stack = new ArrayList<>();
		//Starting card cannot be a wild draw 4 card
		while(deck.deck.get(deck.deck.size()-1).getValue() == 14) {
			deck.shuffle();
		}
		
		stack.add(deck.deck.get(deck.deck.size()-1));
		deck.deck.remove(deck.deck.size()-1);
		
		int playerCount = 2;
		List<UNOHand> players = new ArrayList<>();
		
		for(int i=0; i<playerCount; i++) {
			List<UNOCard> hand = new ArrayList<>();
			for(int j=0; j<7; j++) {
				hand.add(deck.deck.get(deck.deck.size()-1));
				deck.deck.remove(deck.deck.size()-1);
			}
			players.add(new UNOHand(hand));
		}
		
		int playerTurn = 0; //when playerTurn = 0, player 1 starts
		int direction = 1;
		boolean playGame = true;
		
		
		while(playGame) {
			clearConsole();
			System.out.println("Player " + (playerTurn+1) + "'s turn: press Enter to continue");
			sc.nextLine();
			
			System.out.println("Opponent(s) card count:");
			for(int j=0; j<playerCount; j++) {
				if(j != playerTurn) {
					System.out.println("- Player " + (j+1) + ": " + players.get(j).hand.size() + " cards");
				}	
			}
			
			System.out.println("\nTop card: " + stack.get(stack.size()-1).toString());
			UNOCard topCard = stack.get(stack.size()-1);
			
			List<UNOCard> handCards = players.get(playerTurn).hand;
			
			
			if(topCard.getValue() == 12 && (!UNOCard.isPlayed(topCard))) {
				topCard.setCardToPlayed();
				System.out.println("\nDraw 2 cards!");
				
				System.out.println("First card: " + deck.deck.get(deck.deck.size()-1));
				handCards.add(deck.deck.get(deck.deck.size()-1));
				deck.deck.remove(deck.deck.size()-1);
				
				System.out.println("Second card: " + deck.deck.get(deck.deck.size()-1));
				handCards.add(deck.deck.get(deck.deck.size()-1));
				deck.deck.remove(deck.deck.size()-1);
				
			} else if(topCard.getValue() == 14 && (!UNOCard.isPlayed(topCard))) {
				topCard.setCardToPlayed();
				System.out.println("\nDraw 4 cards!");
				for(int j=0; j<4; j++) {
					System.out.println("Card " + j + ": " + deck.deck.get(deck.deck.size()-1));
					handCards.add(deck.deck.get(deck.deck.size()-1));
					deck.deck.remove(deck.deck.size()-1);
				}
			}
			
		

			System.out.println("\nYour cards: ");
			
			boolean playableCards = false;
			for(int i = 0; i<handCards.size(); i++) {
				if (UNOCard.isPlayable(handCards.get(i), stack.get(stack.size()-1))) { 
					System.out.println((i+1) + ". " + handCards.get(i).toString() + " ✅");
					playableCards = true;
				} else {
					System.out.println((i+1) + ". " + handCards.get(i).toString() + " ❌");
				}
				
			}
			
			int cardNum = 0;
			
			if(playableCards) {
				while (true) {
				    System.out.println("\nWhat card do you want to play? (1-" + handCards.size() + "): ");
				    

				    if (!sc.hasNextInt()) {
				  
				        System.out.println("Sorry, please enter a number.");
				        sc.next(); 
				        continue;
				    }
				    cardNum = sc.nextInt();
				    
				    if (cardNum < 1 || cardNum > handCards.size()) {
				        System.out.println("That card number is out of range.");
				        continue;
				    }

				    if (!UNOCard.isPlayable(handCards.get(cardNum - 1), topCard)) {
				        System.out.println("That card cannot be played on the top card.");
				        continue;
				    }
				    break;
				}
				sc.nextLine();
				
			} else {
				System.out.println("\nThere are no playable cards. Drawing a card from the deck...");
				System.out.println("Card drawed: " + deck.deck.get(deck.deck.size()-1));
				handCards.add(deck.deck.get(deck.deck.size()-1));
				deck.deck.remove(deck.deck.size()-1);
				try {
				    Thread.sleep(2000);
				} catch (InterruptedException e) {
				    e.printStackTrace();
				}
				
				
				boolean playDrawnCard = false;
				if(UNOCard.isPlayable(handCards.get(handCards.size()-1), topCard)) {
					System.out.println("The card drawn is playable, do you want to play it? (y/n): ");
					String response = sc.nextLine();
					if(response.equals("y") || response.equals("yes")) {
						playDrawnCard = true;
						System.out.println("Card played!");
						try {
						    Thread.sleep(2000);
						} catch (InterruptedException e) {
						    e.printStackTrace();
						}
						cardNum = handCards.size();
						
					}
				} else {
					System.out.println("Press Enter to end your turn");
					sc.nextLine();
					
				}
				
				if(!playDrawnCard) {
					if(direction==1) {
						playerTurn++;
					} else {
						playerTurn--;
					}
					
					if(playerTurn == playerCount) {
						playerTurn = 0;
					} else if (playerTurn == -1) {
						playerTurn = playerCount-1;
					}
					
					continue;
					
				}
				
				
			}
			
			if((cardNum == 1) && (handCards.size() == 1)) {
				clearConsole();
				System.out.println("Player " + (playerTurn+1) + " wins!");
				playGame = false;
				continue;
			}
			
			
			
			int cardValue = handCards.get(cardNum-1).getValue();
			
			if(handCards.get(cardNum-1).getValue() > 12) {
				System.out.println("What color are you picking? (red, yellow, green, blue): ");
				String chosenColor = sc.nextLine();
				while(!(chosenColor.equals("red") || chosenColor.equals("yellow") || chosenColor.equals("green") || chosenColor.equals("blue" ))) {
					System.out.println("Sorry, please enter a valid UNO color: ");
					chosenColor = sc.nextLine().trim();
				}
				stack.add(new UNOCard(handCards.get(cardNum-1).getValue(), chosenColor));
				
			} else {
				stack.add(handCards.get(cardNum-1));
				
			}
			handCards.remove(cardNum-1);
			
			if(handCards.size() == 1) {
				System.out.println("Good job getting UNO!");
				try {
				    Thread.sleep(2000);
				} catch (InterruptedException e) {
				    e.printStackTrace();
				}
			}
			
			
			if(cardValue == 11 && playerCount == 2) { //cardValue 11 is reverse
				continue;
			}
			
			if(cardValue == 10) { //cardValue 10 is skip
				playerTurn += direction*2; 
			} else {
				playerTurn += direction;
			}
			
			if(playerTurn > (playerCount-1)) {
				playerTurn = playerTurn - playerCount;
			} else if (playerTurn < 0) {
				playerTurn = playerCount + playerTurn;
			}
			
		}
		
		
		
	}
	

}
