public class PizzeriaHamburg extends APizzeria {
    private String location = "Hamburg";

    public String getLocation(){
        return this.location;
    }

    public PizzeriaHamburg(String l){
        super(l);
    }

    public String toString(){
        return "Location: " + this.getLocation(location);
    }

}
