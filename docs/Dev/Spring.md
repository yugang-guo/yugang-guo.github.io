# Spring 笔记

[TOC]

## IoC

### 实现

```java
//创建ioc容器对象，指定配置文件，ioc也开始实例组件对象
ApplicationContext context = new ClassPathXmlApplicationContext("services.xml", "daos.xml");
//获取ioc容器的组件对象(id, 类型)
PetStoreService service = context.getBean("petStore", PetStoreService.class);
//使用组件对象
List<String> userList = service.getUsernameList();
```

### 注解

> **Bean注解**

- @Component 普通组件Bean
  - @Controller 控制层
  - @Service 业务层
  - @Repository 持久化层

> **Bean id属性**

- 默认为类名首字母小写
- value属性指定：@Controller(value = "id")
- 注解只有一个属性时，value可省略：@Controller("id")

> **周期方法**

- PostConstruct 初始化方法
- PreDestroy 销毁方法

> **Bean属性赋值**

- 引用类型
  - @Autowired：自动装配，不需要setter方法
  - 位置：成员变量、构造器、setter方法
  - 先根据成员变量类型查找，若找到多个，再根据成员变量id查找
  - @Qualifier：指定成员变量的Bean id
- 基本类型
  - @Value：注入外部属性
  - @Value(${key})：取外部配置key对应的值!
  - @Value(${key:defaultValue})：没有key,可以给与默认值

### 配置类

> **Spring配置类注解**

  - @Configuration：标记配置类
  - @ComponentScan(basePackages = {"包","包"})：配置扫描包
  - @PropertySource("classpath:配置文件地址")：读取外部配置文件

> **创建IoC容器**

```java
ApplicationContext iocContainerAnnotation = new AnnotationConfigApplicationConte(配置类名.class);
```

> **无参构造实例化IoC容器**

```java
ApplicationContext iocContainerAnnotation = new AnnotationConfigApplicationConte();
//外部设置配置类
iocContainerAnnotation.register(配置类名.class);
//刷新后方可生效！！
iocContainerAnnotation.refresh();
```

> **第三方类**
- 无法使用@Component
- xml方式：使用<bean>
- 配置类方式：使用方法返回值+@Bean注解

> **@Bean注解**

- Bean id：@Bean("name")，省略时默认为方法名
- 初始化方法：@Bean(initMethod = "init")
- 销毁方法：@Bean(destroyMethod = "cleanup")
- 作用域：@Scope("prototype")，默认为singleton

> @Import：允许从另一个配置类加载 @Bean 定义

## AOP 面向切面编程

### 实现

- @Aspect：切面类
- @EnableAspectJAutoProxy：开启Aspectj注解支持，作用于配置类
- @Before：AOP前置通知
- @AfterReturning：AOP返回通知
- @AfterThrowing：AOP异常通知
- @After：AOP后置通知
- 属性：(value = "execution(public int com.atguigu.proxy.CalculatorPureImpl.add(int,int))")

### 通知

> **JoinPoint作为通知方法的形参**

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

> **通知方法的返回值：返回通知**

```java
@AfterReturning(
        value = "execution(public int com.atguigu.aop.api.Calculator.add(int,int))",
        returning = "targetMethodReturnValue"
)
public void printLogAfterCoreSuccess(JoinPoint joinPoint, Object targetMethodReturnValue)
```

> **异常对象捕捉：异常通知**

```java
@AfterThrowing(
        value = "execution(public int com.atguigu.aop.api.Calculator.add(int,int))",
        throwing = "targetMethodException"
)
public void printLogAfterCoreException(JoinPoint joinPoint, Throwable targetMethodException)
```

> **切点表达式**

- 示例：execution(public int com.atguigu.spring.aop.Calculator.div(int,int))
- 语法：execution(权限 返回值 包名.类名.方法名(参数列表))

> **重用切点表达式**

```java
@Pointcut("execution(public int com.atguigu.aop.api.Calculator.add(int,int)))")
public void declarPointCut() {} // 必须为无参数无返回值方法

@Before(value = "declarPointCut()")
public void printLogBeforeCoreOperation(JoinPoint joinPoint)
```

> **环绕通知**

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

> 切面优先级：@Order(value)

## 声明式事务

### 实现

- `@EnableTransactionManagement`：配置事务管理，作用于配置类
- 声明`transactionManager`方法：指定事务管理器

```java
@Bean
    public DataSourceTransactionManager transactionManager(DataSource dataSource){
        DataSourceTransactionManager transactionManager = new DataSourceTransactionManager();
        transactionManager.setDataSource(dataSource);
        return transactionManager;
    }
```

- `@Transactional`：事务注解

### 事务属性

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