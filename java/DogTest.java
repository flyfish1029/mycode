import java.io.*;
public class DogTest{
	public static void main(String []args){
		Dog Dogone = new Dog("kit");
		Dog Dogtwo = new Dog("Tom");
		Dogone.type("Jiwawa");
		Dogone.color("White");
		Dogone.age(2);
		Dogone.printDog();
		Dogone.baking();
	}
}
