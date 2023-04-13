public class PizzeriaRostock extends APizzeria {
    private String location = "Rostock";

    public String getLocation(){
        return this.location;
    }

    public PizzeriaRostock(String l){
        super(l);
    }

    public String toString(){
        return "Location: " + this.getLocation(location);
    }

}
