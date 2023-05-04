public class main {
    public static void main(String[] args) {

        Weather weather = new Weather();
        PushClient c1 = new Client1();
        PushClient c2 = new Client2();

        weather.addClient(c1);
        weather.addClient(c2);

        weather.setHumidity(50);
        weather.setTemperature(29);
        weather.removeClient(c2);
        weather.setWindSpeed(35);
    }



}