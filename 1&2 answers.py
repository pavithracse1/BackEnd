1 ANSWER:


import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ContactNumberValidator {

    public static boolean validateContactNumber(String number) {
        // Regular expression pattern for validating contact numbers
        String pattern = "^(\\+\\d{1,2})?[-.\\s]?\\(?\\d{1,4}\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$";

        // Remove any non-digit characters from the number
        number = number.replaceAll("\\D", "");

        // Check if the number matches the pattern
        Pattern regex = Pattern.compile(pattern);
        Matcher matcher = regex.matcher(number);

        return matcher.matches();
    }

    public static void main(String[] args) {
        // Test cases
        String[] numbers = {
                "2124567890",
                "212-456-7890",
                "(212)456-7890",
                "(212)-456-7890",
                "212.456.7890",
                "212 456 7890",
                "+12124567890",
                "+1 212.456.7890",
                "+212-456-7890",
                "1-212-456-7890"
        };

        for (String number : numbers) {
            if (validateContactNumber(number)) {
                System.out.println(number + " is a valid contact number.");
            } else {
                System.out.println(number + " is an invalid contact number.");
            }
        }
    }
}



2 ANSWER:


import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;

public class WebsiteDetailsScraper {

    public static void main(String[] args) {
        String websiteUrl = "https://ful.io";

        try {
            // Connect to the website and retrieve the HTML document
            Document document = Jsoup.connect(websiteUrl).get();

            // Extract social links
            System.out.println("Social links:");
            Elements socialLinks = document.select("a[href*=facebook.com], a[href*=linkedin.com]");
            for (Element link : socialLinks) {
                System.out.println(link.attr("abs:href"));
            }

            // Extract email
            System.out.println("Email:");
            Element emailLink = document.selectFirst("a[href^=mailto]");
            if (emailLink != null) {
                System.out.println(emailLink.attr("href").substring(7));
            }

            // Extract contact details
            System.out.println("Contact:");
            Elements contactElements = document.getElementsContainingOwnText("Contact");
            for (Element contactElement : contactElements) {
                Element contactDetails = contactElement.nextElementSibling();
                if (contactDetails != null) {
                    System.out.println(contactDetails.text());
                }
            }
        } catch (IOException e) {
            System.out.println("Error: Failed to fetch website details.");
            e.printStackTrace();
        }
    }
}

