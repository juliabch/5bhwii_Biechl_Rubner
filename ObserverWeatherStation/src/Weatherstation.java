import java.util.ArrayList;
import java.util.List;

public class Weatherstation {
    private List<PushClient> pushClients = new ArrayList<>();

    public void addClient(PushClient client){
        pushClients.add(client);
    }
    public void removeClient(PushClient client){
        pushClients.remove(client);
    }

    public void notify(int humidity, int temperature, int windSpeed){
        for(PushClient pc : this.pushClients){
            pc.update(humidity, temperature, windSpeed);
        }
    }

}
