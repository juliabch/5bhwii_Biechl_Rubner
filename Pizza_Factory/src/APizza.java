public abstract class APizza {

    private APizzeria l;

    public String Prepare(){ return "Preparation finished!";}
    public String Cut(){ return "Cutting finished!";}
    public String Packaging(){ return "Packaging finished";}


    public APizzeria getLocation(APizzeria location){
        return this.l = location;
    };

    public APizza(APizzeria location){
        this.l = location;
    }


}
