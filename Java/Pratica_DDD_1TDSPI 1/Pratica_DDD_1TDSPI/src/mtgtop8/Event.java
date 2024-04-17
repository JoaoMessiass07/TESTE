package mtgtop8;

import java.time.LocalDateTime;
import java.util.List;

public class Event {
    private String name;
    private MTG_FORMAT format;
    private LocalDateTime date;
    private List<TournamentPlayer> players;
    private int rating;
    private String location;

    public Event() {

    }
    public Event(String name, MTG_FORMAT format, LocalDateTime date, List<TournamentPlayer> players, int rating, String location) {
        this.name = name;
        this.format = format;
        this.date = date;
        this.players = players;
        this.rating = rating;
        this.location = location;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MTG_FORMAT getFormat() {
        return format;
    }

    public void setFormat(MTG_FORMAT format) {
        this.format = format;
    }

    public LocalDateTime getDate() {
        return date;
    }

    public void setDate(LocalDateTime date) {
        this.date = date;
    }

    public List<TournamentPlayer> getPlayers() {
        return players;
    }

    public void setPlayers(List<TournamentPlayer> players) {
        this.players = players;
    }

    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    @Override
    public String toString() {
        return "Event{" +
                "name='" + name + '\'' +
                ", format=" + format +
                ", date=" + date +
                ", players=" + players +
                ", rating=" + rating +
                ", location='" + location + '\'' +
                '}';
    }
}
