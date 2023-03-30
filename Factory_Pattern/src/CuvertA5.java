public class CuvertA5 extends ACuvert {
    private Size size;
    private String measure;
    private double weight;

    public CuvertA5(Size s, String m, double w){
        this.size = s;
        this.measure = m;
        this.weight = w;
    }

    @Override
    public Size getSize() {
        return this.size;
    }

    @Override
    public String getMeasure(){
        return this.measure;
    }

    @Override
    public double getWeight(){
        return this.weight;
    }
}
