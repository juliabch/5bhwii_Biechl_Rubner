public class Main {
    public static void main(String[] args) {

        ACuvert a4 = CuvertFactory.getCuvert(Size.A4, "15x18", 192);
        ACuvert a5 = CuvertFactory.getCuvert(Size.A5, "192x27", 278);
        ACuvert a6 = CuvertFactory.getCuvert(Size.A6, "26x82", 6.4);

        System.out.println(a4);
        System.out.println(a5);
        System.out.println(a6);
    }
}
