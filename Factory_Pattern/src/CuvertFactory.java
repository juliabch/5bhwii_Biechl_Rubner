public class CuvertFactory {
    public static ACuvert getCuvert(String size, String measure, double weight){
        if ("A4".equalsIgnoreCase(size)){
            return new CuvertA4(size, measure, weight);
        }
        else if ("A5".equalsIgnoreCase(size)){
            return new CuvertA5(size, measure, weight);
        }
        else if ("A6".equalsIgnoreCase(size)){
            return new CuvertA6(size, measure, weight);
        }

        return null;

    }

}
