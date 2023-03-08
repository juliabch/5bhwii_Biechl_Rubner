public class Endrekursion {
    public static void main(String[] args) {
        System.out.println("Die Fakultät von 6 ist: "+ fakultät());
    }
    public static int fakultät(){
        return multpliziereFakultät(1,6);
    }
    public static int multpliziereFakultät(int f, int n){
        if(n == 1 || n == 0){
            return f;
        }
        return multpliziereFakultät(f*n,n-1);
    }
}