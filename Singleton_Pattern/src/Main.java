public class Main {
    static Printer p = Printer.getPrinter();
    static Printer p2 = Printer.getPrinter();

    public static void main(String[] args) {
        System.out.println(p.print());
        System.out.println("Hashcode von printer 1: "+ p.hashCode());
        System.out.println(p2.print());
        System.out.println("Hashcode von printer 2: "+ p2.hashCode());
    }
}
