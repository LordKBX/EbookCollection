# eBookCollection
This application is designed for managing eBooks

## formats support
|**type**|**library**|**intern reader**|**editor**|
|:---|:---:|:---:|:---:|
|***epub 1/2/3***|X|X|X|
|***cbz***|X|X|.|
|***cbr***|X|X||
|***pdf***|X|||
|***mobi***|X|||
|***txt***|X|||
|***rtf***|X|||
|***doc***|X|||
|***docx***|X|||

## Features
- eBook import in database
- eBook reader, if file not supported open file with default application
- eBook editor
- edit eBook metadata(support for title, series and authors)
- modify eBook storage directory if metadata updated
- Settings window
    - Global
        - change language
        - import language
        - change style
        - import style
        - modify library folder
    - Metadata
        - change default eBook cover style
        - change file name eBook import template
    - About tab

## Planed Features
- Library sub window metadata edition
- File conversion
- Settings window
    - Conversion
        - default module CBZ to EPUB
        - import Conversion module
        - modify parameters of Conversion modules

- Synchronize eBook library with mobile terminal (in a far future)
    - incompatible terminal software would only have the eBook file copied
    - compatible terminal software would have
        - full metadata information's
        - bookmark
        - cover
        - tags


## Prerequisites

Require Python >= 3.5.x
Require the following complements:
- PyQt5
- PyQtWebKit
- Qsci
- pysqlite3
- lxml
- numpy
- six
- Beautifulsoup4
- pywin32(on windows)

Required Archiver:
- Windows => 7Zip

## Additional Packages
- [lang](https://github.com/LordKBX/eBookCollection/tree/main/packages/lang)
- [style](https://github.com/LordKBX/eBookCollection/tree/main/packages/style)
- [plugin](https://github.com/LordKBX/eBookCollection/tree/main/packages/plugin)

## Additional Packages examples
- [lang](https://github.com/LordKBX/eBookCollection/raw/main/test/example%20lang%20package.ebclang)
- [style](https://github.com/LordKBX/eBookCollection/raw/main/test/example%20style%20package.ebcstyle)
##### /!\ the packages are only example packages, their content is incomplete(for style) or invalid(text in lang package still in english)

## Installation
### Windows installer: 
Go to the Release page [Here](https://github.com/LordKBX/EbookCollection/releases), contains:
- executable with scripts compiled (compiled version) 
- executable not compiled and without dependencies (light version)

### Manualy
#### On Windows and Mac
1. Install Python >=3.5.x which you can find [here](https://www.python.org/downloads/ "Python Download Link"). Do not forget the PATH inclusion(checked by default)
2. Run
```
pip install -r [path of the application files]requirements.txt
```
#### On Linux(Ubuntu)
1. Run 
```
sudo apt-get install python3
```
2. Run
```
sudo pip3 install -r [path of the application files]requirements.txt
```

## Usage
Use the start.bat file. 
```
[path of the application files]start.bat
```
Or Run
```
python [path of the application files]main.py
```
##### If Python dir not in the PATH variable then remplace "python" by "[path of the python dir]python.exe"


#### On Linux and MacOs
```
python3 main.py
```
or use the script start.sh

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

Third party references => [here](./README-third_party.md)