# swirl

Help message:
```
➜ py .\swirl.py --help
Usage: swirl.py [OPTIONS] COMMAND [ARGS]...

  CLI entry point. Will plot a single default spirograph if left blank without
  a subcommand.

  Args:     ctx (click.core.Context): Context passed by click to determine if
  subcommand is empty.

Options:
  --help  Show this message and exit.

Commands:
  multi   A helper function to plot multiple graphs by incrementing the...
  single  Function to plot and display a defaul spirograph.
```

Creating and displaying a `single` image with defaults:
```
➜ py .\swirl.py
```
or
```
➜ py .\swirl.py single
```

Creating and displaying a `single` image with changed `inner` and `outer` radius sizes:
```
➜ py .\swirl.py --inner=0.7 --outer=0.9
```

Creating and displaying a `multi` image with defaults:
```
➜ py .\swirl.py multi
```

Creating and displaying a `multi` image with changed `inner` and `outer` radius sizes:
```
➜ py .\swirl.py --inner=0.1 --outer=2.5
```

Default `single` image:

![image](https://github.com/brad90four/swirl/blob/main/img/single.png)

Default `multi` image:

![image](https://github.com/brad90four/swirl/blob/main/img/multi.png)

## Installation and Setup

This project uses [poetry](https://python-poetry.org/) for the dependency management. Once you have poetry installed, initialize your virtual environment for the project with `poetry shell`

Install the dependencies with `poetry install`

#
If you wish to contribute to the repo, install the pre-commit hooks with `poetry run pre-commit install`
