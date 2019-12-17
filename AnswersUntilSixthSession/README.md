# Some discovery around jupyter

## Install Theme
### 1. Istall the theme
```bash
$ pip install jupytertheme
```
### 2. Change the theme
to see the list of available themes:
```bash
$ jt -l
Available Themes:
   chesterish
   grade3
   gruvboxd
   gruvboxl
   monokai
   oceans16
   onedork
   solarizedd
   solarizedl
```
to change the theme:
```bash
$ jt -t monokai
```
## Install some extensions
> See [doc](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/install.html) for this section

### 1. Install the python package
```bash
$ pip install jupyter_contrib_nbextensions
```
*or...*
```bash
$ pip3 install jupyter_contrib_nbextensions --user
```

### 2. Install javascript and css files
```bash
$ jupyter contrib nbextension install --user
```

### 3. Enabling/Disabling extensions
```bash
$ jupyter nbextension enable codefolding/main
```
