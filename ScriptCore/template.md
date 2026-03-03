In your main.py, you could implement this:
SCRIPTCORE subfile
subfile{
    FileType="the file type(supported- .css, .html, .js)"
    FileID="(your html name)"
    is_main="(boolean)"
    {
        //file code
    }
}
and the .html that contains is_main="true" will be the one that shows up when you open the main.py
