public class PizzaCalzone extends APizza {
    private String topping;
    private APizzeria location;

    public PizzaCalzone(APizzeria l){
        super(l);
    }

    public String getTopping(){
        return this.topping;
    }

    @Override
    public String toString(){
        return "Topping: " + this.getTopping() + "\n" + "Location: " + this.getLocation(location) + "\n";
    }
}
