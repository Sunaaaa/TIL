# [1:N Relation]

### Foreign Key

- 참조 키의 값으로는 부모 테이블에 존재하는 키의 값만을 넣을 수 있다. 

  참조 무결성을 위해 참조키를 사용하여 **부모 테이블의 유일한 값(PK)을 참조**한다.

  - 부모 테이블의 기본키를 참조

- 참조 키의 값이 부모 테이블의 기본 키일 필요는 없지만 **<u>유일</u>**해야 한다.



<br><br>

## 1. Modeling [Models.py]

### 1.1 possible values for `on_delete`

- `CASCADE` 
  - 부모 객체가 삭제 되면 참조하는 객체도 삭제한다.
- `PROTECT` 
  - 참조가 되어 있는 경우 오류 발생!

- `SET NULL` 
  - 부모 객체가 삭제 되면 모든 값은 NULL로 치환
  - 해당 값이 NOT NULL 조건이면 불가능
- `SET DEFAULT` 
  - 모든 값이 DERAULT 값으로 치환 
  - 해당 값이 DEFAULT 값이 지정되어 있어야 함

- `SET()` 

  - 특정 함수 호출

- `DO_NOTHING` 

  - 아무것도 하지 않는다. 

    다만, DB 필드에 대한 SQL  ON_DELETE 제한 조건이 설정되어 있어야 한다.



<br>

- Comment Model을 정의한다.

  - models.py

    ```python 
    class Comment(models.Model):
        content = models.CharField(max_length=250)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        # Model Level 에서 MetaData 설정
        # 정렬
        class Meta:
            ordering = ['-pk',]
    
        # 객체 표시 형식 수정
        def __str__(self):
            return self.content
    
    ```

    

<br>

- migrate

  ![1572851641383](https://user-images.githubusercontent.com/39547788/68106762-fd4c0000-ff25-11e9-8aa2-171db1b9a465.png)

<br>



- Foreign Key

  - models.py

    ```python 
    class Comment(models.Model):
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
        content = models.CharField(max_length=250)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        # Model Level 에서 MetaData 설정
        class Meta:
            ordering = ['-pk',]
    
        # 객체 표시 형식 수정
        def __str__(self):
            return self.content
    ```

    <br>

  - 다시 migrate

    - 'Default 값' 설정 안내가 나온다.

    - 만약 데이터가 있었다면, 어떤 값으로 할래?

      ![1572851779974](https://user-images.githubusercontent.com/39547788/68106763-fd4c0000-ff25-11e9-9b3a-053560e6ac82.png)

      <br>

    - migrate 후 sqlite3 확인!

      ![1572852005354](https://user-images.githubusercontent.com/39547788/68106765-fde49680-ff25-11e9-8104-d39789b48fa0.png)

      <br>

      ![1572851989490](https://user-images.githubusercontent.com/39547788/68106764-fde49680-ff25-11e9-9732-c61ac7f28e79.png)

<br><br>



## 2. ORM 실습

> shell_plus를 이용해 댓글을 생성하고 조회해보자.

<br>

### 2.1 댓글 생성

```bash
$ python manage.py shell_plus
```

- shell_plus로 Comment 생성

  ```shell
  In [1]: article = Article.objects.get(pk=1)
  
  In [2]: comment = Comment()
  
  In [3]: comment
  Out[3]: <Comment: >
  
  In [5]: comment.content = "Hi~~"
  
  In [6]: comment.article = article
  
  In [7]: comment
  Out[7]: <Comment: Hi~~>
  
  In [8]: comment.save()
  
  In [9]: Comment.objects.all()
  Out[9]: <QuerySet [<Comment: Hi~~>]>
  
  ----------------------------------------------------------------------------
  
  In [11]: comment = Comment(article=article, content ="Second Hi")
  
  In [12]: comment.save()
  
  In [13]: Comment.objects.all()
  Out[13]: <QuerySet [<Comment: Second Hi>, <Comment: Hi~~>]>
  ```

  - Comment 생성 완료 

    - sqlite3로 확인

      ![1572852930967](https://user-images.githubusercontent.com/39547788/68106761-fd4c0000-ff25-11e9-94dc-f012d566c74b.png)

      <br>

    - Admin 페이지로 확인

      ![1572852906439](https://user-images.githubusercontent.com/39547788/68106760-fd4c0000-ff25-11e9-9cbf-fa72563fa4b6.png)

      <br>

- 해당 Comment의 article의 title 가져오기

  ```shell
  In [10]: comment.article.title
  Out[10]: '첫 번째 제목'
  ```

  <br>

###  2.2 댓글 조회

- **1:N Relation 활용하기**

  - Article (1) : Comment (N) => **comment_set**

    - `article.commnet` 형태로는 가져올 수 없다. 

    - 게시글에 몇 개의 댓글이 있는지 Django ORM 측에서 보장할 수 없다.

    - 하나의 Article에 달려있는 Comments 확인하기

      `article.comment_set.all()`

      <br>

      ```shell
      In [5]: article
      Out[5]: <Article: [1] : 첫 번째 제목 >
      
      In [6]: comments = article.comment_set.all()
      
      In [7]: comments
      Out[7]: <QuerySet [<Comment: Second Hi>, <Comment: Hi~~>]>
      
      In [8]: comments.first()
      Out[8]: <Comment: Second Hi>
      
      In [9]: comments.first().content
      Out[9]: 'Second Hi'
      ```

      <br>

  - Comment (N) : Article (1) => article

    - 댓글의 경우, `comment.article` 형태로 접근할 수 있다. 

    - 어떤 댓글이든 본인이 참조하고 있는 게시글을 반드시 있다. 

      따라서, 이런식으로 접근할 수 있다. 

      `comment.article`

      <br>

      ```shell
      In [10]: comment = comments.first()
      
      In [11]: comment
      Out[11]: <Comment: Second Hi>
      
      In [12]: comment.article
      Out[12]: <Article: [1] : 첫 번째 제목 >
      ```

      <br>

## [related_name ]

- 부모 테이블에서 역으로 참조한다.

- Article에서 Comments를 가져올때, 기본적으로 [모델이름]_set 형식으로 불러온다.

- related_name 값을 설정해서 _set 명령어를 임의로 변경할 수 있다.

- models.py 작성 예

  ```python 
  from django.db import models
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, 
      related_name='comments')
      content = models.CharField(max_length=250)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      # Model Level 에서 MetaData 설정
      class Meta:
          ordering = ['-pk',]
  
      # 객체 표시 형식 수정
      def __str__(self):
          return self.content
  ```

  <br>



## [dir(article)]

- article이 사용할 수 있는 메서드 목록 보기

  ```shell
  In [3]: article = Article.objects.get(pk=1)
  
  In [4]: dir(article)
  Out[4]: 
  ['DoesNotExist',
   'MultipleObjectsReturned',
   '__class__',
   '__delattr__',
   '__dict__',
   '__dir__',
   '__doc__',
   '__eq__',
   '__format__',
   '__ge__',
   '__getattribute__',
   '__getstate__',
   '__gt__',
   '__hash__',
   '__init__',
   '__init_subclass__',
   '__le__',
   '__lt__',
   '__module__',
   '__ne__',
   '__new__',
   '__reduce__',
   '__reduce_ex__',
   '__repr__',
   '__setattr__',
   '__setstate__',
   '__sizeof__',
   '__str__',
   '__subclasshook__',
   '__weakref__',
   '_check_column_name_clashes',
   '_check_constraints',
   '_check_field_name_clashes',
   '_check_fields',
   '_check_id_field',
   '_check_index_together',
   '_check_indexes',
   '_check_local_fields',
   '_check_long_column_names',
   '_check_m2m_through_same_relationship',
   '_check_managers',
   '_check_model',
   '_check_model_name_db_lookup_clashes',
   '_check_ordering',
   '_check_property_name_related_field_accessor_clashes',
   '_check_single_primary_key',
   '_check_swappable',
   '_check_unique_together',
   '_do_insert',
   '_do_update',
   '_get_FIELD_display',
   '_get_next_or_previous_by_FIELD',
   '_get_next_or_previous_in_order',
   '_get_pk_val',
   '_get_unique_checks',
   '_meta',
   '_perform_date_checks',
   '_perform_unique_checks',
   '_save_parents',
   '_save_table',
   '_set_pk_val',
   '_state',
   'check',
   'clean',
   'clean_fields',
   'comment_set',
   'content',
   'created_at',
   'date_error_message',
   'delete',
   'from_db',
   'full_clean',
   'get_deferred_fields',
   'get_next_by_created_at',
   'get_next_by_updated_at',
   'get_previous_by_created_at',
   'get_previous_by_updated_at',
   'id',
   'objects',
   'pk',
   'prepare_database_save',
   'refresh_from_db',
   'save',
   'save_base',
   'serializable_value',
   'title',
   'unique_error_message',
   'updated_at',
   'validate_unique']
  ```


<br>
