# NethyTech

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagram][instagram-shield]][instagram-url]
[![Twitter][twitter-shield]][twitter-url]
[![YouTube][youtube-shield]][youtube-url]

<!-- Links to Social Media -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0B5FBB
[linkedin-url]: https://www.linkedin.com/in/anubhav-chaturvedi-/

[instagram-shield]: https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white
[instagram-url]: https://www.instagram.com/_anubhav__chaturvedi_/

[twitter-shield]: https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white
[twitter-url]: https://x.com/AnubhavChatu

[youtube-shield]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[youtube-url]: https://www.youtube.com/@NetHyTech



## Overview

NethyTech is a Python package that utilizes Selenium to monitor a text box on a specified webpage. Whenever the text in the text box changes, the package captures the new value and writes it to a file named `input_cmd.txt`. This functionality can be useful for applications such as automated testing, web scraping, or real-time data monitoring.

## Features

- Monitors changes in a text box on a live webpage.
- Saves the updated text to a local file.
- Runs headless (without opening a browser window) for background operations.

## Requirements

- Python 3.12
- Selenium
- WebDriver Manager

## Installation

To install this package, ensure you have Python 3.x installed. You can install NethyTech using pip:

```bash
pip install nethytech
```

This command will install the package along with its dependencies.

## Usage

To use the `SpeectToText` function from the package, you can import it in your Python script:

```python
from nethytech import SpeechToText
```

Then, you can call the `SpeechToText()` function to start the monitoring process:

```python
SpeechToText()
```

The script will continuously check for changes in the text box on the specified webpage. When a change is detected, the new text will be saved to `input_cmd.txt` in the current working directory.

### 1 Speech To Text

1. Install the package using `pip install nethytech`.
2. Create a Python script and import the `SpeechToText()` function:

    ```python
    from nethytech.STT import 

    SpeechToText()()
    ```

3. Run your script.
4. Open the webpage (https://aquamarine-llama-e17401.netlify.app/) and change the text in the input box.
5. The changes will be captured and written to `input_cmd.txt`.

## result :
`input_cmd.txt`
```
i am listening..
```
`terminal`
```
i am listning...
```

# 2 Check Weather in any area

Use case
```python
from nethytech import weather
weather("karnataka")
```

## result : 
```
Weather report: Karnataka

      \   /     Sunny
       .-.      +28(29) °C
    ― (   ) ―   ↘ 8 km/h
       `-’      10 km
      /   \     0.0 mm
                                                       ┌─────────────┐

┌──────────────────────────────┬───────────────────────┤  Sat 26 Oct ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│     \   /     Sunny          │     \   /     Sunny          │     \   /     Clear          │     \   /     Clear          │
│      .-.      +25(27) °C     │      .-.      +28(29) °C     │      .-.      +23(25) °C     │      .-.      22 °C          │
│   ― (   ) ―   ↘ 10-12 km/h   │   ― (   ) ―   ↘ 13-15 km/h   │   ― (   ) ―   ↘ 4-8 km/h     │   ― (   ) ―   ↗ 5-11 km/h    │
│      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │      `-’      10 km          │
│     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                       ┌─────────────┐

┌──────────────────────────────┬───────────────────────┤  Sun 27 Oct ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│     \   /     Sunny          │     \   /     Sunny          │    \  /       Partly Cloudy  │    \  /       Partly Cloudy  │
│      .-.      +24(26) °C     │      .-.      +28(29) °C     │  _ /"".-.     +25(27) °C     │  _ /"".-.     +23(24) °C     │
│   ― (   ) ―   → 9-11 km/h    │   ― (   ) ―   → 11-13 km/h   │    \_(   ).   ↗ 10-21 km/h   │    \_(   ).   ↗ 11-23 km/h   │
│      `-’      10 km          │      `-’      10 km          │    /(___(__)  10 km          │    /(___(__)  10 km          │
│     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                       ┌─────────────┐

┌──────────────────────────────┬───────────────────────┤  Mon 28 Oct ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│     \   /     Sunny          │     \   /     Sunny          │    \  /       Partly Cloudy  │     \   /     Clear          │
│      .-.      +24(26) °C     │      .-.      +28(30) °C     │  _ /"".-.     +26(27) °C     │      .-.      +24(25) °C     │
│   ― (   ) ―   → 10-11 km/h   │   ― (   ) ―   ↘ 10-12 km/h   │    \_(   ).   ↘ 6-12 km/h    │   ― (   ) ―   → 6-13 km/h    │
│      `-’      10 km          │      `-’      10 km          │    /(___(__)  10 km          │      `-’      10 km          │
│     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │               0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
Location: Karnataka, India [14.5203896,75.7223521]
```

## 3 print with animation
Use case
```python
from NetHyTech import printA
printA("hello i am anubhav")
```
## result:
--- Animated text ---

## 4 calculate any thing
Use case
```python
from NetHyTech import calculate
print(calculate("2+5+5*7+45/2"))
```
# result:
```
64.5
```
## Notes

- Make sure to have Chrome installed, as this script uses Chrome WebDriver.
- If you encounter any issues, ensure that you have the correct versions of Python and the required packages.

## Author

Anubhav Chaturvedi  
chaturvedianubhav520@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
