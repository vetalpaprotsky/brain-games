# Brain Games

[![Maintainability](https://api.codeclimate.com/v1/badges/49a4a81a5cd353407533/maintainability)](https://codeclimate.com/github/vetalpaprotsky/brain-games/maintainability)
![Python CI](https://github.com/vetalpaprotsky/brain-games/workflows/Python%20CI/badge.svg)

## Installation
Brain Games can be installed using pip. The package is published on [TestPyPI](https://test.pypi.org/) repository(not [PyPI](https://pypi.org/), as usually) so, you need to pass additional parameters to `pip install` command to make pip search for the package on [TestPyPI](https://test.pypi.org/) instead of [PyPI](https://pypi.org/). Note that the name of the package is actually vetalpaprotsky-brain-games. Here's the installation command:

```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ vetalpaprotsky-brain-games
```

To verify that the installation was successful, run `brain-games` command in the terminal. If you're not getting any errors, then everything went well.

Here's how the installation process looks like:
[![asciicast](https://asciinema.org/a/O6ESbaJR1hTTSIIFJG3jF190Q.svg)](https://asciinema.org/a/O6ESbaJR1hTTSIIFJG3jF190Q)

## Available games
There're five different games you can play. Each game has a short description and a terminal recording which demonstrates the gameplay:
- [Calculator](#calculator)
- [Even](#even)
- [GCD](#gcd)
- [Prime](#prime)
- [Progression](#progression)

<a name="calculator"></a>
### Calculator
Calculate a simple arithmetic expression.
[![asciicast](https://asciinema.org/a/qyvyfYPyj9hwHctQGvLUTMLv4.svg)](https://asciinema.org/a/qyvyfYPyj9hwHctQGvLUTMLv4)

<a name="even"></a>
### Even
Determine whether a number is even or odd.
[![asciicast](https://asciinema.org/a/JS2uW7hURfIP2oNQqu5cZBsb7.svg)](https://asciinema.org/a/JS2uW7hURfIP2oNQqu5cZBsb7)

<a name="gcd"></a>
### GCD
Try to find the greatest common denominator of two numbers.
[![asciicast](https://asciinema.org/a/7U9GR0XTC1hqwK9DIy0SRmYg9.svg)](https://asciinema.org/a/7U9GR0XTC1hqwK9DIy0SRmYg9)

<a name="prime"></a>
### Prime
Figure out whether a number is prime or compound.
[![asciicast](https://asciinema.org/a/t6ZrO99xKpvBRrsZ4htHBfWet.svg)](https://asciinema.org/a/t6ZrO99xKpvBRrsZ4htHBfWet)

<a name="progression"></a>
### Progression
Fill a gap in an arithmetic progression.
[![asciicast](https://asciinema.org/a/Hamj30tuqbHJDdNpBEGBVa4W5.svg)](https://asciinema.org/a/Hamj30tuqbHJDdNpBEGBVa4W5)
