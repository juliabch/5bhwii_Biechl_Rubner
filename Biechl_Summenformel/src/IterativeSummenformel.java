public class IterativeSummenformel {
    public static void main(String[] args) {
        System.out.println("Summenformel von 6: ");
        System.out.println(summe(6));
    }

    public static int summe(int n){
        int sum = 1;
        while(n > 1){
            sum = sum + n;
            n--;
        }
        return sum;
    }
}