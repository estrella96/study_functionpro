# 高级特性
## 函数式编程（FunctionalProgramming）
- 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数和返回值
    - 纯函数式编程语言 LISP Haskell
- Python只是借助函数式编程的一些特点
    - 高阶函数
    - 返回函数
    - 匿名函数
    - 装饰器
    - 偏函数
### lambda表达式 01.py
- 函数：最大程度复用代码
    - 存在问题：如果函数很小很短 反而会使程序复杂
    - 如果函数被调用次数少 会造成浪费
    - 不容易阅读
- lambda表达式（匿名函数）：
    - 一个表达式 函数体相对简单
    - 不是一个代码块 只是一个表达式
    - 可以有参数 逗号隔开
    - 用法 以lambda开头，紧跟参数，参数后用冒号，只是一个表达式没有return
### 高阶函数
- 把函数作为参数使用的函数（函数名就是一个变量 不加括号）
- 系统高阶函数-map
    - 原意是映射 把集合或者列表的元素 每一个元素按一定规则进行操作 生成一个新的列表或集合
    - map函数式系统提供的具有映射功能的函数 返回值是一个迭代对象
- reduce
    - 归并 缩减
    - 把一个可迭代对象最后归并为一个结果
    - 作为参数的函数要求：两个参数 必须有返回结果
        reduce([1,2,3,4,5])==f(f(f(f(1,2),3),4),5)
    - 导入functools包
- filter
    - 过滤函数：对一组数据进行过滤 符合条件的生成新的列表并返回
    - 跟map相比
        - 相同 都对列表中每一个元素逐一操作
        - 不同 map生成一个与原来数据相对应的新队列filter不一定
    - 利用给定函数进行判断 返回值是布尔值
        filter(f,data)
        返回的是filter的可迭代对象
- 排序
    - 将序列按给定算法进行排序
    - key：在排序前对每一个元素进行key函数运算 可以理解为按key函数定义的逻辑进行排序
### 返回函数 02.py
- 函数可以返回具体的值 也可以返回一个函数作为结果
- 函数作为返回值返回，被返回的函数在函数体内定义
### 闭包（closure）
- 当一个函数在内部定义函数，并且内部函数用外部函数的参数或局部变量，
当内部函数被当做返回值时，相关参数和变量保存在返回的函数中 
这种结果叫闭包
- 返回闭包时，返回函数不能引用任何循环变量
### 装饰器
- 不改动函数代码基础上扩展函数功能
- 返回函数的高阶函数
- 使用 @+函数名
- 一旦定义可以装饰任意函数
- 一旦被其装饰 装饰器的功能直接添加到定义函数的功能上
### 偏函数
- 参数固定的函数 相当于一个由特定参数的函数体
- functools.partial:把一个函数的某些参数固定 返回一个新函数

# 高级函数 03.py
## zip
- 把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
## enumerate
- 与zip功能相似
- 对可迭代对象的每一个元素 配上一个索引 形成tuple元组
## collections 模块
- namedtuple 类似结构体
    - 可命名的tuple
- deque
    - 解决频繁删除插入问题
- defaultdict
    - 直接读取dict不存在的属性时，直接返回默认值
- Counter
    - 统计字符串个数
    
# 文件 04.py
- 长久保存信息的数据集合
- 常用操作
    - 打开关闭（打开的文件需要关闭）
    - 读写内容
    - 查找
## open函数
- 打开文件 
- 参数：
    - 文件路径和名称
    - mode：打开方式 
        r 
        w（覆盖旧内容） 
        x(创建方式打开) 
        a(append方式 追加写)
        b（二进制方式）
        t（文本方式打开）
        +读写
## with语句
- with语句使用成为上下文管理协议的技术（ContextManagementProtocal）
- 自动判断文件作用域 自动关闭文件句柄 不需要close
##read
- 按字符读取
- 可以从当前位置指定读取几个字符 默认到结尾
## sake(offset,from)
- 移动文件的读取位置/指针
- from：
    - 0：从文件头开始偏移
    - 1：从当前位置开始偏移
    - 2：从文件末尾开始偏移
- 移动的单位是字节(byte)
- 返回文件只针对当前位置
## tell
- 显示文件读写指针的当前位置
- 返回数字的单位是byte
## write
- write(str):字符串写入文件
- writelines(str):写入很多行 参数可以是list 字符串/字符序列

#pickle 序列化
- 保存在磁盘
- pickle:python提供的序列化模块
- pickle.dump 序列化
- pickle.load 反序列化

#shelve 持久化工具
- 类似字典 用kv对保存数据
- open
- close
- 不支持多个应用并行写入
- 写回问题
    不会等待持久化对象进行任何修改
    
# log 05.py
- https://www.cnblogs.com/yyds/p/6901864.html
- logging 模块提供模块级别的函数记录日志
- 包括四大组件
## 1.日志相关概念
- 日志
- 日志级别level
    - 不同的用户关注不同的程序信息
    - DEBUG INFO NOTICE WARNING ERROR CRITICAL ALERT EMERGENCY
- LOG 作用
   调试 了解软件运行情况 分析定位问题
- 日志信息
   - time
   - 地点
   - level
   - 内容
## 2 logging模块
- 初始化/ 写日志实例需要指定级别 当级别等于或高于指定级别才被记录
- 使用方式
    - 使用logging
        - logging.debug
        - logging.info
        - logging.warning
        - logging.critical
        - logging.log
        - logging.basicConfig 只在第一次调用时起作用 warning级别
    - logging四大组件直接定制
- format log格式
- 四大组件
    - 日志器Logger：产生日志的一个接口
    - 处理器Handler：把产生的日志发送到相应的目的地
    - 过滤器Filter：更精细的控制哪些日志输出
    - 格式器Formatter：对输出信息进行格式化
- Logger
    - setLevel()
    - addHandler()/remove
    - addFilter()/remove 
    - debug():产生一条debug级别的日志
    - logging.getLogger() 得到一个logger对象
- Handler
    - 把log发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter,removeFilter 
    - Handler是基类
        logging.StreamHandler 写入流
        logging.FileHandler 写入磁盘
        logging.handlers.RotatingFileHandler
- Format
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 参数
        - fmt 指定消息格式化字符串
        - datefmt 指定日期格式字符串
        - style
- Filter
    - 控制传递过来的信息的具体内容
    - 被logger和handler使用
    
# 多线程 
- 线程的共享和互斥
- 全局解释器锁GIL
    - python代码执行由python虚拟机控制
    - 在主循环中只能有一个控制线程在执行
- python包
    - _thread 06.py/07.py/08.py
    - threading
- threading 09.py
    - 用threading.Thread生成Thread实例
        1. t=threading.Thread(target=xxx,args=(xxx,))
        2. t.start():启动多线程
        3. t.join():等待多线程执行完成
    - 守护线程-daemon 10.py
        - 设置为守护线程的子线程会在主线程结束时自动退出
        - 守护线程一般不允许离开主线程独立运行
        - 能否有效与环境相关
    - 线程属性
        - threading.currentThread
        - threading.enumerate
        - threading.activeCount
        - thr.setName
        - thr.getName
    - 直接用Thread 11.py
        - 重写run函数