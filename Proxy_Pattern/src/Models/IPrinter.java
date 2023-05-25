package Models;

public interface IPrinter {

    public void print(int pageCount) throws Exception;

    public void print(int pageCount, PrinterOptions options) throws Exception;

}
