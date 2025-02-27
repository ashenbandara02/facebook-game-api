# Facebook Game API

This repository contains the necessary components to integrate Facebook's gaming services into your game. With Facebook's extensive social features, you can enhance user engagement and expand your game's reach.

## Features

- **Facebook Login for Gaming**: Simplifies user authentication by allowing players to log in using their Facebook credentials.
- **Sharing for Gaming**: Enable players to share their in-game achievements and content directly to their Facebook feed or via Messenger.
- **Player Finder**: Help players discover and connect with their friends who are also playing your game.
- **Leaderboards**: Implement competitive leaderboards to motivate players and encourage friendly competition.
- **In-App Purchases (IAP)**: Integrate Facebook's payment system to offer in-game purchases.
- **In-App Ads (IAA)**: Utilize Facebook's Audience Network to display ads within your game.

## Getting Started

### Prerequisites

1. Create a new app on the [Facebook Developers portal](https://developers.facebook.com/) to obtain your App ID.
2. Integrate the Facebook SDK into your game. Depending on the platform you're developing for, you'll need to use the appropriate SDK:
   - [JavaScript SDK](https://developers.facebook.com/docs/games/build/gaming-services/sdk-js/)
   - [Unity SDK](https://developers.facebook.com/docs/games/build/gaming-services/sdk-unity/)
   - [iOS SDK](https://developers.facebook.com/docs/games/build/gaming-services/sdk-ios/)
   - [Android SDK](https://developers.facebook.com/docs/games/build/gaming-services/sdk-android/)

### Installation

To get started with the Facebook Game API in your project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ashenbandara02/facebook-game-api.git
   ```

2. **Install Dependencies**

   Install the necessary dependencies for your project using the appropriate package manager (e.g., npm, yarn, etc.).

3. **Configure the Facebook SDK**

   After installing the SDK for your platform, configure it with your Facebook App ID. Detailed instructions on configuring each SDK can be found in the links above.

4. **Integrate the Features**

   Use the provided classes and methods to integrate the following features into your game:
   - Facebook Login
   - Sharing
   - Player Finder
   - Leaderboards
   - In-App Purchases
   - In-App Ads

   Refer to the documentation for more detailed implementation guides.

5. **Test the Integration**

   Thoroughly test each feature to ensure everything works as expected.

6. **Deploy Your Game**

   Once you have completed your testing, deploy your game to the desired platform.

## Example Usage

```javascript
// Example of Facebook Login integration

FB.login(function(response) {
  if (response.authResponse) {
    console.log('Player logged in successfully');
  } else {
    console.log('Player login failed');
  }
});
```

## Additional Resources

- [Facebook Games Documentation](https://developers.facebook.com/docs/games/)
- [Gaming Services Quick Start Guide](https://developers.facebook.com/docs/games/build/instant-games/get-started/quick-start)
- [JavaScript SDK Reference](https://developers.facebook.com/docs/games/build/gaming-services/sdk-js/)

## Contributing

Feel free to fork the repository, open issues, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
