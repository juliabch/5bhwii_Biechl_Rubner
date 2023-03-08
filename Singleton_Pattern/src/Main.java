public class Main {
    static Printer p = Printer.getPrinter();
    static Printer p2 = Printer.getPrinter();

    public static void main(String[] args) {
        System.out.println(p.print());
        System.out.println(p2.print());
    }
}
