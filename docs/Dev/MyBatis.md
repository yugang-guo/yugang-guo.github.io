# MyBatis 笔记

[TOC]

## 实现

- JDBC：Dao层（Java代码+SQL语句）
- MyBatis：Mapper接口（Java代码）+MapperXML文件（SQL语句）

> **Mapper接口**

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

> **MapperXML配置**

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

> **具体调用**

```java
//1.读取外部配置文件
InputStream ips = Resources.getResourceAsStream("mybatis-config.xml");

//2.创建sqlSessionFactory
SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(ips);

//3.创建sqlSession
SqlSession sqlSession = sqlSessionFactory.openSession();
//4.获取mapper代理对象
EmpMapper empMapper = sqlSession.getMapper(EmpMapper.class);
//5.数据库方法调用
int rows = empMapper.deleteEmpById(1);
System.out.println("rows = " + rows);
//6.提交和回滚
sqlSession.commit();
sqlSession.close();
```

SqlSessionFactory 和 Mapper 实例需交给 IoC 进行管理，MyBatis 提供了封装 SqlSessionFactory 和 Mapper 实例化的逻辑的FactoryBean组件：`SqlSessionFactoryBean`

```java
// Mapper 配置类

/**
 * 配置SqlSessionFactoryBean,指定连接池对象和外部配置文件即可
 * @param dataSource 需要注入连接池对象
 * @return 工厂Bean
 */
@Bean
public SqlSessionFactoryBean sqlSessionFactoryBean(DataSource dataSource){
    //实例化SqlSessionFactory工厂
    SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();

    //设置连接池
    sqlSessionFactoryBean.setDataSource(dataSource);

    //设置配置文件
    //包裹外部配置文件地址对象
    Resource resource = new ClassPathResource("mybatis-config.xml");
    sqlSessionFactoryBean.setConfigLocation(resource);

    return sqlSessionFactoryBean;
}

/**
 * 配置Mapper实例扫描工厂,配置 <mapper <package 对应接口和mapperxml文件所在的包
 * @return
 */
@Bean
public MapperScannerConfigurer mapperScannerConfigurer(){
    MapperScannerConfigurer mapperScannerConfigurer = new MapperScannerConfigurer();
    //设置mapper接口和xml文件所在的共同包
    mapperScannerConfigurer.setBasePackage("com.atguigu.mapper");
    return mapperScannerConfigurer;
}

```

## 基本使用

### SQL传参

1. `#{}`：占位符
2. `${}`：底层是字符串拼接

### 数据输入

1. 单参数：SQL语句中的\#{}可随意命名，建议和Mapper接口方法的参数名一致
2. POJO实体类：根据#{}中传入的数据，加工成getXxx()方法，通过反射在实体类对象中调用该方法，从而获取数据
3. 多参数：在Mapper接口方法的参数旁 定义@Param("xxx")
4. Map参数：\#{}中写Map中的key

### 数据输出

- 增删改操作返回受影响的行数，使用int / long类型接收
- 查询操作返回查询结果

> **返回类型**

resultType = "全限定符 ｜ 别名 ｜ 如果是返回集合类型，写范型类型即可"

- 若返回Map，resultType = “map”
- 若返回List，resultType 为泛型类型
- 若返回实体类，resultType 为实体类的全类名
- 返回自增主键，useGeneratedKeys="true" keyProperty="empId" ，其中keyProperty为主键在实体类中的属性名

## 多表映射

| 关联关系 | 配置项关键词                              | 所在配置文件和具体位置            |
| -------- | ----------------------------------------- | --------------------------------- |
| 对一     | association标签/javaType属性/property属性 | Mapper配置文件中的resultMap标签内 |
| 对多     | collection标签/ofType属性/property属性    | Mapper配置文件中的resultMap标签内 |

## 动态语句

> **where / if 标签**

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

> **set 标签**

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

> **choose / when / otherwise 标签**

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

> **foreach 标签**

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