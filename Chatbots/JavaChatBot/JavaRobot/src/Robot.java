// Author: James Wallace
/* Simple Java ChatBot Program
   First code i've ever wrote in Java
   For Middlesbrough College TLevel Course
*/
import java.util.Scanner;
import utils.*;
import responder.*;

/*
  Robot Class
  Main Class that runs everything
 */
public class Robot {
	final static String botName = "Elle";
	// final static String password = "test";
	
	static boolean botRunning = true;
	static Scanner getInput = new Scanner(System.in);
	//static boolean userLogIn = false;
	
	public static void main(String args[])
	{
		System.out.println(utils.getDate());
		System.out.println(botName);
		
		while (botRunning) {
			System.out.print(">>> ");
			
			String userInput = "";
			
			if (getInput.hasNext()) 
			{
				userInput = getInput.nextLine();
				
				if (utils.match(userInput, "quit")) 
				{
					System.out.println(userInput);
					break;
				}
				
				String BotResponse = responder.getResponseFromInput(userInput);
				System.out.println(botName+": "+BotResponse);
				
				/* CODE FOR COMMAND SYSTEM - MASSIVE WIP NOT WORKING AT ALL RIGHT NOW
				String[] commandPrefixes = {"command","cmd","run"};
				String[] quitPrefixes = {"quit","close","shut down"};
				String[] loginPrefixes = {"log in","log on","login"};
				
				if (utils.matchTable(userInput,commandPrefixes)) {
					if (userLogIn) 
					{
						
					}
				}
				
				if (utils.matchTable(userInput, loginPrefixes)) 
				{
					System.out.println("hi");
					if (userLogIn)
					{
						System.out.println(botName+": You are already logged in!");
					}
					else 
					{
						System.out.println("Enter Password");
						System.out.println(">>> ");
						userInput = getInput.nextLine();
						
						if (userInput == password) 
						{
							userLogIn = true;
							System.out.println("Logged In!");
						}
						else
						{
							System.out.println("Incorrect");
						}
					}
				}
				
				if (utils.matchTable(userInput, quitPrefixes)) 
				{
					break;
				}
				
				else 
				{
					String BotResponse = responder.getResponseFromInput(userInput);
					System.out.println(BotResponse);
				}*/
			}
		}
		
		getInput.close();
		System.out.println(botName+" has been shut down!");
	}
} 