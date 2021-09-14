/* Simple Java Chatbot Program
   First code i've ever wrote in Java
   For Middlesbrough College TLevel Course
*/
import java.util.Scanner;

public class Robot {
	
	public static void main(String args[])
	{
		Scanner getInput = new Scanner(System.in);
		System.out.println("You: ");
		
		String userInput = getInput.nextLine();
		
		String BotResponse = getResponseFromInput(userInput);
		System.out.println(BotResponse);
		
	}
	
	public static String getResponseFromInput(String input) 
	{
		System.out.println(input);
		if (checkExists(input,"hi")) {
			return "Hello!";
		} else if (checkExists(input,"bye")) {
			return "Good Bye!";
		} else 
		{
			return "I don't know";
		}
		
	}
	
	public static boolean checkExists(String input, String item) 
	{
		return input.indexOf(item) >= 0;
	}
}