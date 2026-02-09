import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class UNODeck {
	public List<UNOCard> deck = new ArrayList<>();
	private final String[] colors = {"red", "yellow", "green", "blue"};
	
	public UNODeck() {		
		for(int c=0; c<4; c++) {
			deck.add(new UNOCard(0, colors[c]));
			for(int j=1; j<10; j++) {
				deck.add(new UNOCard(j, colors[c]));
			}
			for(int j=1; j<10; j++) {
				deck.add(new UNOCard(j, colors[c]));
			}
		}
		for(int actionNum=10; actionNum<13; actionNum++) {
			for(int c=0; c<4; c++) {
				deck.add(new UNOCard(actionNum, colors[c]));
				deck.add(new UNOCard(actionNum, colors[c]));
			}
		}
		for(int j=0; j<4; j++) {
			deck.add(new UNOCard(13, ""));
		}
		for(int j=0; j<4; j++) {
			deck.add(new UNOCard(14, ""));
		}
	}
	
	public void shuffle() {
		Collections.shuffle(deck);
	}
	

}
