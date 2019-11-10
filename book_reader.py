# This is the example of reading in the book, and building up a structure with
# lists. Transforming a source string text into a more complicated structure is
# called "parsing".

# Read in the sources string wonderland.txt
text = open('wonderland.txt').read()

# Split into a list of lines, so we can loop through each line and process it
lines = text.splitlines()

# Create variables that we'll use to build up our structure
paragraphs = []
current_chapter = ''
current_paragraph = ''
chapters = []

# Loop through each line in the text file
for line in lines:

    # "strip" will remove extraneous spaces from beginning and end
    line = line.strip()

    # Does the line start with CHAPTER, indicating the start of a chapter?
    if line.startswith('CHAPTER'):
        # If so, lets mark this as the current chapter we are processing
        current_chapter = line

        # ...and reset the paragraphs list, which we will use to build up the
        # paragraphs contained in that chapter
        paragraphs = []

        # ...and then, build up the "chapters" list, which is a list of all the
        # chapters in our book
        chapters.append([current_chapter, paragraphs])

        # ...and then continue on to the next line.
        continue

    # If there is no chapter presently specified, continue (this happens only
    # in the beginning, allowing us to skip over the initial copyright info).
    if not current_chapter:
        continue

    # "Grow" the current paragraph by this line (+= adds to a variable)
    current_paragraph += ' ' + line


    # If we find the text "THE END", lets just stop right now
    if line == 'THE END':
        break

    # "not line" means its an empty line. This is some code to "cut off" the
    # current paragraph, and also clean up some garbage-y paragraphs that only
    # consist of asterisk that exist in the source text
    if not line:
        current_paragraph = current_paragraph.strip(' *')
        if current_paragraph:
            paragraphs.append(current_paragraph)
        current_paragraph = ''

print(chapters[0])

# This following code is not necessary, but saves in a file the intermediate
# data so we can better debug and visualize what is going on.
# This "import json" thing can be found from Googling.
#import json
#open('wonderland.json', 'w+').write(json.dumps(chapters, indent=4))

# Now, lets loop through the chapters again and output the resulting HTML

# Notice that we can omit the "write" on the "open" line, and then instead
# write a little at a time as we need to.
f = open('wonderland.html', 'w+')

# Start by writing the boilerplate.
f.write('''
<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Alice in Wonderland</title>
    <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css">
</head>
<body>
<h1>Alice in Wonderland</h1>
''')

# Then, loop through the chapters
for chapter_title, contents in chapters:

    # Output the title in an "h2" tag
    f.write('<h2>' + chapter_title + '</h2>')

    # Loop through the paragraphs inside of this chapter
    for paragraph in contents:
        # And output the paragraph in a "p" tag
        f.write('<p>' + paragraph + '</p>')

    # Finally, ad a horizontal rule at the end of each chapter, to look nice
    f.write('<hr />')


# And output the final boilerplate at the end of the file.
f.write('''
</body>
</html>
''')
