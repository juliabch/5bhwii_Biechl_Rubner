public class PizzeriaBerlin extends APizzeria {
    private String location = "Berlin";

    public String getLocation(){
        return this.location;
    }

    public PizzeriaBerlin(String l){
        super(l);
    }

    public String toString(){
        return "Location: " + this.getLocation(location);
    }

}
