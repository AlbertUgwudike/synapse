# Scripts to automate batch image processing using CellProfiler on MacOS

## Requirements
- CellProfiler 4.2.6 (Please ensure its located in Applications!).
- Python3 (Usually installed by default in MacOS).
- A batch of images.
- A CellProfiler Pipeline `.cppipe` file.
- (Please ensure the ExportToSpreadSheet module adds the image file and folder names!).

## Usage 
- Open terminal.
- Clone this repository `$ git clone https://github.com/AlbertUgwudike/synapse.git`
- Navigate into the project by running the command: `$ cd synapse`
- Use finder to copy all your images and one `.cppipe` file into the `data/` folder
- Back in the same terminal, run the command: `$ ./synapse.zsh`
- All done!
