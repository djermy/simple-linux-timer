# simple_linux_timer

## Setup
This timer requires `speech-dispatcher` and the defualt voice is `espeak-ng`.

*arch linux*
```
sudo pacman -S speech-dispatcher espeak-ng
```
*ubuntu*
```
sudo apt install speech-dispatcher espeak-ng
```
run `spd-conf`
Edit speech dispatcher config file in `~/.config/speech-dispatcher/speechd.conf`.

**uncomment** `# DefaultModule espeak-ng`

## How To Use
* Clone this repository.
* Navigate to the cloned repository.
* Run `python3 timer.py [MINS]`, example:
```
python3 timer 5
```
## Alternatively
* Clone this repository.
* Add timer.py to $PATH.
* Alias timer.py by adding `alias timer="timer.py"` to `.bashrc`
* Run `timer [MINS]`, example:
```
timer 5```