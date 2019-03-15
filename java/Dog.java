public class Dog{
	String name;
	int age;
	String type;
	String color;
	public Dog(String name){
		this.name = name;
	}
	public void age(int age){
		this.age = age;
	}
	public void type(String type){
		this.type = type;
	}
	public void color(String color){
		this.color = color;
	}
	public void baking(){
		System.out.println("wangwangwang!");
	}
	public void printDog(){
		System.out.println("name:"+name);
		System.out.println("age:"+age);
		System.out.println("type:"+type);
		System.out.println("color:"+color);
	}
}
