/*
 * Author: Connor Heard
 * Date: 5 / 13 / 2023
 * Description: Program 05 - GameCharacter
 */

 // The GameCharacter class instantiates a player object and keeps 
 //track of their name, inventory, and health. Allows for the functionality
 // of managing the player's inventory and health stats.
 class GameCharacter {
    private String name;
    private int lives;
    private String [] inventory;
    private final int MAXLIVES = 5;
    
    // Base constructor
    public GameCharacter() {
        name = "Sam Sung";
        lives = MAXLIVES;
        inventory = new String[5];

    }

    // Overloaded Constructor recieves both a name and the number of lives of player
    public GameCharacter(String name, int lives) {
        this.name = name;
        if (lives >= 0 && lives <= MAXLIVES){
            this.lives = lives;
        }
        else{
            this.lives = MAXLIVES;
        }

        inventory = new String[5];

    }

    // Getters amd Setters for all instance variables
    public String getName() {
        return name;
    }

    public void setName(String val) {
        name = val;
    }

    public int getLives() {
        return lives;
    }

    // If the user tries to change the lives val and it is below 0
    // or above the MAXLIVES then the health is set to MAXLIVES. Else,
    // the user health is set to the input.
    public void setLives(int l) {
        if (l >= 0 && l <= MAXLIVES){
            lives = l;
        }

        else{
            lives = MAXLIVES;
        }
    }

    public String[] getInventory() {
        return inventory;
    }

    public void setInventory(String[] val) {
        inventory = val;
    }

    // Returns true if the player has positive health;
    // false, otherwise.
    public boolean isAlive() {
        if (lives > 0) {
            return true;
        }
        else{
            return false;
        }
    }

    // If the user has a "knife" or "gun" in their inventory,
    // then true is returned; else, false is returned.
    public boolean hasWeapon() {
        for (String s : inventory)
            if (s != null && (s.equals("knife") || s.equals("gun"))){
                return true;
            }
        
        return false;
    }

    // Counts the non-null elements in the user's inventory
    // and returns that value.
    public int sizeOfInventory() {
        int count = 0;
        for (String s : inventory){
            if (s != null){
                count++;
            }
        }
        return count;
    }

    // Heals the player back to MAXLIVES
    public void heal() {
        lives = MAXLIVES;
    }
    
    // lowers the player's health by 1
    public void damage() {
        if (isAlive()){
            lives--;
        }
    }

        // If empty space in inventory, then the player
        // will pick up the item.
    public void pickUp(String item) {
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] == null){
                inventory[i] = item;
                break;
            }
        }
    }

    // If item in inventory is equal to user argument,
    // then the slot becomes empty, essentially "dropping" it.
    public void drop(String item) {
        for (int i = 0; i < inventory.length; i++) {
            if (inventory[i] != null && inventory[i].equals(item)) {
                inventory[i] = null;
                break;
            }
        }
    }

    // Prints the current state of the player: Name, health, and inventory.
    public String toString() {
        String inventoryString = "";
        for (String item : inventory){
            if (item != null){
                inventoryString += item + ", ";
            }
        }
        return "Name:\t" + name + "\nLives:\t" + lives + "\nInventory:\t" + inventoryString + "\n";
    }

    }