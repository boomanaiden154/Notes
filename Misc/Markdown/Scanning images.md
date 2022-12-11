# Scanning images

This command allows you to see the scanners that you have installed on your computer, and the scanners that are automatically detected by SANE:

```bash
scanimage -L
```

This command will produce an output listing the devices that SANE has access to. On my computer, it looks like this:

```bash
device `brother4:net1;dev0' is a Brother Brother MFC-L3770CDW
device `v4l:/dev/video2' is a Noname Chicony USB 5M WebCam: Chicony  virtual device
device `v4l:/dev/video0' is a Noname Chicony USB2.0 2M WebCam: Chico virtual device
```

Once you have found the scanner that you would like to use, you can use the next command to scan an image, making sure to use the full device name. For example, if I wanted to scan an image using the Brother MFC-L3770CDW that I have connected to my system, I would need to add the parameter `--device "brother4:net1;devo"` to the `scanimage` command.

```bash
scanimage --device <insert full device name here> --format=png --mode color --resolution 300 --progress --output-file page2.png
```

- Note: You might have to put the name of your scanner in quotes, especially if there is a semicolon as your terminal will most likely interpret this as another command if you do not wrap the name of the printer in quotes.

If you would like to do duplex scanning and your scanner supports duplex scanning, you can't really know what to do unless you have the data on your specific scanner. To acquire the commands that are specific to your scanner, you can use the following command:

```bash
scanimage --help -d <insert full device name here>
```

After you have seen this, you are looking for an option under a name like `mode` or `source` or `ScanMode`, or something akin to those options that has something mentioning duplex. You might have to mess around with it a little bit. Then to scan using duplex, you have to use batch mode in `scanimage` and set it to use duplex. The command would look something like this:

```bash
scanimage --device <insert full device name here> --format=png --resolution 300 --progress <insert your duplex paramter here> --batch="test%d.png"
```

This command on the scanner that I have access to, the Brother MFC-L3770CDW looks like this:

```bash
scanimage --device "brother4:net1;dev0" --format=png --resolution 300 --progress --source "Automatic Document Feeder(left aligned,Duplex)" --batch="test%d.png"
```

After you have scanned the images, if you have used the `tif` format, you can convert them into PDF files using the command below. Otherwise, there is a command in Imagemagicks `convert` command that allows you to convert any file type into a PDF.

```bash
tiff2pdf page4.tif -o page4.pdf
```

Then once you have a set of PDFs that you would like to turn into a single PDF with compression enabled, you can use the `gs` command from ghostscript as follows:

```bash
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=01A.pdf ./out/page{1..4}.pdf
```
