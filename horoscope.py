# Dictionary of horoscopes
horoscopes = {
  "aries": "Today is a good day to take a risk and try something new.",
  "taurus": "Expect good things to come your way. Don't be afraid to reach out and grab them.",
  "gemini": "Communication is key. Make sure to listen carefully to what others have to say.",
  "cancer": "You may be feeling a little bit emotional today. Take some time to relax and recharge.",
  "leo": "You are feeling confident and ready to take on the world. Embrace your inner lion.",
  "virgo": "Pay attention to the details. They can make a big difference in your success today.",
  "libra": "Be fair and just in all your interactions. Remember to treat others as you would like to be treated.",
  "scorpio": "Don't be afraid to let your passion and intensity shine. You are unstoppable when you set your mind to something.",
  "sagittarius": "Be open to new experiences and ideas. You never know what you might learn or discover.",
  "capricorn": "Focus on your goals and work hard to achieve them. Success is within your reach.",
  "aquarius": "Be yourself and don't be afraid to be unique. You are a one-of-a-kind individual.",
  "pisces": "Trust your intuition and listen to your inner voice. It will guide you in the right direction."
}

# Get the user's star sign
sign = input("Enter your star sign: ").lower()

# Check if the sign is in the dictionary
if sign in horoscopes:
  # Print the horoscope for the user's sign
  print(horoscopes[sign])
else:
  # Print an error message if the sign is not in the dictionary
  print("Invalid star sign. Please try again.")
