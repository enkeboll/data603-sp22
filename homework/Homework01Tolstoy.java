package homework;

import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.MatchResult;
import java.util.regex.Pattern;
import java.util.stream.Collectors;


public class Homework01Tolstoy {
	
	private static int numberOfUniqueWords(List<MatchResult> list) {
		List<String> finalList = new ArrayList<>();
		
		for (MatchResult result : list) {
			String str = result.group();
			if (!finalList.contains(str)) {
				finalList.add(str);
			}
		}
		return finalList.size();
	}

	public static void main(String[] args) {
		try {
			URL url = new URL("https://www.gutenberg.org/files/2600/2600-0.txt");
			Scanner sc = new Scanner(url.openStream());
			Pattern p = Pattern.compile("[a-zA-Z]+");
			
			List<MatchResult> list = sc.findAll(p).collect(Collectors.toList());
			
			System.out.println(numberOfUniqueWords(list));
			
		} catch (Exception e) {
			System.out.println(e);
		}
	}

}
