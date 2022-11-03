public class RekursiveSummenformel {

    public static void main(String[] args) {
        System.out.println("Summenformel von 6:");
        System.out.println(summe(6));
    }

    public static int summe(int n){
        if (n == 1){
            return 1;
        } else {
            return n + summe(n-1);
        }
    }
}
