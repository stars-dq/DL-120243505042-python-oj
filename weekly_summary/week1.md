选择：
在python中，代码的简洁性有了大幅度的提升，同时也有了诸多问题。
比如，输出一个数除以一个数时，不会像c++一样，输出其特定位数，需要你个人在python中进行设置，若结果为整数则可能会输出类似于1.0的这种.0，还需要你个人再将其转化成整数输出,y用到类似于#if b.is_integer():这种判断代码。
并且输入一堆数据时也会与c++大不相同，c++输入时使用空格就可以将一堆数据输入并运行程序，python则需要输入一个数据回车一下，这样也会导致在oj提交时无法运行程序的错误，这就会用到map函数和.spilt()将你输入的数据来达到类似于c++输入的感觉。
循环：
就像在24循环数列求和那个题，c++的输出结果是5位小数，而python则是很多位，这则需要调用round函数来限定输出位数了。
还比如当你设定一个整数型变量后，这个变量除以一个数，c++会自动向下取整，但是python则会输出小数，这就又需要一个新的运算符"//"也就是整除运算符了。但是几次方的计算就会很简洁，因为"**"这个符号就是求几次方的运算，很方便。
输出时，若是一很多数据，python会自动以回车结尾，这也需要你个人添加end=" "来解决输出回车的问题。

