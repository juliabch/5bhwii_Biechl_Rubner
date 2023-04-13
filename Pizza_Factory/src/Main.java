public class Main {
    public static void main(String[] args) {

        APizza b = PizzaFactory.getPizza(Location.Berlin, Topping.Calzone);

        b.Prepare();
        b.Cut();
        b.Packaging();

        System.out.println(b);


    }
}
