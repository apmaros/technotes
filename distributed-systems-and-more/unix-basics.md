# Unix Basics

## File Descriptors
Everything in the Linux is a file and if it is not a file, it is a process. Each file is represented by a file descriptor.

Each process needs 3 file descriptors:
- stdin
- stdout
- stderr

They are usually inherited by the parent process. Process accesses files by using file descriptors


All accesses to files are via standard system calls which pass or return file descriptors. These descriptors are indices into the process's fd vector, so _standard input_, _standard output_, and _standard error_ have file descriptors 0, 1, and 2. Each access to the file uses the file data structure's file operation routines together with the VFS inode to achieve its needs.
