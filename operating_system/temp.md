操作系统
    概念: 操作系统是管理硬件和软件的程序。栗子：操作系统管理微信，并给微信分配内存、CPU等资源。
    功能: 对资源进行管理分配，如：处理机，存储器，文件，设备等资源进行管理分配。
    特征: 并发、共享、虚拟、异步，并发与共享是互相存在，是虚拟与异步的前提。
        并发: 一段时间内处理多个事件。栗子: 单个cpi一边上传文件，一边下载文件。
        并发-并行: 多个事件同时发送。栗子: 十个电脑一起下载文件。
        共享-互斥共享: 同一时间点，cpu只允许被单个线程使用。
        共享-同时共享: 一段时间，cpu运行被多个线程使用。
        虚拟-时分复用: cpu在一段时间(2s内)，1s给线程1，2s给线程2。即线程1跟2在2s内都用到了cpu。
        虚拟-空分复用: 内存１k在一段时间(2s内)，1s时先存储了线程1的数据，2s时存储了线程2的数据，即线程1跟线程2在2s内都用到了内存。内存在两s内总共可存储2k，忽略数据替换时间。
        异步: 一个任务队列，一个循环。假设有cpu-a, cpu-b，循环从任务队列中取任务，cpu-a执行任务，遇到io操作，将任务给cpu-b执行，继续从队列取任务执行。cpu-b处理好任务将任务放到任务队列。
    运行机制:用户态(非特权指令)[应用程序]、内核态(特权指令)[内核程序]
        用户态通过中断(唯一方式)进入内核态，内核态通过特权指令设置psw(程序状态)进入用户态。类似普通用户与root用户。
        中断: 内中断(cpu内部自愿中断，cpu内部故障[程序异常，硬件故障]) 外部中断(IO操作，用户ctrl+c)。
    系统调用:系统调用使处理器从用户态进入核心态，对设备管理，文件管理，进程控制，进程通信，内存管理。
        为了系统安全和稳定，获取系统资源时，需要通过系统调用(使用操作系统的功能)，使处理器从用户态进入和系统，对设备管理，文件管理，进程管理，进程通信，内存管理等
总结:
    1.裸机－硬件需要使用程序进行资源管理(操作系统)，操作系统可以管理软件。
    2.操作系统主要功能是管理处理器、存储器、IO设备、文件系统和提供用户接口。
    3.用户-应用程序调用操作系统获取资源时，会处于两种状态(用户态和内核态)。
    4.系统调用