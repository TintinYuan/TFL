# Introduction to the picCat
This is a simple `Python` script for figure concatenation.

## Supported  format
- .png
- .jpeg
- .jpg

## Functionality
- Three types of horizontal alignment: `l`, `c`, `r` -> **left**, **centre**, **right** (`r` by default)
- Two background paddings: `b`, `w` -> **black**, **white** (`w` by default)
- Adjustable image directory: (`./` by default )
## Usage
Open terminal app under the current working directory of `picCat.py`, and run program using the following command
```bash
./picCat.py <alignment> <padding> <directory> 
```
Arguments are optional, default options will be used without specifications. Replace the arguments in `<>` by corresponding adjustments directly. The relative positions of arguments cannot be changed. (i.e. cannot specifying padding without specifying the alignment) 
