package Models;

public class PrinterBlackWhite implements IPrinter {

    @Override
    public void print(int pageCount) {
        System.out.printf("Printing %d page(s) in Black and White...", pageCount);
    }

    @Override
    public void print(int pageCount, PrinterOptions options){
        print(pageCount);
    }

}
