package Models;

public class ProxyPrinter implements IPrinter {

    private IPrinter _printer;
    private final int MAX_COLOR_PAGES = 50;
    private final int MAX_PAGES = 500;

    @Override
    public void print(int pageCount) throws Exception {
        if(pageCount <= 0){
            throw new Exception("pages must be more than 0");
        }
        if(pageCount > MAX_PAGES){
            throw new Exception("too many pages, must be less than " + MAX_PAGES);
        }

        if(pageCount < MAX_COLOR_PAGES){
            _printer = new PrinterColor();
        }
        else {
            _printer = new PrinterBlackWhite();
        }

        _printer.print(pageCount);
    }

    @Override
    public void print(int pageCount, PrinterOptions option) throws Exception {
        if(pageCount <= 0){
            throw new Exception("pages must be more than 0");
        }
        if(pageCount > MAX_PAGES){
            throw new Exception("too many pages, must be less than " + MAX_PAGES);
        }

        if(option == PrinterOptions.color && pageCount < MAX_COLOR_PAGES){
            _printer = new PrinterColor();
        }
        else {
            _printer = new PrinterBlackWhite();
        }

        _printer.print(pageCount);
    }





}
