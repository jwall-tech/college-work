// Author: James Wallace

package utils;
import java.util.regex.*;
import java.util.Date;

public class utils {
	/*
	 Module Functions 
	 - Public functions that are used outside this package
	 */
	public static boolean checkExists(String input, String item) 
	{
		return input.indexOf(item) >= 0;
	}
	
	public static Date getDate() 
	{
		return new Date(0);
	}
	
	public static boolean match(String Text, String Item) 
	{
		return checkExists(Text,Item);
	}
	
	public static boolean matchTable(String Text, String Item[]) 
	{
		if (checkExists(Text,"login")) 
		{
			return true;
		}
		else if (checkExists(Text,"quit"))
		{
			return true;
		}
		else if (checkExists(Text,"command"))
		{
			return true;
		}
		return false;
	}
	
	/*
	  Package Functions
	  - Private functions that aren't used outside of this package
	 */
}
