public class CuvertFactory {
    public static ACuvert getCuvert(Size size, String measure, double weight){
        if (size == Size.A4){
            return new CuvertA4(size, measure, weight);
        }
        else if (size == Size.A5){
            return new CuvertA5(size, measure, weight);
        }
        else if (size == Size.A6){
            return new CuvertA6(size, measure, weight);
        }

        return null;

    }

}
