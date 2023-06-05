public class TwoDstring {
	public static void main(String[] args) {


		String[][] array = new String[3][2];

		array[0][0] = "hello";
		array[0][1] = "world";
		array[1][0] = "java";
		array[1][1] = "programming";
		array[2][0] = "python";
		array[2][1] = "machine learning";

		for(int i= 0; i< array.length; i++) {
			for (int j= 0; j<array[0].length; j++) {
				System.out.println(array[i][j]);
			}
		}
	}
}