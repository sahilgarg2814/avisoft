import java.util.ArrayList;
import java.util.Scanner;


class april_3_2024{
      
    // Function to find maximum product pair 
    // in arr[0..n-1] 
    static void findMaxProductPair(int[] array, int size) 
    { 
        if (size < 2) 
        { 
            System.out.println("The array does not contain enough elements to form pairs."); 
            return; 
        } 
       
        // Initialize max product pair 
        int maxProductFirstElement = array[0]; 
        int maxProductSecondElement = array[1]; 
       
        // Traverse through every possible pair 
        // and keep track of max product 
        for (int i = 0; i < size; i++) 
            for (int j = i + 1; j < size; j++) 
                if (array[i] * array[j] > maxProductFirstElement * maxProductSecondElement){ 
                    maxProductFirstElement = array[i];  
                    maxProductSecondElement = array[j]; 
                } 
               
        System.out.println("Max product pair is {" + 
                           maxProductFirstElement + ", " + maxProductSecondElement + "}"); 
    } 
    public static ArrayList<Integer> primeFactors(int number) {
        ArrayList<Integer> primeFactorsList = new ArrayList<>();

        // Check for divisibility by 2
        while (number % 2 == 0) {
            primeFactorsList.add(2);
            number /= 2;
        }

        // Check for divisibility by odd numbers starting from 3
        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            while (number % i == 0) {
                primeFactorsList.add(i);
                number /= i;
            }
        }

        // If the remaining number is a prime greater than 2
        if (number > 2) {
            primeFactorsList.add(number);
        }

        return primeFactorsList;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number between 2 and 100: ");
        int number = scanner.nextInt();

        if (number < 2 || number > 100) {
            System.out.println("Number must be between 2 and 100.");
        } else {
            ArrayList<Integer> primeFactors = primeFactors(number);
            System.out.println("Prime factors of " + number + " are: " + primeFactors);
        }
        
        int[] array = {1, 4, 3, 6, 7, 0}; 
        int size = array.length; 
        findMaxProductPair(array, size);

        scanner.close();
    }

}

