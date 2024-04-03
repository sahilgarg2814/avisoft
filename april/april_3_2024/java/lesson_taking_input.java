import java.util.Scanner;
public class lesson_taking_input {
    public static void main(String[] args){
        System.out.println("Taking input from the user");
        Scanner sc= new Scanner(System.in);
        System.out.println("Number 1");
        int a = sc.nextInt();
        System.out.println("Number 2");
        int b = sc.nextInt();
        int sum = a + b;
        System.out.println(sum);
        boolean b1=sc.hasNextInt();
        System.out.println(b1);
        String str1=sc.next();
        String str2=sc.nextLine();
        System.out.println(str1);
        System.out.println(str2);
    }
}
