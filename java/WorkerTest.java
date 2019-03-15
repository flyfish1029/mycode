public class WorkerTest{
	public static void main(String []args){
		Worker workerone = new Worker("RunooB1");
		Worker workertwo = new Worker("RunooB2");

		workerone.empAge(26);
		workerone.empDesignation("高级程序员");
		workerone.empSalary(100000);
		workerone.printEmployee();
	}
}
