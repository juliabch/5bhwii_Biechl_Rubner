public class IterativeSummenformel {
    public static void main(String[] args) {

        System.out.println("Summenformel von 6: ");
        System.out.println(summe(6));
    }

    public static int summe(int n){
        int p = 1;
        while(n > 1){
            p = p + n;
            n--;
        }
        return p;
    }
}