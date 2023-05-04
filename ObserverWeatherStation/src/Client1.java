public class Client1 implements PushClient{
    @Override
    public void update(int humidity, int temperature, int windSpeed) {
        System.out.println(getClass().getSimpleName());
        if (temperature >= 25){
            System.out.println("Temperatur: rot");
        }
        else if((temperature >=10)){
            System.out.println("Temperatur: gelb");
        }
        if(humidity >= 80){
            System.out.println("Hohe Luftfeuchtigkeit");
        }
        else if((humidity >= 60)){
            System.out.println("erhöhte Luftfeuchtigkeit");
        }
        else if(humidity >= 40){
            System.out.println("normale Luftfeuchtigkeit");
        }
        else{
            System.out.println("niedrige Luftfeuchtigkeit");
        }
        if(windSpeed > 30){
            System.out.println("Windgeschwindigkeit: ALLLLLAAAAAAAARRRRRRRRRMMMMMMMMM");
        }
        else if(windSpeed > 15){
            System.out.println("Windgeschwindigkeit: Warnung");
        }
        else{
            System.out.println("Windgeschwindigkeit: niedrig");
        }
    }
}
