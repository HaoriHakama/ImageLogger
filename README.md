# ImageLogger
## What is ImageLogger
* ImageLogger is application which helps you to create an image abalysis program
* This application was built to solve some small annoyances when I use `cv2.imshow()`.
    * I can not open the window where I want to plase them.
    * When I call `cv2.imshow()` many times, too many windows are opened and I forget the order in which windows are opened.

## Requirements
* flet>=0.7.4
* PyImageSocket>=1.0.1

[`PyImageSocket`](https://github.com/HaoriHakama/PyImageSocket) is my Library to send images to `ImageLogger`