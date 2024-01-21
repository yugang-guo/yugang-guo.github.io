# 项目插件笔记

[TOC]

## Maven

### GAVP

- Group ID：项目所属的组织或包，通常为组织的域名倒序
- Artifact ID：项目的唯一标识符，通常为项目名
- Version：项目版本号
- Packagng：项目打包方式：jar、war、pom，默认为jar

```xml
<!-- pom.xml -->
<project>
    <groupId>com.example</groupId>
    <artifactId>my-project</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    <!-- 其他配置 -->
</project>

```

## JWT

Java Web Token（JWT）：生成,校验,解析等动作Token的技术

token：一串随机生成的字符或数字，用于验证用户的身份或授权用户对特定资源的访问，

> **导入依赖**

```xml
<dependency>
    <groupId>io.jsonwebtoken</groupId>
    <artifactId>jjwt</artifactId>
    <version>0.9.1</version>
</dependency>

<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```

> **配置**（application.yaml）

```yaml
#jwt配置
jwt:
  token:
    tokenExpiration: 120 #有效时间,单位分钟
    tokenSignKey: headline123456  #当前程序签名秘钥 自定义
```

> **JWT 工具类**

```java
@Data
@Component
@ConfigurationProperties(prefix = "jwt.token")
public class JwtHelper {

    private  long tokenExpiration; //有效时间,单位毫秒 1000毫秒 == 1秒
    private  String tokenSignKey;  //当前程序签名秘钥

    //生成token字符串
    public  String createToken(Long userId) {
        String token = Jwts.builder()
                .setSubject("YYGH-USER")
                .setExpiration(new Date(System.currentTimeMillis() + tokenExpiration*1000*60)) //单位分钟
                .claim("userId", userId)
                .signWith(SignatureAlgorithm.HS512, tokenSignKey)
                .compressWith(CompressionCodecs.GZIP)
                .compact();
        return token;
    }

    //从token字符串获取userid
    public  Long getUserId(String token) {
        if(StringUtils.isEmpty(token)) return null;
        Jws<Claims> claimsJws = Jwts.parser().setSigningKey(tokenSignKey).parseClaimsJws(token);
        Claims claims = claimsJws.getBody();
        Integer userId = (Integer)claims.get("userId");
        return userId.longValue();
    }

    //判断token是否有效
    public  boolean isExpiration(String token){
        try {
            boolean isExpire = Jwts.parser()
                    .setSigningKey(tokenSignKey)
                    .parseClaimsJws(token)
                    .getBody()
                    .getExpiration().before(new Date());
            //没有过期，有效，返回false
            return isExpire;
        }catch(Exception e) {
            //过期出现异常，返回true
            return true;
        }
    }
}
```

## Lombok

通过添加注解来简化java代码的编写

- `@Getter` `@Setter`：自动生成 getter 和 setter 方法
- `@ToString`：自动生成 toString 方法
- `@NoArgsConstructor` `@AllArgsConstructor` `@RequiredArgsConstructor`：自动生成无参构造函数、全参构造函数、要求字段的构造函数
- `@EqualsAndHashCode`：自动生成 equals 和 hashCode 方法
- `@Data`：包含 `@ToString`, `@EqualsAndHashCode`, `@Getter`, `@Setter` 和 `@RequiredArgsConstructor` 的组合注解。
- `@Builder`：自动生成构造器方法

```java
@Builder
public class Example {
    private String name;
    private int age;

    public static void main(String[] args) {
        Example example = Example.builder()
                                 .name("John")
                                 .age(25)
                                 .build();
    }
}
```

## FastSON

阿里巴巴JSON 处理库，用于在 java 代码中处理 JSON 数据

> **导入依赖**

```xml
<!-- pro.xml -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.79</version> <!-- 使用最新版本 -->
</dependency>
```

> **使用**

- 引入 JSON 包

```java
import com.alibaba.fastjson.JSON;
```

- Java实体类 -> JSON字符串

```java
User user = new User("John Doe", 25);
String jsonString = JSON.toJSONString(user);
```

- JSON字符串 -> Java实体类

```java
String jsonString = "{\"name\":\"John Doe\",\"age\":25}";
User user = JSON.parseObject(jsonString, User.class);
```

