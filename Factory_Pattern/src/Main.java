public class Main {
    public static void main(String[] args) {

        ACuvert a4 = CuvertFactory.getCuvert("a4", "15x18", 192);
        ACuvert a5 = CuvertFactory.getCuvert("a5", "192x27", 278);
        ACuvert a6 = CuvertFactory.getCuvert("a6", "26x82", 6.4);

        System.out.println(a4);
        System.out.println(a5);
        System.out.println(a6);
    }
}
