# Java笔记

## JavaSE

### 注释

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

### 命名规范

- 类名、接口名：大驼峰 UpperCamelCase
- 方法名、变量名：小驼峰 lowerCamelCase
- 常量名：全大写
- 抽象类以Abstract、Base开头，异常类以Exception结尾，测试类以Test结尾
- POJO类中boolean变量不要加is，否则引起序列化错误

### 继承的执行顺序

1. 父类的静态代码段
2. 子类的静态代码段
3. 父类代码段
4. 父类构造方法
5. 子类代码段
6. 子类构造方法

### instanceof

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

### 常用类接口

#### String

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

// 可变字符串
StringBuffer str = new StringBuffer(); // 线程安全
StringBuilder str = new StringBuilder(); // 非线程安全，速度较快

// 尾部添加
str.append(s); // s 可以为 字符串 或 字符

// 可变字符串->字符串
String <- str.toString();
```

#### 数组

```java
int[] nums;

// 数组长度
int <- nums.length;
```

#### List

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

#### Set

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

#### Map

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

## JDBC

https://www.bilibili.com/video/BV1Bt41137iB/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

不重要

## JavaWeb

https://www.bilibili.com/video/BV1Z3411C7NZ/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

重要

## Maven



## Spring

### IoC

#### 实现

```java
//创建ioc容器对象，指定配置文件，ioc也开始实例组件对象
ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
//获取ioc容器的组件对象(id, 类型)
PetStoreService service = context.getBean("petStore", PetStoreService.class);
//使用组件对象
List<String> userList = service.getUsernameList();
```

#### 注解

Bean注解
- @Component 普通组件Bean
  - @Controller 控制层
  - @Service 业务层
  - @Repository 持久化层

Bean id属性
- 默认为类名首字母小写
- value属性指定：@Controller(value = "id")
- 注解只有一个属性时，value可省略：@Controller("id")

周期方法
- PostConstruct 初始化方法
- PreDestroy 销毁方法

Bean属性赋值
- 引用类型
  - @Autowired：自动装配，不需要setter方法
  - 位置：成员变量、构造器、setter方法
  - 先根据成员变量类型查找，若找到多个，再根据成员变量id查找
  - @Qualifier：指定成员变量的Bean id
- 基本类型
  - @Value：注入外部属性
  - @Value(${key})：取外部配置key对应的值!
  - @Value(${key:defaultValue})：没有key,可以给与默认值

#### 配置类

Spring配置类注解
- @Configuration：标记配置类
- @ComponentScan(basePackages = {"包","包"})：配置扫描包
- @PropertySource("classpath:配置文件地址")：读取外部配置文件

创建IoC容器
```java
ApplicationContext iocContainerAnnotation = new AnnotationConfigApplicationConte(配置类名.class);
```

无参构造实例化IoC容器
```java
ApplicationContext iocContainerAnnotation = new AnnotationConfigApplicationConte();
//外部设置配置类
iocContainerAnnotation.register(配置类名.class);
//刷新后方可生效！！
iocContainerAnnotation.refresh();
```

第三方类
- 无法使用@Component
- xml方式：使用<bean>
- 配置类方式：使用方法返回值+@Bean注解

@Bean注解
- Bean id：@Bean("name")，省略时默认为方法名
- 初始化方法：@Bean(initMethod = "init")
- 销毁方法：@Bean(destroyMethod = "cleanup")
- 作用域：@Scope("prototype")，默认为singleton

@Import：允许从另一个配置类加载 @Bean 定义

### AOP 面向切面编程

#### 实现
- @Aspect：切面类
- @EnableAspectJAutoProxy：开启Aspectj注解支持，作用于配置类
- @Before：AOP前置通知
- @AfterReturning：AOP返回通知
- @AfterThrowing：AOP异常通知
- @After：AOP后置通知
- 属性：(value = "execution(public int com.atguigu.proxy.CalculatorPureImpl.add(int,int))")

#### 通知

- JoinPoint作为通知方法的形参
```java
// 1.通过JoinPoint对象获取目标方法签名对象
Signature signature = joinPoint.getSignature();

// 2.通过方法的签名对象获取目标方法的详细信息
String methodName = signature.getName();
int modifiers = signature.getModifiers();
String declaringTypeName = signature.getDeclaringTypeName();

// 3.通过JoinPoint对象获取外界调用目标方法时传入的实参列表
Object[] args = joinPoint.getArgs();
```
- 通知方法的返回值：返回通知
```java
@AfterReturning(
        value = "execution(public int com.atguigu.aop.api.Calculator.add(int,int))",
        returning = "targetMethodReturnValue"
)
public void printLogAfterCoreSuccess(JoinPoint joinPoint, Object targetMethodReturnValue)
```
- 异常对象捕捉：异常通知
```java
@AfterThrowing(
        value = "execution(public int com.atguigu.aop.api.Calculator.add(int,int))",
        throwing = "targetMethodException"
)
public void printLogAfterCoreException(JoinPoint joinPoint, Throwable targetMethodException)
```

- 切点表达式
  - 示例：execution(public int com.atguigu.spring.aop.Calculator.div(int,int))
  - 语法：execution(权限 返回值 包名.类名.方法名(参数列表))

- 重用切点表达式
```java
@Pointcut("execution(public int com.atguigu.aop.api.Calculator.add(int,int)))")
public void declarPointCut() {} // 必须为无参数无返回值方法

@Before(value = "declarPointCut()")
public void printLogBeforeCoreOperation(JoinPoint joinPoint)
```

- 环绕通知
```java
@Around(value = "com.atguigu.aop.aspect.AtguiguPointCut.transactionPointCut()")
public Object manageTransaction(ProceedingJoinPoint joinPoint) {
    Object[] args = joinPoint.getArgs(); // 参数列表
    Signature signature = joinPoint.getSignature(); // 方法签名
    String methodName = signature.getName(); // 方法名
    Object targetMethodReturnValue = null; // 返回值
    try {
        // 前置通知
        targetMethodReturnValue = joinPoint.proceed(args);
        // 返回通知
    }catch (Throwable e){
        // 异常通知
    }finally {
        // 后置通知
    }
    return targetMethodReturnValue;
}
```

- 切面优先级：@Order(value)

### 声明式事务

#### 实现

- @EnableTransactionManagement：配置事务管理，作用于配置类
- @Transactional：事务注解

#### 事务属性

- 只读
```java
@Transactional(readOnly = true)
```

- 超时时间
```java
// 单位：秒
// 默认: -1 永不超时
@Transactional(readOnly = false,timeout = 3)
```

- 事务异常
  - 默认只针对运行时异常回滚，编译时异常不回滚
  - rollbackFor：指定哪些异常才会回滚，默认是 RuntimeException and Error
  - noRollbackFor：指定哪些异常不会回滚, 默认没有指定,如果指定,应该在rollbackFor的范围内

- 事务隔离级别：isolation
- 事务传播：propagation
  - REQUIRED 默认值，如果父方法有事务，就加入，如果没有就新建自己独立
  - REQUIRES_NEW：不管父方法是否有事务，我都新建事务，都是独立的

## MyBatis

### 实现

- JDBC：Dao层（Java代码+SQL语句）
- MyBatis：Mapper接口（Java代码）+MapperXML文件（SQL语句）

```java
// Mapper接口文件
package com.atguigu.mapper;
import com.atguigu.pojo.Employee;

public interface EmployeeMapper {

    /**
     * 根据员工id查询员工数据方法
     * @param empId  员工id
     * @return 员工实体对象
     */
    Employee selectEmployee(Integer empId);
    
}
```

```xml
<!-- MapperXML文件 -->
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "https://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!-- namespace等于mapper接口类的全限定名,这样实现对应 -->
<mapper namespace="com.atguigu.mapper.EmployeeMapper">
    
    <!-- 查询使用 select标签
            id = 方法名
            resultType = 返回值类型
            标签内编写SQL语句
     -->
    <select id="selectEmployee" resultType="com.atguigu.pojo.Employee">
        <!-- #{empId}代表动态传入的参数,并且进行赋值!后面详细讲解 -->
        select emp_id empId,emp_name empName, emp_salary empSalary from 
           t_emp where emp_id = #{empId}
    </select>
</mapper>
```

- 方法名和SQL的id一致
- 方法返回值和resultType一致
- 方法的参数和SQL的参数一致
- 接口的全类名和映射配置文件的名称空间一致

### 基本使用

#### SQL传参

1. `#{}`：占位符
2. `${}`：底层是字符串拼接

#### 数据输入

1. 单参数：SQL语句中的\#{}可随意命名，建议和Mapper接口方法的参数名一致
2. POJO实体类：根据#{}中传入的数据，加工成getXxx()方法，通过反射在实体类对象中调用该方法，从而获取数据
3. 多参数：在Mapper接口方法的参数旁 定义@Param("xxx")
4. Map参数：\#{}中写Map中的key

#### 数据输出

- 增删改操作返回受影响的行数，使用int / long类型接收
- 查询操作返回查询结果



返回类型：resultType = "全限定符 ｜ 别名 ｜ 如果是返回集合类型，写范型类型即可"

- 若返回Map，resultType = “map”
- 若返回List，resultType 为泛型类型
- 若返回实体类，resultType 为实体类的全类名
- 返回自增主键，useGeneratedKeys="true" keyProperty="empId" ，其中keyProperty为主键在实体类中的属性名

### 多表映射

| 关联关系 | 配置项关键词                              | 所在配置文件和具体位置            |
| -------- | ----------------------------------------- | --------------------------------- |
| 对一     | association标签/javaType属性/property属性 | Mapper配置文件中的resultMap标签内 |
| 对多     | collection标签/ofType属性/property属性    | Mapper配置文件中的resultMap标签内 |

### 动态语句

- where / if 标签

```sql
<where>
        <if test="empName != null">
            or emp_name=#{empName}
        </if>
        <if test="empSalary &gt; 2000">
            or emp_salary>#{empSalary}
        </if>
    </where>
```

- set 标签

```sql
<!-- 使用set标签动态管理set子句，并且动态去掉两端多余的逗号 -->
<set>
    <if test="empName != null">
        emp_name=#{empName},
    </if>
    <if test="empSalary &lt; 3000">
        emp_salary=#{empSalary},
    </if>
</set>
```

- choose / when / otherwise 标签
    - 遇到的第一个满足条件的分支会被采纳
    - 被采纳分支后面的分支都将不被考虑
    - 如果所有的when分支都不满足，那么就执行otherwise分支

```sql
<choose>
    <when test="empName != null">emp_name=#{empName}</when>
    <when test="empSalary &lt; 3000">emp_salary &lt; 3000</when>
    <otherwise>1=1</otherwise>
</choose>
```

- foreach 标签
    - collection属性：要遍历的集合
    - item属性：遍历集合的过程中能得到每一个具体对象，在item属性中设置一个名字，将来通过这个名字引用遍历出来的对象
    - separator属性：指定当foreach标签的标签体重复拼接字符串时，各个标签体字符串之间的分隔符
    - open属性：指定整个循环把字符串拼好后，字符串整体的前面要添加的字符串
    - close属性：指定整个循环把字符串拼好后，字符串整体的后面要添加的字符串
    - index属性：这里起一个名字，便于后面引用。遍历List集合，这里能够得到List集合的索引值；遍历Map集合，这里能够得到Map集合的key

```sql
<foreach collection="empList" item="emp" separator="," open="values" index="myIndex">
    <!-- 在foreach标签内部如果需要引用遍历得到的具体的一个对象，需要使用item属性声明的名称 -->
    (#{emp.empName},#{myIndex},#{emp.empSalary},#{emp.empGender})
</foreach>
```

## SpringMVC

作用于Controller表述层


**核心组件**

- DispatcherServlet：web.xml配置生效，整个流程处理的核心，所有请求都经过它的处理和分发
- HandlerMapping：IoC配置生效，内部缓存handler(controller方法)和handler访问路径数据，被DispatcherServlet调用，用于查找路径对应的handler
- HandlerAdapter：IoC配置生效，处理请求参数和处理响应数据数据，每次DispatcherServlet都是通过handlerAdapter间接调用handler
- Handler：Controller类内部的方法简称，自己定义，用来接收参数，向后调用业务，最终返回响应结果
- ViewResovler：IoC配置生效，主要作用简化模版视图页面查找（前后端分离项目，后端只返回JSON数据，不返回页面，不需要ViewResovler）



### 实现

- Controller层
    - @RequestMapping("/springmvc/hello") ：向HandlerMapping中注册路径
    - @ResponseBody：代表向浏览器直接返回数据
- 配置类 @EnableWebMvc

```java
//TODO: SpringMVC提供的接口,是替代web.xml的方案,更方便实现完全注解方式ssm处理!
//TODO: Springmvc框架会自动检查当前类的实现类,会自动加载 getRootConfigClasses / getServletConfigClasses 提供的配置类
//TODO: getServletMappings 返回的地址 设置DispatherServlet对应处理的地址
public class MyWebAppInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {

  /**
   * 指定service / mapper层的配置类
   */
  @Override
  protected Class<?>[] getRootConfigClasses() {
    return null;
  }

  /**
   * 指定springmvc的配置类
   * @return
   */
  @Override
  protected Class<?>[] getServletConfigClasses() {
    return new Class<?>[] { SpringMvcConfig.class };
  }

  /**
   * 设置dispatcherServlet的处理路径!
   * 一般情况下为 / 代表处理所有请求!
   */
  @Override
  protected String[] getServletMappings() {
    return new String[] { "/" };
  }
}
```

### 接收数据

#### 访问路径

`@RequestMapping(value = {“路径”})`

模糊匹配：`/*` 为单层任意字符串，`/**` 为任意层任意字符串

设置到类级别：通用路径；设置到方法级别：方法路径；路径 = 类路径 + 方法路径

可指定请求协议 `@RequestMapping(method = RequestMethod.POST)`

```java
public enum RequestMethod {
  GET, HEAD, POST, PUT, PATCH, DELETE, OPTIONS, TRACE
}
```

HTTP方法的变体：`@GetMapping` `@PostMapping` `@PutMapping` `@DeleteMapping` `@PatchMapping` （只能设置的Handler方法上）

#### 接收参数

**param参数**

- 直接接收：参数名 == 形参名
- `@RequestParam`：为形参绑定参数名，例如：`@RequestParam(value = "stuAge")`。默认参数必须传递，可设置为非必需传递并指定默认值：`@RequestParam(required = false,defaultValue = "18")`
- 单参数多值：使用集合接收，`@RequestParam List age`
- 实体类接收：参数名 == 实体类的属性名

**路径参数**

 * 前端路径：/user/1/root   ->   id = 1，  uname = root     即：/user/{动态部分}/{动态部分} 
 * 动态路径：`@GetMapping("/user/{id}/{name}")`
 * 形参列表：`@PathVariable Long id, @PathVariable("name") String uname`

**json参数**

创建一个接收json数据的实体类，使用 `@RequestBody` 注解来将 JSON 数据转换为 Java 对象

需在配置类中加入`@EnableWebMvc`，用于json数据处理

**Cookie数据**

```java
// Cookie示例
// JSESSIONID=415A4AC178C59DACE0B2C9CA727CDD84
(@CookieValue("JSESSIONID") String cookie)
```

**请求头数据**

`@RequestHeader`注解：`(@RequestHeader("Keep-Alive") long keepAlive)`

#### 共享域

1. `Application` 级别共享域：`ServletContext` 对象可以在整个 Web 应用程序中共享数据
2. `Session` 级别共享域：`HttpSession` 对象可以在同一用户发出的多个请求之间共享数据，但只能在同一个会话中使用。
3. `Request` 级别共享域：`HttpServletRequest` 对象可以在同一个请求的多个处理器方法之间共享数据。
4. `PageContext` 共享域：`PageContext` 对象是在 JSP 页面Servlet 创建时自动创建的，它可以在 JSP 的各个作用域中共享数据。

### 响应数据

#### 页面跳转

**jsp页面**

在配置类中进行jsp视图配置

```java
//配置jsp对应的视图解析器
@Override
public void configureViewResolvers(ViewResolverRegistry registry) {
    //快速配置jsp模板语言对应的
    registry.jsp("/WEB-INF/views/",".jsp"); // jsp页面路径的前缀和后缀
}
```

handler页面：返回值为字符串，直接返回jsp逻辑视图名

**转发、重定向**

handler页面：返回值为字符串，格式为：`关键字: /路径`，路径为项目路径，不需要添加根路径

转发关键字：`forward`，重定向关键字：`redirect`

#### 返回JSON数据

在配置类中加入 `@EnableWebMvc `注解

handler方法，使用 `@ResponseBody`注解，用于将方法返回的对象序列化为 JSON 或 XML 格式的数据

`RestController ` = `Controller ` + `ResponseBody `

#### 返回静态资源

在配置类中设置静态资源处理

```java
//开启静态资源处理 <mvc:default-servlet-handler/>
@Override
public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
    configurer.enable();
}
```

### 异常处理

- 异常处理类：通过`RestControllerAdvice`声明，其中`@RestControllerAdvice = @ControllerAdvice + @ResponseBody`，`ControllerAdvice `代表当前类的异常处理controller
- 异常处理handler方法：通过`@ExceptionHandler(异常.class)`映射异常
- 配置类：确保异常处理类被 `@ComponentScan` 扫描

#### 拦截器

- 创建拦截器类

```java
public class Process01Interceptor implements HandlerInterceptor {
    // 在处理请求的目标 handler 方法前执行
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {}
 
    // 在目标 handler 方法之后，handler报错不执行!
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {}
 
    // 渲染视图之后执行(最后),一定执行!
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {}
}
```

- 在配置类中添加拦截器

```java
//添加拦截器
@Override
public void addInterceptors(InterceptorRegistry registry) { 
    //将拦截器添加到Springmvc环境,默认拦截所有Springmvc分发的请求
    registry.addInterceptor(new Process01Interceptor());
}
```

#### 参数校验

**JSR 303**

| 注解                       | 规则                                           |
| -------------------------- | ---------------------------------------------- |
| @Null                      | 标注值必须为 null                              |
| @NotNull                   | 标注值不可为 null                              |
| @AssertTrue                | 标注值必须为 true                              |
| @AssertFalse               | 标注值必须为 false                             |
| @Min(value)                | 标注值必须大于或等于 value                     |
| @Max(value)                | 标注值必须小于或等于 value                     |
| @DecimalMin(value)         | 标注值必须大于或等于 value                     |
| @DecimalMax(value)         | 标注值必须小于或等于 value                     |
| @Size(max,min)             | 标注值大小必须在 max 和 min 限定的范围内       |
| @Digits(integer,fratction) | 标注值值必须是一个数字，且必须在可接受的范围内 |
| @Past                      | 标注值只能用于日期型，且必须是过去的日期       |
| @Future                    | 标注值只能用于日期型，且必须是将来的日期       |
| @Pattern(value)            | 标注值必须符合指定的正则表达式                 |

**Hibernate Validator**

| 注解      | 规则                               |
| --------- | ---------------------------------- |
| @Email    | 标注值必须是格式正确的 Email 地址  |
| @Length   | 标注值字符串大小必须在指定的范围内 |
| @NotEmpty | 标注值字符串不能是空字符串         |
| @Range    | 标注值必须在指定的范围内           |

<!--

# MySQL初级

https://www.bilibili.com/video/BV1Vy4y1z7EX/?spm_id_from=333.337.search-card.all.click&vd_source=b9435537613316ae78f950a35c22f30a

# 前端

https://www.bilibili.com/video/BV1hP411679m/?spm_id_from=333.999.0.0&vd_source=b9435537613316ae78f950a35c22f30a

不重要，过一遍就行

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
-->