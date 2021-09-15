// Author: James Wallace

package responder;
import utils.*;
import java.util.regex.*;

public class responder {
	
	static String[] greetingPrefixes = {};
	static String[] byePrefixes = {};
	
	/*
	 Module Functions 
	 - Public functions that are used outside this package
	 */
	public static String getResponseFromInput(String input) 
	{
		if (checkExistsInTable(input,greetingPrefixes)) {
			return "Hello!";
		} 
		
		else if (checkExistsInTable(input,byePrefixes)) {
			return "Good Bye!";
		} 
		
		else if (utils.match(input,"test")) 
		{
			return "WOW";
		}
		
		else 
		{
			return "I don't know";
		}
		
	}
	
	/*
	  Package Functions
	  - Private functions that aren't used outside of this package
	 */
	
	private static boolean checkExistsInTable(String input, String table[]) 
	{
		return false;
	}
}
