import Models.IPrinter;
import Models.PrinterOptions;
import Models.ProxyPrinter;

public class Main {

    public static void main(String[] args) {

        IPrinter printer = new ProxyPrinter();

        try{

            printer.print(790);
        }catch (Exception e){
            e.printStackTrace();
        }



    }


}
