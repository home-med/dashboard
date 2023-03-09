#QR Code creator 

Used to create QR codes from urls.

Inputs:
  URL: Where the QR code is to go to.
  Location: The location of the store. This determins the image that will be displayed in the middle of the qr code.
  Add Logo: Whether or not you wish to add the logo to the qr code. If the image for the logo doesn't exist it will
      simply be skipped and no error will occur.


Config:
  Config file is in TOML each section has information in it necessary
  for the program to work. It also makes it easy to add additional details to the program and extend it.

  VERSION: Simple version number, this will change as more things are added or bug fixes are done.