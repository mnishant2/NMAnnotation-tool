# NMAnnotation-tool
This is a simple tool to annotate keypoints in images,for your computer vision tasks.
In order to use it -you need *Opencv python2 Tkinter*
Download the code and run using command line
> python /path/to/Annotation.py 

A dialogue box will appear prompting you to select the directories.You can select multiple.Once you're done selecting the directories,close the dialog box.
Start marking keypoints on the images.Green circles will appear.
Some helpful commands-
* Next image - space (twice)
* Erase point - ‘e’
* Ignore(irrelevant/blurry) image - space+esc
* Quit - space+q
* In order to delete previous selected point in case you made an error press e,this will turn the last green point white indicating that the last point was deleted.If you have not selected any point but try to erase,an error dialog box opens .click OK and close the tk window and continue.
