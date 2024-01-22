# JavaSE 笔记

[TOC]

## 注释

```java
// 单行注释

/*
多行注释
多行注释
*/

/**
* JavaDoc注释
* JavaDoc注释
*/
```

## 命名规范

- 类名、接口名：大驼峰 UpperCamelCase
- 方法名、变量名：小驼峰 lowerCamelCase
- 常量名：全大写
- 抽象类以Abstract、Base开头，异常类以Exception结尾，测试类以Test结尾
- POJO类中boolean变量不要加is，否则引起序列化错误

## 继承的执行顺序

1. 父类的静态代码段
2. 子类的静态代码段
3. 父类代码段
4. 父类构造方法
5. 子类代码段
6. 子类构造方法

## instanceof

用于多态情况下，向下转型之前进行运行期类型判断

使用：引用 instanceof 类型，返回true / false

```java
// Base 父类
// Child1，Child2 子类
Base b = new Child1();
if(b instanceof Child2) {
  Child2 c2 = (Child2)b;
  c2.fun();
}
```

## 常用类接口

### String

```java
String s;

// 字符串长度
int <- s.length();

// 获取指定索引值
char <- s.charAt(i);

// 判断字符串是否为空
boolean <- s.isEmpty();

// 转化为字符数组(用于范围for循环)
char[] <- s.toCharArray();

// 数字类型的字符串->int / Integer
Integer <- Integer.parseInt(s);

// 根据正则表达式拆分字符串
String[] <- s.split("res");

// 字符串截取 [startIndex, endIndex)
String <- s.substring(startIndex, endIndex);

// 去除前后空格 -> String
String <- s.trim();

// 判断字符串是否相等
// == 比较的是字符串的引用是否相等，equals比较的是内容是否相等
boolean <- s.equals(str);

-----------------------------------------------------------

// 可变字符串
StringBuffer str = new StringBuffer(); // 线程安全
StringBuilder str = new StringBuilder(); // 非线程安全，速度较快

// 尾部添加
str.append(s); // s 可以为 字符串 或 字符

// 插入字符串 / 字符
str.insert(int pos, Object data);

// 可变字符串->字符串
String <- str.toString();
```

### 数组

```java
int[] nums;

// 数组长度
int <- nums.length;
```

### List

```java
List<Integer> arr = new ArrayList<>();

// 数组长度
int <- arr.size();

// 添加元素
arr.add(num);

// 访问元素
Integer <- arr.get(i);

// 修改元素
arr.set(i, num); // i 为索引值， num 为修改值

// 删除元素
Integer <- arr.remove(i); // 删除指定索引的值，传入int时默认删除索引
boolean <- arr.remove(num); // 删除指定值

// 返回元素索引值
int <- arr.indexOf(num); // 不存在num，则返回-1

// 判断元素是否存在
boolean <- arr.contains(num);

// 排序
Collections.sort(arr);
Arrays.sort(arr);

// ArrayList -> 数组
// 引用类型
List<String> arr = new ArrayList<>();
String[] nums = arr.toArray(new String[0]);

// ArrayList -> 数组
// 非引用类型
List<Integer> arr = new ArrayList<>();
int[] nums = arr.stream().mapToInt().toArray();

// 数组 -> ArrayList
String[] nums = {"1", "2"};
List<String> arr = Arrays.asList(nums);
```

### Set

```java
Set<Integer> set = new HashSet<>();

// 添加元素
arr.add(num);

// 判断元素是否存在
boolean <- set.contains(num);

// 删除元素
boolean <- set.remove(num);

// 元素数量
int <- set.size();
```

### Map

```java
Map<Integer, String> map = new HashMap<>();

// 添加元素
map.put(key, value);

// 访问元素
String <- map.get(key);
String <- map.getOrDefault(key, defaultValue); // 获取key对应的value，不存在则返回默认值

// 删除元素
boolean <- map.remove(key);

// 判断是否存在key / value
boolean <- map.containsKey(key);
boolean <- map.containsValue(value);

// 元素数量
int <- map.size();

// 迭代遍历 Key-Value
for(Integer key : map.keySet()) {
    System.out.println(key + "-" + map.get(key));
}
// 迭代遍历 Value
for(String value : map.values()) {
    System.out.println(value);
}
```

### Stack

```java
Stack<Object> st = new Stack<>();

// 判空
boolean isEmpty();

// 返回栈顶元素
Object peek();

// 入栈
st.push(Object item);

// 栈顶元素出栈
Object pop();

// 元素数量
int size();

// 元素在栈中的位置(不存在返回-1，栈顶为1)
int search(Object item);
```

## Queue

```java
Queue<Object> que = new LinkedList<>();

// 队尾添加元素
que.offer(Object e);

// 获取并删除队头元素，队列为空返回 null
Object <- que.poll();

// 获取队头元素，队列为空返回 null
Object <- que.peek();
```