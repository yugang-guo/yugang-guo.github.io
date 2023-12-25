# JavaSE

## 学习路线

https://www.bilibili.com/video/BV1Rx411876f/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

P1-P159、P456-end

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
int[] nums = new int[arr.size()];
arr.toArray(nums);
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



# MySQL初级

https://www.bilibili.com/video/BV1Vy4y1z7EX/?spm_id_from=333.337.search-card.all.click&vd_source=b9435537613316ae78f950a35c22f30a

# JDBC

https://www.bilibili.com/video/BV1Bt41137iB/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

不重要

# 前端

https://www.bilibili.com/video/BV1hP411679m/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

不重要，过一遍就行

# JavaWeb

https://www.bilibili.com/video/BV1Z3411C7NZ/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

重要

# 工具

## maven

## Linux

## Git

# SSM

## Mybatis

https://www.bilibili.com/video/BV1JP4y1Z73S/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

## Spring

https://www.bilibili.com/video/BV1Ft4y1g7Fb/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

## SpringMVC

https://www.bilibili.com/video/BV1oP4y1K7QT/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

# SpringBoot

https://www.bilibili.com/video/BV15b4y1a7yG/?spm_id_from=333.337.search-card.all.click&vd_source=b9435537613316ae78f950a35c22f30a

# Redis（初级）

https://www.bilibili.com/video/BV1cr4y1671t/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

## 基础

P1-P24

## 进阶（Redis项目）

P24 - P95

# SpringCloud

https://www.bilibili.com/video/BV1LQ4y127n4/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

P1 - P60、P143-P146

不重要

# 消息队列

https://www.bilibili.com/video/BV1mN4y1Z7t9/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

# JVM

https://www.bilibili.com/video/BV1yE411Z7AP/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

# 并发编程JUC

https://www.bilibili.com/video/BV16J411h7Rd/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

# MySQL（进阶）

https://www.bilibili.com/video/BV1Kr4y1i7ru/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

P58-P96、P121-P147

# Redis（进阶）

https://www.bilibili.com/video/BV1cr4y1671t/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

P145-P175

# 进阶

## 设计模式

## spring 源码

## netty

