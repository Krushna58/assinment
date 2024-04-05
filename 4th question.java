public class DuplicateCharacters {
    public static void main(String[] args) {
        String input = "Great responsibility";
        for (int i = 0; i < input.length(); i++) {
            char currentChar = input.charAt(i);
            if (currentChar != ' ') {
                int count = 0;
                for (int j = 0; j < input.length(); j++) {
                    if (currentChar == input.charAt(j)) {
                        count++;
                    }
                }
                if (count > 1) {
                    System.out.println(currentChar);
                }
            }
        }
    }
}
