class april_4_2024{
      
    public static boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;
        
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false; // If characters at current positions don't match, it's not a palindrome
            }
            left++;
            right--;
        }
        
        return true; // If the loop completes without finding any mismatch, it's a palindrome
    }

    public static int[] countVowelsAndConsonants(String str) {
        int[] counts = new int[2]; // Index 0 for vowels count, index 1 for consonants count
        
        // Convert the string to lowercase to make case-insensitive comparisons
        str = str.toLowerCase();
        
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            // Check if the character is a letter
            if (Character.isLetter(ch)) {
                // Check if the letter is a vowel
                if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                    counts[0]++; // Increment vowels count
                } else {
                    counts[1]++; // Increment consonants count
                }
            }
        }
        
        return counts;
    }

    public static void main(String[] args){
        String str="Hello World";
        int[] counts= countVowelsAndConsonants(str);
        System.out.println("Number of vowels: "+ counts[0]);
        System.out.println("Number of consonants: " + counts[1]);

        String str1 = "racecar"; // Example string
        if (isPalindrome(str1)) {
            System.out.println(str1 + " is a palindrome.");
        } else {
            System.out.println(str1 + " is not a palindrome.");
        }
    }

    
    }
