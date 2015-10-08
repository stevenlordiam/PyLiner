# PyLiner
A Python tool that helps you to see how many lines of code you have written in the current project directory or user-defined path

## Usage

```
usage: PyLiner.py [-h] [-p PATH] [-t TYPE] [-v]

A Python tool that helps you to see how many lines of code you have written in
the current project directory or user-defined path

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  specify the path to count lines, default is current
                        directory
  -t TYPE, --type TYPE  specify the file type to count lines, default is Java,
                        you can also use py, cpp to specify your file type
  -v, --version         show program's version number and exit

```

## Example 
  

```
python PyLiner.py
# Count the Java lines in current directory
```

![alt text](https://github.com/stevenlordiam/PyLiner/blob/master/usage/1.png "1")


```
python PyLiner.py -h
# Get option help
```

![alt text](https://github.com/stevenlordiam/PyLiner/blob/master/usage/2.png "2")

```
python PyLiner.py -p [PATH]
# Get count for user-defined path
```

![alt text](https://github.com/stevenlordiam/PyLiner/blob/master/usage/3.png "3")

```
python PyLiner.py -t [TYPE]
# Specity which file type you want to count, default is Java
```

![alt text](https://github.com/stevenlordiam/PyLiner/blob/master/usage/4.png "4")

## Contact

Steven Liu

[stevenlordiam@gmail.com](mailto: stevenlordiam@gmail.com)

If you have any suggestion, don't hesitate to send me an email. :)

## License
* [MIT](https://opensource.org/licenses/MIT)
