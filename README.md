<br/>
<p align="center">
  <a href="https://github.com/jack-lowe-7/DWP-Project">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>
  <h1 align="center">StampWorks</h1>
  <h3 align="center">DWP Stamp Redesign Project</h3>

  <p align="center">
    As part of project with the Department of Work and Pensions Digital Team, I wrote a redesign for the current paper rewards system at my school.
    <br/>
    <br/>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/jack-lowe-7/DWP-Project?color=dark-green) ![License](https://img.shields.io/github/license/jack-lowe-7/DWP-Project) 

## Table Of Contents

* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## Built With

We used python for this project, and the built in SQLite3 module to handle the database - this is then served to the client via a Flask based website

## Getting Started

We went  through a few iterations of access - the web app was our final decision, however the local GUI & CLI versions are still in the repo
To get a local copy up and running follow these simple example steps.

### Prerequisites

This will run in the terminal (2. c.), however it's advised to use the GUI made with the PySimpleGUI module to see the full functionality in terms of a local app. The web app is however, the best option as the others have been deprecated.

```sh
pip install pysimplegui
or
pip3 install pysimplegui
```

The web app runs through a flask server, to run it you need flask
```sh
pip install flask
or
pip3 install flask
```

### Installation

1. Clone or download the repo

```sh
git clone https://github.com/Jack-Lowe-7/DWP-Project.git
```

2. a. For the web app, ensuring you are in the ```site``` directory, run
   ```sh
   flask run --cert=adhoc
   ```
   This will run the webapp out of ```https://[localhost]:500``` <br>b.For the GUI, ensure you have PySimpleGUI, then run the ```guiAccess.py``` script<br>c. For console, simply run the ```consoleAccess.py``` script



## License

Distributed under the MIT License. See [LICENSE](https://github.com/jack-lowe-7/DWP-Project/blob/main/LICENSE.md) for more information.

## Authors

* **Jack Lowe** - *Student* - [Jack Lowe](https://github.com/Jack-Lowe-7/) - [jacklowe.dev](https://www.jacklowe.dev)

## Acknowledgements

* [README Generator](https://github.com/ShaanCoding/ReadME-Generator)
