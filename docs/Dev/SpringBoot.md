# SpringBoot 笔记

## 启动类

在启动类上添加注解`@SpringBootApplication` = `@Configuration` + `@ComponentScan` + `@EnableAutoConfiguration`

`@EnableAutoConfiguration`：用于启用Spring Boot的自动配置机制

```java
@SpringBootApplication
public class MainApplication {

    //SpringApplication.run() 方法是启动 Spring Boot 应用程序的关键步骤
    public static void main(String[] args) {
        SpringApplication.run(MainApplication.class,args);
    }
}
```

## 配置文件

SpringBoot 进行统一的配置管理，配置文件：`application.properties` 或 `application.yaml `（建议使用yaml文件）

配置文件的路径：`src/main/resources`

在Java代码中通过 `@Value(${xxx.xxx})` 注解来获取配置数据

批量配置文件注入：`@ConfigurationProperties` 可以将配置属性批量注入到Bean对象

```java
@Component
@ConfigurationProperties(prefix = "spring.jdbc.datasource") // prefix 前缀
public class DataSourceConfigurationProperties {
    // 不再需要使用 @Value 注解
    private String driverClassName;
    private String url;
    private String username;
    private String password;
}
```

多环境使用：开发环境 (application-dev.yml)，测试环境 (application-test.yml)，生产环境 (application-prod.yml)，在配置文件中通过`spring.profiles.active`属性来指定当前环境

## 整合SpringMVC

Web配置参数：

- `server.port`：端口号，默认为8080
- `server.servlet.context-path`：应用程序的上下文路径，默认为空
- `spring.mvc.view.prefix` `spring.mvc.view.suffix`：视图解析器的前缀、后缀
- `spring.resources.static-locations`：自定义静态资源的位置，配置后会覆盖默认位置
- `spring.http.encoding.charset` `spring.http.encoding.enabled`：HTTP请求和相应的字符编码

默认的静态资源路径

- `classpath:/META-INF/resources/`
- `classpath:/resources/`
- `classpath:/static/`
- `classpath:/public/`

拦截器：正常声明拦截器类和配置拦截器，需保证拦截器配置类在启动类的同包或子包下

## 整合MyBatis

步骤：

- 导入依赖
- `application.yml`配置数据源
- 创建实体类
- 创建Mapper接口
- 创建Mapper接口SQL实现
- 创建启动类
- 注解扫描：在Spring Boot的启动类上添加`@MapperScan`注解，用于扫描和注册Mapper接口。
- 使用Mapper接口

声明式事务：在 Service 方法中添加 `@Transactional` 注解
