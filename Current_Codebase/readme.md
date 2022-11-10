Requirements:

- Python installed on your computer
    - React native emulation software (varies)
    - Use this guide to determine what is needed for your OS https://reactnative.dev/docs/0.65/environment-setup

- Google Maps API Key
  - To access the Google Maps API, you need to create a new API key. The one included in the app is disabled.
    - Guide to create API key: https://developers.google.com/maps/documentation/javascript/get-api-key

- Android Studio (for emulation)
  - Set up a device within Android Studio’s device manager
  - The following Android Studio version is running and emulates successfully as of 5/27/2022
    - Android Studio Bumblebee | 2021.1.1 Patch 2
    - Build #AI-211.7628.21.2111.8193401, built on February 16, 2022
    - Runtime version: 11.0.11+9-b60-7590822 amd64
    - VM: OpenJDK 64-Bit Server VM by Oracle Corporation
    - Windows 10 10.0
    - GC: G1 Young Generation, G1 Old Generation
    - Memory: 1280M
    - Cores: 16
    - Registry: external.system.auto.import.disabled=true
    - Non-Bundled Plugins: org.jetbrains.kotlin (211-1.6.10-release-923-AS7442.40)

  - The following device configuration is working as of 5/27/2022
Google Pixel 4 API level 31 (Google Pixel 4 API level 30 for M1 Macs)
    - Android 12.0 Google Play | x86_64
    - Ram size: 1536MB
    - VM heap: 256MB
    - Internal storage space: 6.1GB

- Node
Node.js v16.13.2 works as of 5/27/2022
Instructions for emulation (Windows 10, Android)
Step 1:
  - Start Android Studio
  - Open Android Studio’s “Device Manager” (located on the right side of the window)
  - Create a device following the requirements above
  - Press the green play button to begin booting your chosen device
  - Once the phone has fully booted and is idle at the home screen

Step 2:
  - Open two terminals of your choice
  - On one, type (without quotes)
    - “npx react-native start”
    - OR (to clear cache)
    - “npm start --reset-cache” (recommended)
  - Once the Metro logo is displayed on the first terminal, enter this in the second:
    - npm run android
    - OR
    - npx react-native run-android
Wait for the program to boot