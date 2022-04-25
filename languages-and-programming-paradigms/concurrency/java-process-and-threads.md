# Java Process and Threads

## Process

A **process** is defined as an instance of a program that is currently running. It has a self-contained execution environment.

Both single and multicore processors can execute multiple processes at the same time. In case of a single core processor, the OS scheduler schedules a given process for a time period.

In Linux each process provides following information:

| Name    | Description                               |
| ------- | ----------------------------------------- |
| PID     | process ID                                |
| PPID    | parent process ID                         |
| STAT    | state of the process                      |
| TIME    | CPU Time used by the process              |
| TT      | control terminal of the process           |
| COMMAND | the user command that started the process |

For example in most cases a application running on JVM is running as a single process.

## Thread

The main properties of thread are:

- Thread exists within a process.
- Every process has at least one thread.
- Threads share the process's resources, including memory and open files.
  - This makes communication amongs threads efficient but also problematic

## Thread Object

There are two way to start a new thread.

By extending a `Thread` interface

```Java
public class HelloThread extends Thread {

    public void run() {
        System.out.println("Hello from a thread!");
    }

    public static void main(String args[]) {
        (new HelloThread()).start();
    }
}
```

By implementing a `Runnable` interface

```Java
public class HelloRunnable implements Runnable {

    public void run() {
        System.out.println("Hello from a thread!");
    }

    public static void main(String args[]) {
        (new Thread(new HelloRunnable())).start();
    }
}
```

Implementing a runnable is the preffered way as it makes the class more flexible. The Runnable object is passed to the Thread constructor, as in the HelloRunnable example. However, it can also be run in the executor instead.

## Join

The join method allows one thread to wait for the completion of another. If t is a Thread object whose thread is currently executing,

`t.join();`

## References

- [1] Processes and Threads; <https://docs.oracle.com/javase/tutorial/essential/concurrency/procthread.html>
