
# NethyTech

[![Downloads][downloads-shield]][downloads-url]
<img src="https://komarev.com/ghpvc/?username=anubhavchaturvedi-github&label=Profile%20views&color=0e75b6&style=flat" alt="anubhavchaturvedi-github" width="150" height="28" />
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagram][instagram-shield]][instagram-url]
[![Twitter][twitter-shield]][twitter-url]
[![YouTube][youtube-shield]][youtube-url]

**NethyTech** is a next-gen Python package crafted by Anubhav Chaturvedi for futuristic automation. Imagine a powerful AI at your fingertips—scanning webpages in real-time, delivering precise weather insights, managing files instantly, and executing complex calculations—all in a fraction of a second. Step into the future of Python automation with NethyTech.

---

## Core Capabilities

- **Real-Time Web Monitoring**: Track and log any changes in targeted text on live web interfaces, all updated seamlessly into `input_cmd.txt`.
- **Advanced Weather Insights**: Retrieve accurate, up-to-the-minute weather data for any specified location.
- **File Management**: Effortlessly read and write files with single-line commands, optimizing data flow.
- **Instant Calculations**: Handle arithmetic with precision and speed.
- **Animated Text Display**: Add animated text effects for a dynamic user experience.
- **Stealth Operations**: Operates headlessly for non-disruptive, background automation.

---

## Installation

Easily install NethyTech through pip:

```bash
pip install nethytech
```

### Requirements

- Python 3.12 or above
- Selenium and WebDriver Manager
- Chrome browser (necessary for WebDriver operations)

---

## Usage Guide

### 1. **Web Text Monitoring**  
Track changes in a text field on any webpage:

```python
from nethytech import SpeechToText
SpeechToText()
```

- **Steps**:  
   - Launch [this webpage](https://aquamarine-llama-e17401.netlify.app/) and modify the text.
   - NethyTech will detect and log any updates to `input_cmd.txt` in real time.

### 2. **Weather Reporting**  
Effortlessly access weather data:

```python
from nethytech import weather
print(weather("Karnataka"))
```

**Output Sample**:
```
Weather report: karnataka

     \  /       Partly cloudy
   _ /"".-.     +29(30) °C     
     \_(   ).   ↘ 5 km/h       
     /(___(__)  10 km
                0.0 mm
                                                       ┌─────────────┐               

┌──────────────────────────────┬───────────────────────┤  Sun 27 Oct ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│     \   /     Sunny          │  _`/"".-.     Patchy rain ne…│    \  /       Partly Cloudy  │     \   /     Clear          │
│      .-.      +25(26) °C     │   ,\_(   ).   +28(29) °C     │  _ /"".-.     +25(26) °C     │      .-.      +23(25) °C     │
│   ― (   ) ―   → 7-8 km/h     │    /(___(__)  ↓ 5-6 km/h     │    \_(   ).   ↘ 9-18 km/h    │   ― (   ) ―   → 9-18 km/h    │
│      `-’      10 km          │      ‘ ‘ ‘ ‘  10 km          │    /(___(__)  10 km          │      `-’      10 km          │
│     /   \     0.0 mm | 0%    │     ‘ ‘ ‘ ‘   0.0 mm | 82%   │               0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                       ┌─────────────┐               

┌──────────────────────────────┬───────────────────────┤  Mon 28 Oct ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│     \   /     Sunny          │    \  /       Partly Cloudy  │     \   /     Clear          │     \   /     Clear          │
│      .-.      +25(26) °C     │  _ /"".-.     +28(29) °C     │      .-.      +24(25) °C     │      .-.      21 °C          │
│   ― (   ) ―   → 10-11 km/h   │    \_(   ).   → 12-14 km/h   │   ― (   ) ―   → 10-22 km/h   │   ― (   ) ―   ↗ 12-25 km/h   │
│      `-’      10 km          │    /(___(__)  10 km          │      `-’      10 km          │      `-’      10 km          │
│     /   \     0.0 mm | 0%    │               0.0 mm | 0%    │     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
                                                       ┌─────────────┐               

┌──────────────────────────────┬───────────────────────┤  Tue 29 Oct ├───────────────────────┬──────────────────────────────┐
│            Morning           │             Noon      └──────┬──────┘     Evening           │             Night            │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│     \   /     Sunny          │     \   /     Sunny          │    \  /       Partly Cloudy  │     \   /     Clear          │
│      .-.      +25(26) °C     │      .-.      +28(30) °C     │  _ /"".-.     +25(26) °C     │      .-.      +23(25) °C     │
│   ― (   ) ―   → 10-12 km/h   │   ― (   ) ―   → 10-12 km/h   │    \_(   ).   ↗ 10-20 km/h   │   ― (   ) ―   ↗ 10-17 km/h   │
│      `-’      10 km          │      `-’      10 km          │    /(___(__)  10 km          │      `-’      10 km          │
│     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │               0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
Location: Karnataka, India [14.5203896,75.7223521]
```


### 3. **Animated Text Output**

Create an engaging user interface with animated text:

```python
from nethytech import printA
printA("Hello from the future!")
```

### 4. **Instant Calculations**  
Execute calculations swiftly:

```python
from nethytech import calculate
print(calculate("2+5+5*7+45/2"))
```

   - **Output**: `64.5`

### 5. **File Management in One Line**

**Read File**:
```python
from nethytech import readfile
print(readfile("file.txt"))
```

**Write to File**:
```python
from nethytech import writefile
writefile("file.txt", "Data saved successfully.")
```

---

## Social Stats and Links

[downloads-shield]: https://img.shields.io/badge/Downloads-1K+-brightgreen?style=for-the-badge
[downloads-url]: https://pypi.org/project/nethytech/

[profile-views-shield]: https://komarev.com/ghpvc/?username=anubhav-chaturvedi&color=blue&style=for-the-badge
[profile-views-url]: https://github.com/AnubhavChaturvedi-GitHub

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=0B5FBB
[linkedin-url]: https://www.linkedin.com/in/anubhav-chaturvedi-/

[instagram-shield]: https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white
[instagram-url]: https://www.instagram.com/_anubhav__chaturvedi_/

[twitter-shield]: https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white
[twitter-url]: https://x.com/AnubhavChatu

[youtube-shield]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[youtube-url]: https://www.youtube.com/@NetHyTech

---

## Author

**Anubhav Chaturvedi**  
Email: [chaturvedianubhav520@gmail.com](mailto:chaturvedianubhav520@gmail.com)  
Explore more at [GitHub](https://github.com/AnubhavChaturvedi-GitHub)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information. 

---

**NethyTech: Where Automation Meets the Future**
