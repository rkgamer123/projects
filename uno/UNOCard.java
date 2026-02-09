//Total: 108 cards
//Red, Yellow, Green, and Blue: two sets of 1-9, and one 0
//Action cards: 2 skip, 2 reverse, 2 draw two for each color
//4 wild cards
//4 wild draw four cards

//10: skip
//11: reverse
//12: draw 2
//13: wild card
//14: wild draw 4


public class UNOCard {
	
	public final String ANSI_RED = "\u001B[31m";
	public final String ANSI_GREEN = "\u001B[32m";
	public final String ANSI_YELLOW = "\u001B[33m";
	public final String ANSI_BLUE = "\u001B[34m";
	public final String ANSI_RST = "\u001B[0m";
	
	private int value;
	private String color;
	
	private boolean playedCard = false; //boolean to check if a plus 4 or plus 2 was already played
	
	public UNOCard(int value, String color) {
		this.value = value;
		this.color = color;
	}
	
	public int getValue() {
		return value;
	}
	
	public void setValue(int value) {
		this.value = value;
	}
	
	public String getColor() {
		return color;
	}
	
	public void setColor(String color) {
		this.color = color;
	}
	
	public void setCardToPlayed() {
		playedCard = true;
	}
	
	public static boolean isPlayed(UNOCard card) {
		return card.playedCard;
	}
	
	
	public static boolean isPlayable(UNOCard playingCard, UNOCard topCard) {
		if(playingCard.getValue() < 13) { //1-9, and 10,11,12
			if((playingCard.getColor().equals(topCard.getColor())) || topCard.getColor().equals("") || (playingCard.getValue() == topCard.getValue())) {
				return true;
			}
			return false;
		} else {
			return true;
		}
		
	}
	
	private String colorToCode(String color) {
		if(color.equals("red")) {
			return ANSI_RED;
		}
		if(color.equals("yellow")) {
			return ANSI_YELLOW;
		}
		if(color.equals("green")) {
			return ANSI_GREEN;
		}
		if(color.equals("blue")) {
			return ANSI_BLUE;
		}
		return "";
	}
	
	public String toString() {
		if(value < 10) {
			return colorToCode(color) + color + " " + value + ANSI_RST;
		} else {
			if (value == 10) {
				return colorToCode(color) + color + " skip" + ANSI_RST;
			}
			if (value == 11) {
				return colorToCode(color) + color + " reverse" + ANSI_RST;
			}
			if (value == 12) {
				return colorToCode(color) + color + " draw 2" + ANSI_RST;
			}
			if (value == 13) {
				if(color.equals("")) {
					return "wild card";
				} else {
					return colorToCode(color) + color + " wild card" + ANSI_RST;
				}
				
			}
			if (value == 14) {
				
				if(color.equals("")) {
					return "wild draw 4";
				} else {
					return colorToCode(color) + color + " wild draw 4" + ANSI_RST;
				}
				
			}
			return "";			
			
		}
		
		
				
	}
	
	public static void main(String args[]) {
		UNOCard topCard = new UNOCard(14, "green");
		topCard.setCardToPlayed();
		System.out.print(UNOCard.isPlayable(new UNOCard(12,"green"), topCard));
		    
	}
	
	
}
