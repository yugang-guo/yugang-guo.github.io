# SpringMVC 笔记

作用于Controller表述层

**核心组件**

- DispatcherServlet：web.xml配置生效，整个流程处理的核心，所有请求都经过它的处理和分发
- HandlerMapping：IoC配置生效，内部缓存handler(controller方法)和handler访问路径数据，被DispatcherServlet调用，用于查找路径对应的handler
- HandlerAdapter：IoC配置生效，处理请求参数和处理响应数据数据，每次DispatcherServlet都是通过handlerAdapter间接调用handler
- Handler：Controller类内部的方法简称，自己定义，用来接收参数，向后调用业务，最终返回响应结果
- ViewResovler：IoC配置生效，主要作用简化模版视图页面查找（前后端分离项目，后端只返回JSON数据，不返回页面，不需要ViewResovler）


## 实现

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

## 接收数据

### 访问路径

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

### 接收参数

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

### 共享域

1. `Application` 级别共享域：`ServletContext` 对象可以在整个 Web 应用程序中共享数据
2. `Session` 级别共享域：`HttpSession` 对象可以在同一用户发出的多个请求之间共享数据，但只能在同一个会话中使用。
3. `Request` 级别共享域：`HttpServletRequest` 对象可以在同一个请求的多个处理器方法之间共享数据。
4. `PageContext` 共享域：`PageContext` 对象是在 JSP 页面Servlet 创建时自动创建的，它可以在 JSP 的各个作用域中共享数据。

## 响应数据

### 页面跳转

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

### JSON数据

在配置类中加入 `@EnableWebMvc `注解

handler方法，使用 `@ResponseBody`注解，用于将方法返回的对象序列化为 JSON 或 XML 格式的数据

`RestController ` = `Controller ` + `ResponseBody `

### 静态资源

在配置类中设置静态资源处理

```java
//开启静态资源处理 <mvc:default-servlet-handler/>
@Override
public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
    configurer.enable();
}
```

## 异常处理

- 异常处理类：通过`RestControllerAdvice`声明，其中`@RestControllerAdvice = @ControllerAdvice + @ResponseBody`，`ControllerAdvice `代表当前类的异常处理controller
- 异常处理handler方法：通过`@ExceptionHandler(异常.class)`映射异常
- 配置类：确保异常处理类被 `@ComponentScan` 扫描

### 拦截器

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

### 参数校验

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
