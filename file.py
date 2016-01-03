文件操作
r Opens an existing file for reading.

w Opens a file for writing. If the file already
exists, the contents are deleted. If the file does
not already exist, a new one is created.

a Opens an existing file for updating, keeping the
existing contents intact.

r+ Opens a file for both reading and writing.The
existing contents are kept intact.

w+ Opens a file for both writing and reading.The
existing contents are deleted.

a+ Opens a file for both reading and writing.The
existing contents are kept intact.

b Is applied in addition to one of the read, write,
or append modes.  Opens the file in binary
mode.

U Is applied in addition to one of the read, write,
or append modes. Applies the “universal” new-
line translator to the file as it is opened.