# webdrop-py
Web dead drop.


## Configuration

* TBD


## Execution

### Command line / debug

```shell
> export FLASK_DEBUG=1
> export FLASK_APP=webdrop/webdrop.py
> flask run --host=0.0.0.0
```

### Docker-ized (foreground / debug)

```shell
> docker build -t webdrop .
> docker run -it --rm -p 5000:5000 webdrop
```
