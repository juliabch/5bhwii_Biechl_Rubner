public class Weather extends Weatherstation {
    private int temperature;
    private int humidity;
    private int windSpeed;

    public int getWindSpeed() {
        return windSpeed;
    }

    public void setWindSpeed(int windSpeed) {
        this.windSpeed = windSpeed;
        notify(humidity, temperature, windSpeed);
    }

    public int getTemperature() {
        return temperature;
    }

    public void setTemperature(int temperature) {
        this.temperature = temperature;
        notify(humidity, temperature, windSpeed);
    }

    public int getHumidity() {
        return humidity;
    }

    public void setHumidity(int humidity) {
        this.humidity = humidity;
        notify(humidity, temperature, windSpeed);
    }
}
