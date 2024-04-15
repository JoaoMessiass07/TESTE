package bgg;

import java.util.List;

public abstract class Game {
    private String name;
    private int yearLaunched;
    private int minPlayers;
    private int maxPlayers;
    private int bestNumPlayers;
    private int meanPlayTime;
    private int minAge;
    private double meanRatings;
    private List<Rating> ratings;

    public Game() {
    }

    public Game(String name, int yearLaunched, int minPlayers, int maxPlayers,
                int bestNumPlayers, int meanPlayTime, int minAge,
                List<Rating> ratings) {
        this.name = name;
        this.yearLaunched = yearLaunched;
        this.minPlayers = minPlayers;
        this.maxPlayers = maxPlayers;
        this.bestNumPlayers = bestNumPlayers;
        this.meanPlayTime = meanPlayTime;
        this.minAge = minAge;
        this.ratings = ratings;
        this.meanRatings = calculateMeanRatings();
    }

    private double calculateMeanRatings() {
        return ratings.stream()
                .mapToDouble(Rating::getRating)
                .average()
                .orElse(0);
    }
}
