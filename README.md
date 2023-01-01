![GitHub license](https://img.shields.io/github/license/torresflo/Pokedex-AI.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![GitHub contributors](https://img.shields.io/github/contributors/torresflo/Pokedex-AI.svg)
![GitHub issues](https://img.shields.io/github/issues/torresflo/Pokedex-AI.svg)

<p align="center">
  <h1 align="center">Pokédex AI</h3>

  <p align="center">
    A little Pokédex application that can find a Pokémon in any image with the power of machine learning.
    <br />
    <a href="https://github.com/torresflo/Pokedex-AI/issues">Report a bug or request a feature</a>
  </p>
</p>

## Table of Contents

* [Introduction](#introduction)
* [Getting Started](#getting-started)
  * [Prerequisites and dependencies](#prerequisites-and-dependencies)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Introduction

This repository is a little Pokédex application (first generation of Pokémon only) that can find any Pokémon in a given image.\
It uses the Pokémon Classifier generated from <a href="https://github.com/torresflo/Poke-Model">Poké Model</a>.

## Getting Started

### Prerequisites and dependencies

This repository is tested on Python 3.7+ and PyTorch 1.13.1 with Cuda 11.6.

You should install Pokédex AI in a [virtual environment](https://docs.python.org/3/library/venv.html). If you're unfamiliar with Python virtual environments, check out the [user guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
First, create a virtual environment with the version of Python you're going to use and activate it.

You can install directly all required packages by using the file `requirements.txt` and doing:
```bash
pip install -r requirements.txt
```

If you want a more step by step approach, here are the main required packages:
- *PySide6* for the user interface.
- *torch* to manipulate the model.
- *transformers* for the model.
- *pillow* to load and manipulate images.
- *progress* to feedback progression with beautiful progress bars (only used to reconstruct the database).

All packages can be installed separetly with the regular:

```bash
pip install <package-name>
```

### Installation

Follow the instructions above then clone the repo (`git clone https:://github.com/torresflo/Pokedex-AI.git`).\
You can now launch the app by running `main.py`.

## Usage

When the app is running, you can select an image by clicking on the button `Select image...` and then ask to search for the Pokémon by clicking on `Search Pokémon`. Depending on your machine, this can take some time but it should be faster after the first search.

You can also navigate between the different Pokémon by clicking on the buttons at the bottom of the application (`<<`, `<`, `>`, and `>>`).

All data required for the application is stored in the `data` folder. The data has been scraped from <a href="https://pokeapi.co/">PokeAPI</a>. You can force the application to retrieve all the data by just deleting the file `data\pokemon_data.json`. By default, data will just be loaded from that file if it exists.

### Screenshot ###

![Example image](https://raw.githubusercontent.com/torresflo/Pokedex-AI/main/examples/example1.png)

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE` for more information.
