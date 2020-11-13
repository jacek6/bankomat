# bankomat
Prosty projekt z przykladem bankomatu

# Setup
For installaion you may install dependencies by pip:

```bash
pip install -r requirements.txt
```

or by creating conda env (required conda installed):
```bash
conda env create -f environment.yml

# activate the conda environment
conda activate bankomat_env

```

# Cryptinng code

To encrypt your source code run:
```
pyarmor obfuscate bankomat/bankomat_model.py
```
In case you don't have `pyarmor` installed just run `pip install pyarmor`.

In folder `dist` you have crypted code:
```
├── dist
│   ├── bakomat_event.py
│   ├── bankomat_model.py
│   ├── __init__.py
│   ├── main_window.py
│   └── pytransform
│       ├── __init__.py
│       └── _pytransform.so

```

You may copy your original `bankomat_model.py` to some safe location and paste
crypted version of `bankomat_model.py`. Please remeber to copy also `pytransform` folder.
At the end everything should look like this:
```
├── bankomat
│   ├── bakomat_event.py
│   ├── bankomat_model.py
│   ├── __init__.py
│   ├── main_window.py
│   └── pytransform
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-38.pyc
│       └── _pytransform.so
```