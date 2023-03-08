public class Printer {
    // private variable
    private static Printer instance;

    //private constructor
    private Printer(){}

    //public get instance
    //one instance per thread/process
    public static Printer getPrinter(){
        if(instance == null){
            instance = new Printer();
        }
        return instance;
    }

    public static String print(){
        String s ="Ich drucke und bin die Instanz vom coolen Drucker!";
        return s;
    }
}
