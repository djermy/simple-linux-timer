# simple_linux_timer

## Setup
This timer was made and tested with the `speech dispatcher` linux package, ensure you have it installed.

*arch linux*
```
sudo pacman -S speech-dispatcher
```
*ubuntu*
```
sudo apt install speech-dispatcher
```
This was only tested with the `festival` package for `speech-dispatcher`. once both are installed, run
```
spd-conf
```
to set up `speech dispatcher`, then run the festival server
```
festival --server
```

## How To Use
clone this repository, add main.py to `$PATH` and alias it as timer or similar. call function with,
minutes you'd like to set it for. example:
```
timer 5
```