

public class TwoDarray {

	public static void main(String[] args) {
		int[][] numbers = new int[3][2];

		numbers[0][0] = 10;
		numbers[0][1] = 11;
		numbers[1][0] = 12;
		numbers[1][1] = 13;
		numbers[2][0] = 14;
		numbers[2][1] = 15;

		for(int i=0; i< numbers.length; i++) {
			for(int j= 0; j< numbers[i].length; j++){
				System.out.println(numbers[i][j]);
				
			}
		}
	}
}