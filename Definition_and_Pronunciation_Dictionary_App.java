```java
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class DictionaryApp {
    public static void main(String[] args) {
        Map<String, String[]> dictionary = new HashMap<>();
        dictionary.put("apple", new String[]{"A round fruit with red or yellow or green skin", "æpl"});
        dictionary.put("banana", new String[]{"A long curved fruit with yellow skin", "bəˈnænə"});
        dictionary.put("cherry", new String[]{"A small round fruit with a single hard pit", "ˈtʃɛri"});

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Enter a word (or 'exit' to quit): ");
            String word = scanner.nextLine().toLowerCase();
            if (word.equals("exit")) {
                break;
            }
            if (dictionary.containsKey(word)) {
                System.out.println("Definition: " + dictionary.get(word)[0]);
                System.out.println("Pronunciation: " + dictionary.get(word)[1]);
            } else {
                System.out.println("Word not found in dictionary.");
            }
        }
        scanner.close();
    }
}
```