public class PizzaFactory {

    private static APizzeria Berlin = new PizzeriaBerlin("Berlin");
    private static APizzeria Hamburg = new PizzeriaHamburg("Hamburg");
    private static APizzeria Rostock = new PizzeriaRostock("Rostock");

    public static APizza getPizza(Enum l, Enum t){
        if(t == Topping.Salami){
            if (l == Location.Berlin) {return new PizzaSalami(Berlin);}
            else if (l == Location.Hamburg) {return new PizzaSalami(Hamburg);}
            else if (l == Location.Rostock) {return new PizzaSalami(Rostock);}
        }
        else if(t == Topping.Ananas){
            if (l == Location.Berlin) {return new PizzaAnanas(Berlin);}
            else if (l == Location.Hamburg) {return new PizzaAnanas(Hamburg);}
            else if (l == Location.Rostock) {return new PizzaAnanas(Rostock);}
        }
        else if(t == Topping.Calzone){
            if (l == Location.Berlin) {return new PizzaCalzone(Berlin);}
            else if (l == Location.Hamburg) {return new PizzaCalzone(Hamburg);}
            else if (l == Location.Rostock) {return new PizzaCalzone(Rostock);}
        }

        return null;
    }

}
