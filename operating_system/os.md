[toc]

#### 操作系统
- 概念: 操作系统是管理硬件和软件的程序。
- 功能: 统一管理计算机资源(处理器、存储器、IO设备、文件资源等)。
<!-- - 总结:
    1. 操作系统是管理硬件和软件的程序，具有并发、共享、虚拟、异步等特征。
    2. 为了保证系统安全性，它封装了处理器、存储器、IO设备、文件系统的管理并向用户提供接口。
    3. 用户可以通过系统调用获取系统资源，当应用程序在用户态时，通过调用系统提供的接口，中断进入内核态，并获取系统资源。 -->
#### 进程与线程
- 概念
    - 进程是系统进行资源分配和调度的基本单位。
    - 线程是操作系统进行调度的最小单位。共享进程间资源。
- 进程控制块PCB: 记录进程当前状态和控制进程运行的全部信息。
- 进程状态: 就绪状态、执行状态、阻塞状态、创建状态、终止状态。
- 进程通信:
    - 高级通信：管道(Pipe)、内存共享(Shared Memory)、消息队列(Message Queue)、嵌套字(Socket)。
    - 低级通信: 信号(Signal)、信号量(Semaphore)
    - [参考1](https://blog.csdn.net/jeffcjl/article/details/5523569)  [参考2](https://www.cnblogs.com/yssjun/p/11438850.html) [参考3](https://www.jianshu.com/p/4989c35c9475)
- 进程管理之同步:
  生产者-消费者问题:N个生产者，N个消费者。生产者生产数据到缓冲区，消费者从缓冲区取数据。
  并发执行可能会出现错误。
    例如:缓冲区变量F=10，生产者A，取缓存区变量F，将F=F+1。此时消费者B，取缓存区变量F，
    将F=F-1。并更新缓冲区F。生产者A，缓冲区F。最终F为11。原本F应该为10。
  哲学家进餐问题:五个哲学家在一张圆桌上思考问题，桌子上有五根筷子跟五个碗，哲学家吃饭需要
  获取到最近的两根筷子。
    假设五个哲学家同时吃饭，都获取到左边的筷子，都在等待右边的筷子。结果都死了。
  进程间需要同步，协调各个资源。
  临界资源:共享资源在同一时刻只允许一个进程使用。
  同步方式:消息队列、共享存储、信号量。
  线程同步:同一进程内的线程共享进程的资源，也需要同步。方式:互斥量、读写锁、条件变量、自旋锁。
linux进程管理
  操作系统提供fork创建进程
  进程类型:前台进程、后台进程、守护进程。
    前台进程:占用终端的进程，可与用户交互。
    后台进程:没有占用终端，基本不与用户交互，优先级低于前台进程。(linux 在执行命令添加 & 可转换到后台运行)
    守护进程:特殊的后台进程,一般以d结尾。如httpd,mysqld等。
  进程的标记:
    进程ID:唯一标识,非负整数。ID为0是系统创建的第一个进程(idle)，ID为1是INIT进程，是0号进程的子进程。
    进程的状态标记:R(run运行),S(sleep睡眠),D(等待IO的睡眠态),Z(退出或僵尸进程),T(STOP暂停)
进程调度:计算机通过决策指定那个进程可以使用CPU。(需要将旧进程的上下文从高速缓存迁移到主存)
  抢占式调度(常用)，非抢占式调度。
  调度算法:先来先服务、短进程优先(不利于长作业)、高优先权优先(常用，提高用户体验)、时间片轮状(应该也常用)
死锁:两个或以上进程，竞争资源，双方阻塞，互相等待。
  死锁的产生:
    贡献资源数量不满足各个进程需求，由于各个进程之间进行资源竞争导致死锁。
    进程调度顺序不当。
  死锁四个必要条件(缺一不可)
    互斥条件:资源同一时间段，只允许一个进程的使用。
    请求保持条件:进程至少保持一个资源，又申请新的资源。新资源被占用，请求被阻塞。
    不可剥夺条件:进程获得的资源，只能由自身释放却未完成程序时不释放。
    环路等待添加:...
  预防死锁:破坏必要条件。
    破坏请求保持条件:进程在运行前需要一次性获取所有资源，运行期间不会再获取其他资源。
    破坏不可剥夺条件:进程请求新的资源无法获取时，需要释放占用的资源。
    略
  银行家算法:可操作的避免死锁的算法。将有限资源合理分配给多个进程。
    进程申请的资源有限，却申请前需要声明最大资源。
    系统在满足申请时，应该给进程申请。
    进程结束后能够立即归还资源。
存储管理之内存分配与回收
  分配过程:单一连续分配、固定分区分配、动态分区分配。
  动态分区分配算法:首次适应算法(FF)、最佳适应算法(BF)、快速适应算法(QF)
  回收:略
存储管理之段页式管理:
  页式存储:1.将进程逻辑空间等分若干个页面。2.以页面为单位，根据页面映射到物理内存(可分散)。
    如果连续的逻辑被分散在多个页面中，严重影响运行效率。
  段式存储:1.将进程逻辑空间非等分划分若干段。
  对比:页式跟段式:
    相同点:都离散地管理了进程的逻辑空间
    不同点:页是物理单位，段是逻辑单位。分页是为了合理利用空间，分段是满足用户需求。页大小有硬件固定，段长度动态变化。
  段页式管理:
    分页有限提高内存利用率，分段满足用户。段页式:先按段拆分，再将段进行分页拆分。
存储管理之虚拟内存
  虚拟内存:进程获多个进程所需要内存很大，超过物理内存。
  程序的局部性原理:CPU访问存储器时，访问区间趋近某个连续区域。
    程序运行时，装入部分内存，当访问页不存在内存时，发生页面置换。
    类似高速缓存跟主存。
  虚拟内存的置换算法:先进先出算法(FIFO)、最不经常使用算法(LFU)、最近最少使用算法(LRU)
文件系统:FAT、NTFS(FAT的进阶版)、EXT(2,3,4版本)[windows无法识别,linux可识别所有文件系统]

线程同步之互斥量(互斥锁)，对临界资源操作前进行加锁，操作后释放锁，保证操作的唯一性。
线程同步之自旋锁,自旋锁会反复检查锁变量是否会释放，会一直占用CPU。不适合单核CPU，但避免了进程或者线程的上下文切换。
  互斥锁：线程会从sleep（加锁）——>running（解锁），过程中有上下文的切换，cpu的抢占，信号的发送等开销。
  自旋锁：线程一直是running(加锁——>解锁)，死循环检测锁的标志位，机制不复杂。
  https://blog.csdn.net/susidian/article/details/51068858
线程同步之读写锁,一种特殊的自旋锁，适合多读少写。读写操作是互斥，多读操作不影响。
线程同步之条件变量，限定生产者和消费者在一定条件下进行。
  例如若缓存区为零，消费者不允许消费，休眠等待生产者生产。缓存区大于零，通信消费者消费。
fork系统调用创建新的进程(子进程,与父进程除了进程id,其他资源基本一致)，fork调用返回两次，一次返回子进程id给父进程，另一次返回0给子进程。
进程同步之共享内存:
  进程逻辑地址通过操作系统映射到实际物理地址，操作系统使得各个进程之间相互隔离，互不影响。
  通过系统调用，使得多个进程共享一片内存，达到数据共享。内存共享是高性能后台开发最常用的进程同步方式
  优点:多个进程数据共享最快的方式之一。缺点:未提供同步机制。
  步骤:申请内存空间、连接到进程空间、使用共享内存、删除共享内存。
进程同步之Unix域套接字:提供单机简单可靠的多进程通信同步服务
线程池的优势:
  1.线程本身也是一个资源。在进程内频繁创建线程会浪费大量开销。
  2.提高线程池可以让线程与程序解耦。
