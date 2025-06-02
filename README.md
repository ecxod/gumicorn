<a href="https://salsa.debian.org/ecxod/gumicorn/" target="_new">
<img src="https://salsa.debian.org/ecxod/gumicorn/-/badges/release.svg">
</a>
<a href="https://salsa.debian.org/ecxod/gumicorn/" target="_new">
<img src="https://salsa.debian.org/ecxod/gumicorn/badges/master/pipeline.svg">
</a>


# Welcome to gumicorn

WSGI HTTP Server for UNIX

This project is a gunicorn fork for systemd free distributions like devuan 

```sh
pip install gumicorn
```

if you want make the packege yourself

```sh
git clone https://github.com/ecxod/gumicorn

cd gumicorn
python -m build

```
you find the package in dist/

```
<repository_root>/
├── gumicorn/
│   ├── dist/
│   │   ├── gumicorn-23.0.4-py3-none-any.whl
│   │   ├── gumicorn-23.0.4.tar.gz
│   ├── gumicorn_23.0.4_all/
│   │   ├── DEBIAN/
│   │   │   ├── control
│   │   ├── usr/
│   │   │   ├── bin/
│   │   │   │   ├── gumicorn
│   │   │   ├── lib/
│   │   │   │   ├── python3/
│   │   │   │   │   ├── dist-packages/
│   │   │   │   │   │   ├── gumicorn/
│   │   │   │   │   │   ├── ...
│   ├── gumicorn_23.0.4_all.deb
├── .gitlab-ci.yml

```
