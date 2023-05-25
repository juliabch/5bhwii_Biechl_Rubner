package Models;

public class PrinterColor implements IPrinter {

    @Override
    public void print(int pageCount) {
        System.out.printf("Printing %d page(s) in color...", pageCount);
    }

    @Override
    public void print(int pageCount, PrinterOptions options){
        print(pageCount);
    }

}
