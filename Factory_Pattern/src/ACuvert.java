public abstract class ACuvert {

    public abstract String getSize();
    public abstract String getMeasure();
    public abstract double getWeight();

    @Override
    public String toString(){
        return "Size: " + this.getSize() + "\n" + "Measurements: " + this.getMeasure() + "mm" + "\n" + "Weight: " + this.getWeight() + "g\n";
    }
}
